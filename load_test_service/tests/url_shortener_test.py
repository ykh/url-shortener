import random
from http import HTTPStatus

import httpx
import requests.exceptions
from locust import between, HttpUser, task


class ShortenUrlUser(HttpUser):
    wait_time = between(0.01, 0.02)

    created_short_urls = []
    token = None

    def on_start(self):
        self.token = self.get_jwt_token()

    def get_jwt_token(self):
        if self.token:
            return self.token

        url = f"{self.host}/api/users/token"

        payload = {
            "username": "test",
            "password": "secret"
        }

        response = httpx.post(
            url=url,
            data=payload,
        )

        if response.status_code == HTTPStatus.OK:
            token = response.json().get("access_token")

            if token is None:
                raise ValueError("Couldn't get access-token.")
        else:
            raise ValueError("Couldn't get access-token.")

        self.token = token

        return token

    @task(1)
    def shorten_url(self):
        payload = {"url": "https://google.com/"}

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"{self.token}"
        }

        with self.client.post(
                "/api/shorten",
                json=payload,
                headers=headers,
                name="shorten_url",
                catch_response=True,
        ) as response:
            if response.status_code in (HTTPStatus.OK, HTTPStatus.CREATED):
                response.success()
            else:
                response.failure(
                    f"Unexpected status code: {response.status_code}"
                )

            try:
                short_url = response.json().get("short_url")
            except requests.exceptions.JSONDecodeError as error:
                raise error

            if short_url is None:
                response.failure(f"Key 'short_url' didn't exist.")
            else:
                self.created_short_urls.append(short_url)

    @task(10)
    def get_url(self):
        if not self.created_short_urls:
            return

        short_url = random.choice(self.created_short_urls)

        headers = {
            "Authorization": f"{self.token}"
        }

        with self.client.get(
                f"/api/redirect?url={short_url}",
                name="get_url",
                headers=headers,
                catch_response=True,
        ) as response:
            if response.status_code in (200, 201):
                response.success()
            else:
                response.failure(
                    f"Unexpected status code: {response.status_code}"
                )
