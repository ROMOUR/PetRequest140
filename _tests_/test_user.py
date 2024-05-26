import pytest
import requests   
import json
from utils.utils import ler_csv

user_id = 3899963941
user_username = "Rodolfo"
user_firstname = "test"
user_lastname = "Moura"
user_email = "rodolfo_itg@yahoo.com.br"
user_password = "12345"
user_phone = "996394136"
user_status = 1

url= 'https://petstore.swagger.io/v2/user'                 
headers= {'Content-type':"application/json"}  

def load_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def test_post_user():
    data = load_json('./fixtures/json/user1.json')

    response = requests.post(
        url=url,
        headers=headers,
        data=json.dumps(data),
        timeout=5
    )
    response_body = response.json()                 
    
    assert response.status_code == 200 

def test_get_user():
    response = requests.get(
        url=f'{url}/{user_username}',
        headers=headers,
    )

    response_body = response.json()

    assert response.status_code == 200

def test_put_user():
    data = load_json('./fixtures/json/user2.json')

    response = requests.put(
        url=f'{url}/{user_username}',
        headers=headers,
        data=json.dumps(data),
        timeout=5 
    )

    response_body = response.json()

    assert response.status_code == 200 

def test_delete_user():
    response = requests.delete(
        url=f'{url}/{user_username}',
        headers=headers,
    )

    response_body = response.json()

    assert response.status_code == 200 
    assert response_body['code'] == 200 
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == user_username

@pytest.mark.parametrize('user_id,user_username,user_firstname,user_lastname,user_email,user_password,user_phone,user_status', ler_csv('./fixtures/csv/user.csv'))
def test_post_user_from_csv(user_id, user_username, user_firstname, user_lastname, user_email, user_password, user_phone, user_status):
    user = {
        'id': int(user_id),
        'username': user_username,
        'firstName': user_firstname,
        'lastName': user_lastname,
        'email': user_email,
        'password': user_password,
        'phone': user_phone,
        'userStatus': int(user_status)
    }

    response = requests.post(
        url=url,
        headers=headers,
        data=json.dumps(user),
        timeout=5
    )
    
    response_body = response.json()

    assert response.status_code == 200

@pytest.mark.parametrize('user_id,user_username,user_firstname,user_lastname,user_email,user_password,user_phone,user_status', ler_csv('./fixtures/csv/user.csv'))
def test_delete_user_from_csv(user_id, user_username, user_firstname, user_lastname, user_email, user_password, user_phone, user_status):
    response = requests.delete(
        url=f'{url}/{user_username}',
        headers=headers,
        timeout=5
    )
    
    response_body = response.json()

    assert response.status_code == 200 
    assert response_body['code'] == 200 
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == user_username