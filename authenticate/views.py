import logging #import logging module

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger('django') #Get an instance of a logger

def login_view(request):
        
        try:
            if request.method == "POST":

                # Attempt to sign user in
                username = request.POST["username"]
                password = request.POST["password"]

                # user = authenticate(request, username=username, password=password)

                # Check if authentication successful
                if user is not None:
                    login(request, user)
                    return HttpResponse('Successfully logged in...')
                else:
                    return HttpResponse("Invalid username and/or password.")
            else:
                return render(request, 'authenticate/login.html')
        except Exception as e:
            logger.error(str(e), exc_info=True) #added exception handling for better error handling
            return HttpResponse('Out of service! <br> Please try again later...')
    