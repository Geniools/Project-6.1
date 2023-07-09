import requests
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.urls import reverse

from main.utils import convert_xml_to_dict


def index(request):
    return render(request, 'main/index.html')


@login_required
def list_from_api_json(request, page=1):
    # Retrieve the authentication token for the user
    csrf_token = get_token(request)
    # Make a request to the API
    api_url = f'http://127.0.0.1:8000/api/member/?format=json&page={page}'
    # The cookie is needed for authentication
    headers = {
        'Cookie': 'csrftoken=' + csrf_token + '; sessionid=' + request.session.session_key,
    }
    # Make the request for json data
    json_response = requests.get(api_url, headers=headers)
    json_result = json_response.json()
    # Next and previous page urls
    previous_page, next_page = None, None
    if json_result['next']:
        next_page = reverse('list-json', kwargs={'page': page + 1})
    
    if json_result['previous']:
        previous_page = reverse('list-json', kwargs={'page': page - 1})
    
    result = {
        'result': json_result,
        'previous_page': previous_page,
        'next_page': next_page,
        'format': 'json',
    }
    
    if json_response.status_code != 200:
        return JsonResponse(f"JSON request error: {json_response.json()}", status=json_response.status_code)
    
    return render(request, 'main/list.html', result)


@login_required
def list_from_api_xml(request, page=1):
    # Retrieve the authentication token for the user
    csrf_token = get_token(request)
    # Make the request for xml data
    api_url = f'http://127.0.0.1:8000/api/member/?format=xml&page={page}'
    # The cookie is needed for authentication
    headers = {
        'Cookie': 'csrftoken=' + csrf_token + '; sessionid=' + request.session.session_key,
    }
    # Make the request for xml data
    xml_response = requests.get(api_url, headers=headers)
    xml_result = convert_xml_to_dict(xml_response.content)['root']
    xml_result['results'] = xml_result['results']['list-item']
    if not isinstance(xml_result['results'], list):
        xml_result['results'] = [xml_result['results']]
        # Next and previous page urls
    previous_page, next_page = None, None
    if xml_result['next']:
        next_page = reverse('list-xml', kwargs={'page': page + 1})
    
    if xml_result['previous']:
        previous_page = reverse('list-xml', kwargs={'page': page - 1})
    
    result = {
        'result': xml_result,
        'previous_page': previous_page,
        'next_page': next_page,
        'format': 'xml',
    }
    
    if xml_response.status_code != 200:
        return JsonResponse(f"XML request error: {xml_response.json()}", status=xml_response.status_code)
    
    return render(request, 'main/list.html', result)
