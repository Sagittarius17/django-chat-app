import requests
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
# from .forms import SignupForm, LoginForm

def main_layout(request):
    # Make an API request
    url = "your API url"

    headers = {
        "X-RapidAPI-Key": "your API key",
        "X-RapidAPI-Host": "your host"
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the JSON data from the response
        data = response.json()
        # print(data)
        # Process the data as needed
        # ...

        # Pass the data to the template
        return render(request, 'main/index.html', {'data': data})

    # Handle the case when the request was not successful
    else:
        # Display an error message or redirect to an error page
        print('something went wrong!')


# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             # Create a new user
#             form.save()
#             return redirect('login')
#     else:
#         form = SignupForm()
#     return render(request, 'main/signup.html', {'form': form})

# def user_login(request):
    # if request.method == 'POST':
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         user = authenticate(request, username=username, password=password)
    #         if user is not None:
    #             login(request, user)
    #             return redirect('home')
    #         else:
    #             form.add_error(None, 'Invalid credentials')
    # else:
    #     form = LoginForm()
    # return render(request, 'main/signin.html', {'form': form})

# def user_logout(request):
#     logout(request)
#     return redirect('home')



