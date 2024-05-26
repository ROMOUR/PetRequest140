import pytest
import requests
import json
from utils.utils import ler_csv


pet_id = 389
pet_name = "Schott"
pet_category_id = 1
pet_category_name = "dog"
pet_tag_id = 1
pet_tag_name = "vacinado"

url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-type': "application/json"}


def load_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def test_post_pet():
    data = load_json('./fixtures/json/pet1.json')

    response = requests.post(
        url=url,
        headers=headers,
        data=json.dumps(data),
        timeout=5
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['category']['name'] == pet_category_name
    assert response_body['tags'][0]['name'] == pet_tag_name


def test_get_pet():
    response = requests.get(
        url=f'{url}/{pet_id}',
        headers=headers,
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['name'] == pet_name
    assert response_body['category']['id'] == pet_category_id
    assert response_body['tags'][0]['id'] == pet_tag_id
    assert response_body['status'] == 'available'


def test_put_pet():
    data = load_json('./fixtures/json/pet2.json')

    response = requests.put(
        url=url,
        headers=headers,
        data=json.dumps(data),
        timeout=5
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['category']['name'] == pet_category_name
    assert response_body['tags'][0]['name'] == pet_tag_name
    assert response_body['category']['id'] == pet_category_id
    assert response_body['tags'][0]['id'] == pet_tag_id
    assert response_body['status'] == 'sold'


def test_delete_pet():
    response = requests.delete(
        url=f'{url}/{pet_id}',
        headers=headers,
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(pet_id)


@pytest.mark.parametrize('pet_id,category_id,category_name,pet_name,tags,status', ler_csv('./fixtures/csv/pets.csv'))
def test_post_pet_from_csv(pet_id, category_id, category_name, pet_name, tags, status):
    pet = {
        'id': int(pet_id),
        'category': {'id': int(category_id), 'name': category_name},
        'name': pet_name,
        'photoUrls': [''],
        'tags': [{'id': int(tag.split('-')[0]), 'name': tag.split('-')[1]} for tag in tags.split(';')],
        'status': status
    }

    response = requests.post(
        url=url,
        headers=headers,
        data=json.dumps(pet),
        timeout=5
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id'] == int(pet_id)
    assert response_body['name'] == pet_name
    assert response_body['status'] == status