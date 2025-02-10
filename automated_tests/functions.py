import requests
import string

from typing import Any

def login_user(email: string,
               password: string) -> Any:
    data = {
        "email": email,
        "password": password
    }
    response = requests.post("https://playground.learnqa.ru/api/user/login",
                             data=data)
    return response

def create_user(username: string,
                first_name: string,
                last_name: string,
                email: string,
                password: string) -> Any:
    data = {
        "username": username,
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "password": password
    }
    response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
    return response

def auth_user() -> Any:
    response = requests.get("https://playground.learnqa.ru/api/user/auth")
    return response

def get_user() -> Any:
    response = requests.get("https://playground.learnqa.ru/api/user/{id}")
    return response

def update_user(username: string,
                first_name: string,
                last_name: string,
                email: string,
                password: string) -> Any:
    data = {
        "username": username,
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "password": password
    }
    response = requests.put("https://playground.learnqa.ru/api/user/{id}", data=data)
    return response

def delete_user() -> Any:
    response = requests.delete("https://playground.learnqa.ru/api/user/{id}")
    return response