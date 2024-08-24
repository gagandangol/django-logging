import logging #import logging module

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger('django') #initiate our logger

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
            logger.info(str(e))
            return HttpResponse('Something bad occured..')
    