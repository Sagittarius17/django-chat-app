const localVideo = document.getElementById('localVideo');
const remoteVideo = document.getElementById('remoteVideo');

let localStream;
let remoteStream;
let peerConnection;

// Getting media devices: microphone and camera
function connectToRoom() {
    const enteredRoomName = document.getElementById('roomName').value;
    if (enteredRoomName) {
        console.log("Connecting to room:", enteredRoomName);
        
        // Get user's media stream when they attempt to connect to a room
        navigator.mediaDevices.getUserMedia({ video: true, audio: true })
            .then(stream => {
                localStream = stream;
                localVideo.srcObject = localStream;
                setupPeerConnection(enteredRoomName);  // Only setup peer connection after local stream is ready
            })
            .catch(error => {
                console.error('Error accessing media devices.', error);
            });
    } else {
        console.error('Please enter a room name.');
    }
}


function setupPeerConnection(roomName) {
    const configuration = { 
        iceServers: [{ urls: "stun:stun.l.google.com:19302" }] 
    };

    peerConnection = new RTCPeerConnection(configuration);

    // Set the local stream to the peer connection
    localStream.getTracks().forEach(track => {
        peerConnection.addTrack(track, localStream);
    });

    // Listen for the remote stream and set it to the remote video element
    peerConnection.ontrack = event => {
        if (event.streams[0] !== remoteStream) {
            remoteStream = event.streams[0];
            remoteVideo.srcObject = remoteStream;
        }
    };

    // WebSocket signaling
    const socket = new WebSocket(`ws://localhost:8001/ws/videocall/${roomName}/`);

    // Handle WebSocket errors
    socket.onerror = (error) => {
        console.error("WebSocket Error: ", error);
    };

    // Once the socket is open, create an offer
    socket.onopen = () => {
        peerConnection.createOffer()
            .then(offer => peerConnection.setLocalDescription(offer))
            .then(() => {
                socket.send(JSON.stringify({ "offer": peerConnection.localDescription }));
            })
            .catch(error => {
                console.error('Error sending offer:', error);
            });
    };

    // When receiving a message from the server
    socket.onmessage = event => {
        const msg = JSON.parse(event.data);
        if (msg.answer) {
            const remoteOffer = new RTCSessionDescription(msg.answer);
            peerConnection.setRemoteDescription(remoteOffer);
        } else if (msg.ice_candidate) {
            const iceCandidate = new RTCIceCandidate(msg.ice_candidate);
            peerConnection.addIceCandidate(iceCandidate);
        }
    };

    // Handle ICE Candidate events
    peerConnection.onicecandidate = event => {
        if (event.candidate) {
            socket.send(JSON.stringify({ 'ice-candidate': event.candidate }));
        }
    };
}
