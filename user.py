import allure
import requests

from generator import Generator
from urls import Urls


class User:
    @allure.step('New user registration with data list return')
    def create_new_user(self):
        login_pass = []

        email = Generator.generate_rdm_str(5) + "@yandex.ru"
        password = Generator.generate_rdm_str(7)
        name = "User_" + Generator.generate_rdm_str(5)

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post(Urls.register_url, data=payload)

        if response.status_code == 200:
            login_pass.append(email)
            login_pass.append(password)
            login_pass.append(name)
            login_pass.append(response.json()['accessToken'])

        return login_pass

    @allure.step('Deleting a user')
    def delete_user(self, user_token):
        headers = {
            'Authorization': user_token,
            'Accept': '*/*'
        }

        requests.delete(Urls.edit_del_url, headers=headers)
