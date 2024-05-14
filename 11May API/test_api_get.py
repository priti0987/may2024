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
    create_task_response = requests.put(ENDPOINT+ "/create-task", json=payload)
    assert create_task_response.status_code == 200
    data = create_task_response.json()
    print(data)
    task_id = data["task"]["task_id"]
    get_task_response = requests.get(ENDPOINT+ f"/get-task/{task_id}")
    assert get_task_response.status_code == 200
