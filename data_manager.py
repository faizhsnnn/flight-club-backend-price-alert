import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

class DataManager:

    def __init__(self):
        self.endpoint = os.environ["SHEETY_ENDPOINT"]
        self.auth = HTTPBasicAuth(
            os.environ["SHEETY_USERNAME"],
            os.environ["SHEETY_PASSWORD"]
        )

    def add_user_record(self, record):
        payload = {"user": record}
        response = requests.post(
            self.endpoint,
            json=payload,
            auth=self.auth
        )
        response.raise_for_status()
