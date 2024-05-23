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

def test_post_user():
    user = open('./fixtures/json/user1.json')        
    data = json.loads(user.read())                  

   
    response = requests.post(
        url = url,
        headers = headers,
        data = json.dumps(data),
        timeout = 5
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

    user = open('./fixtures/json/user2.json')
    data = json.loads(user.read())

    response = requests.put(
        url=f'{url}/{user_username}',
        headers=headers,
        data=json.dumps(data),
        timeout= 5 
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



@pytest.mark.parametrize('user_id,user_username,user_firstname,user_lastname,user_email,user_password,user_phone,user_status',
                         ler_csv('./fixtures/csv/user.csv')
                         )



def test_post_user_dinamico(user_id,user_username,user_firstname,user_lastname,user_email,user_password,user_phone,user_status):
    user = {}     # lista vazia pet 
    user['id'] = int(user_id)
    user['username'] = user_username
    user['firstName'] = user_firstname
    user['lastName'] = user_lastname
    user['email'] = user_email
    user['password'] = user_password
    user['phone'] = user_phone
    user['user_Status'] = user_status



    user = json.dumps(obj=user, indent=4)
    print('\n' + user)                     


    response = requests.post(
        url=url,
        headers=headers,
        data=user,
        timeout=5
    )
    
    response_body = response.json()

    assert response.status_code == 200



@pytest.mark.parametrize('user_id,user_username,user_firstname,user_lastname,user_email,user_password,user_phone,user_status',
                         ler_csv('./fixtures/csv/user.csv')
                         )



def test_post_user_dinamico(user_id,user_username,user_firstname,user_lastname,user_email,user_password,user_phone,user_status):
    
    user = {}     # lista vazia pet 
    user['id'] = int(user_id)
    user['username'] = user_username
    user['firstName'] = user_firstname
    user['lastName'] = user_lastname
    user['email'] = user_email
    user['password'] = user_password
    user['phone'] = user_phone
    user['user_Status'] = user_status
    

    response = requests.delete(
        url=f'{url}/{user_username}',
        headers=headers,
        data=user,
        timeout=5
    )
    #compara
    response_body = response.json()

    assert response.status_code == 200 
    assert response_body['code'] == 200 
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == user