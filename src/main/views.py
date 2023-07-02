import requests
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token


def index(request):
    return render(request, 'main/index.html')


@login_required
def list_from_api(request):
    # Retrieve the authentication token for the user
    csrf_token = get_token(request)
    
    # Make a request to the API
    api_url = 'http://127.0.0.1:8000/api/member/?format=json'
    # The cookie is needed for authentication
    headers = {
        'Cookie': 'csrftoken=' + csrf_token + '; sessionid=' + request.session.session_key,
    }
    # Make the request
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        results = response.json()
        return render(request, 'main/list.html', {'results': results})
    else:
        return JsonResponse(response.json(), status=response.status_code)
