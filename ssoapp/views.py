import jwt
import requests
import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    id_token = request.session['oidc_id_token']
    claims = jwt.decode(id_token, verify=False) 
    url = 'https://jsonplaceholder.typicode.com/users/2'
    response = requests.get(url)
    data = response.json()
    print(claims)
    print(claims['sub'])
    return render(request, 'profile.html',  {
            'claims': claims,
            'data': data
            }) 