import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:

    def __init__(self):
        self.token = self._get_token()

    def _get_token(self):
        r = requests.post(
            TOKEN_ENDPOINT,
            data={
                "grant_type": "client_credentials",
                "client_id": os.environ["AMADEUS_API_KEY"],
                "client_secret": os.environ["AMADEUS_API_SECRET"],
            }
        )
        return r.json().get("access_token")

    def get_destination_code(self, city):
        headers = {"Authorization": f"Bearer {self.token}"}
        params = {"keyword": city, "max": 1}

        for _ in range(2):
            r = requests.get(IATA_ENDPOINT, headers=headers, params=params)
            if r.status_code == 200:
                data = r.json()
                if "data" in data and data["data"]:
                    return data["data"][0]["iataCode"]
            time.sleep(1)

        return None

    def check_flights(self, origin, destination, from_time, to_time, is_direct=True):
        headers = {"Authorization": f"Bearer {self.token}"}
        params = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": 10,
        }

        try:
            r = requests.get(FLIGHT_ENDPOINT, headers=headers, params=params)
            if r.status_code == 200:
                return r.json()
        except requests.RequestException:
            pass

        return None
