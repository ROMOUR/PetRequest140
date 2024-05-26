import requests
import json

base_url = "https://petstore.swagger.io/v2"
headers = {"Content-Type": "application/json"}


def test_create_user():
    url = f"{base_url}/user"
    user_data = {
        "id": 12345,
        "username": "testuser",
        "firstName": "Test",
        "lastName": "User",
        "email": "testuser@example.com",
        "password": "password",
        "phone": "1234567890",
        "userStatus": 0
    }

    response = requests.post(url, data=json.dumps(user_data), headers=headers)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    

def test_get_user():
    username = "testuser"
    url = f"{base_url}/user/{username}"
    
    response = requests.get(url, headers=headers)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
    user_data = response.json()
    assert user_data["id"] == 12345, f"Expected user ID 12345, but got {user_data['id']}"
    assert user_data["username"] == "testuser", f"Expected username 'testuser', but got {user_data['username']}"
    assert user_data["email"] == "testuser@example.com", f"Expected email 'testuser@example.com', but got {user_data['email']}"

def test_update_user():
    username = "testuser"
    url = f"{base_url}/user/{username}"
    updated_data = {
        "id": 12345,
        "username": "testuser",
        "firstName": "Updated",
        "lastName": "User",
        "email": "updateduser@example.com",
        "password": "newpassword",
        "phone": "0987654321",
        "userStatus": 1
    }

    response = requests.put(url, data=json.dumps(updated_data), headers=headers)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
  
    response = requests.get(url, headers=headers)
    user_data = response.json()
    assert user_data["firstName"] == "Updated", f"Expected firstName 'Updated', but got {user_data['firstName']}"
    assert user_data["email"] == "updateduser@example.com", f"Expected email 'updateduser@example.com', but got {user_data['email']}"
    assert user_data["phone"] == "0987654321", f"Expected phone '0987654321', but got {user_data['phone']}"

def test_delete_user():
    username = "testuser"
    url = f"{base_url}/user/{username}"
    
    response = requests.delete(url, headers=headers)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
 
    response = requests.get(url, headers=headers)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

if __name__ == "__main__":
    test_create_user()
    print("Test Create User: PASSED")

    test_get_user()
    print("Test Get User: PASSED")

    test_update_user()
    print("Test Update User: PASSED")

    test_delete_user()
    print("Test Delete User: PASSED")