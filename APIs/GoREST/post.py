import requests
import config


request_url = config.get_request_url()
headers = config.get_headers()


def ask_data() -> dict[str, str]:
    name = input("Enter name: ")
    email = input("Enter email: ")
    gender = input("Enter gender as 'male' or 'female' without spaces: ")
    status = input("Enter status as 'active' or 'inactive' without spaces: ")
    gender = "male" if gender.lower() == "male" else "female"
    status = "active" if gender.lower() == "active" else "inactive"
    return {
        "name": name,
        "email": email,
        "gender": gender,
        "status": status
    }


def brain() -> None:
    response = requests.post(url= request_url, data= ask_data(), headers= headers)
    print(f"Post method: {response.json()}")


brain()
# Post method: {'id': 7812403, 'name': "No'El Tercero", 'email': 'noel@gmail.com', 'gender': 'male', 'status': 'inactive'}
# Post method: {'id': 7812488, 'name': "No'Elle Tercero", 'email': 'noelle@gmail.com', 'gender': 'female', 'status': 'inactive'}
# Post method: {'id': 7812543, 'name': 'Ella Bella', 'email': 'ella@bella.com', 'gender': 'female', 'status': 'inactive'}
