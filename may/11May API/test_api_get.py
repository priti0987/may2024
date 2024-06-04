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
    payload = task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    data = create_task_response.json()
    # print(data)
    task_id = data["task"]["task_id"]
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"]==payload["content"]
    assert get_task_data["user_id"]==payload["user_id"]

def test_can_update_task():
    payload = task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]
    new_payload_update = {
        "user_id":payload["user_id"],
        "task_id":task_id,
        "content": "updated",
        "is_done": True
    }
    update_task_response = update_task(new_payload_update)
    assert update_task_response.status_code == 200

    get_task_response1 = get_task(task_id)
    get_task_data1 = get_task_response1.json()
    assert get_task_data1["content"]== new_payload_update["content"]
    assert get_task_data1["is_done"]== new_payload_update["is_done"]

def test_can_list_tasks():
    pass
def update_task(payload):
    return requests.put(ENDPOINT+ "/update-task",json=payload)

def create_task(payload):
    return requests.put(ENDPOINT+ "/create-task", json=payload)

def get_task(task_id):
    return requests.get(ENDPOINT+ f"/get-task/{task_id}")

def task_payload():
    return {
        "content": "testing",
        "user_id": "testsuite",
        "task_id": "stateside",
        "is_done": False
    }
