import requests
import config


request_url = config.get_request_url()
headers = {
    "Authorization": f"Bearar {config.get_access_token()}"
}


def ask_data() -> dict[str, str]:
    url = input("Enter name: ")
    email = input("Enter email: ")
    gender = input("Enter gender as 'male' or 'female' without spaces: ")
    status = input("Enter status as 'active' or 'inactive' without spaces: ")
    gender = "male" if gender.lower() == "male" else "female"
    status = "active" if gender.lower() == "active" else "inactive"
    return {
        "url": url,
        "email": email,
        "gender": gender,
        "status": status,
    }


def brain() -> None:
    response = requests.post(url= request_url, data= ask_data(), headers= headers)
    print(f"Post method: {response.json()}")


brain()
