import requests
#pip install requests
# Post create
# get is fetch/ read /
# put and patch update
# delete
#
# Api testing validating for better quality UI or api mobile app deskapp testing
#     API testing
#
# send valid requestshave valid response
# validate from response
# 1 status code
# 2 headers
# 3 response body parameters
# size
# restime :perfromtesting
#



import pytest

ENDPOINT = "https://todo.pixegami.io"

response = requests.get(ENDPOINT)

# print(response)
data = response.json()


# print(response.status_code)
# print(data)

def test_call():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


def test_create():
    payload = {
        "content": "testing",
        "user_id": "testsuite",
        "task_id": "stateside",
        "is_done": False
    }
    response_p = requests.put(ENDPOINT+ "/create-task", json=payload)
    assert response_p.status_code == 200
    data = response_p.json()
    print(data)
