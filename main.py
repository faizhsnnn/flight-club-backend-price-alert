from datetime import datetime, timedelta
import sys
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

print("\n=== Flight Club ===\n")

# ---------- HELPERS ----------

def clean_text(value: str) -> str:
    """Trim spaces and normalize casing for names/cities."""
    return value.strip().title()

def clean_email(value: str) -> str:
    return value.strip().lower()

# ---------- USER INPUT ----------

first_name = clean_text(input("First name: "))
last_name = clean_text(input("Last name: "))

if not first_name or not last_name:
    print("❌ Name fields cannot be empty.")
    sys.exit()

email_1 = clean_email(input("Email: "))
email_2 = clean_email(input("Confirm email: "))

if not email_1 or email_1 != email_2:
    print("❌ Emails do not match or are empty. Exiting.")
    sys.exit()

email = email_1

from_city = clean_text(input("From city: "))
to_city = clean_text(input("To city: "))

if not from_city or not to_city:
    print("❌ City names cannot be empty.")
    sys.exit()

try:
    target_price = int(input("Target price (GBP): ").strip())
    if target_price <= 0:
        raise ValueError
except ValueError:
    print("❌ Target price must be a positive number.")
    sys.exit()

# ---------- INIT SERVICES ----------

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# ---------- IATA CODES ----------

from_iata = flight_search.get_destination_code(from_city)
to_iata = flight_search.get_destination_code(to_city)

if not from_iata or not to_iata:
    print("❌ Could not resolve airport codes. Try again later.")
    sys.exit()

# ---------- FLIGHT SEARCH ----------

tomorrow = datetime.now() + timedelta(days=1)
return_date = tomorrow + timedelta(days=14)

flights = flight_search.check_flights(
    from_iata, to_iata, tomorrow, return_date, is_direct=True
)

cheapest = find_cheapest_flight(flights)

if cheapest.price == "N/A":
    flights = flight_search.check_flights(
        from_iata, to_iata, tomorrow, return_date, is_direct=False
    )
    cheapest = find_cheapest_flight(flights)

price_found = cheapest.price
email_sent = "NO"

# ---------- EMAIL ----------

if price_found != "N/A" and price_found <= target_price:
    email_body = (
        f"Hi {first_name},\n\n"
        f"A flight matching your target price was found.\n\n"
        f"Route: {from_city} -> {to_city}\n"
        f"Price: GBP {price_found}\n"
        f"Departure: {cheapest.out_date}\n"
        f"Return: {cheapest.return_date}\n"
        f"Stops: {cheapest.stops}\n"
    )

    try:
        notification_manager.send_email(email, email_body)
        email_sent = "YES"
    except Exception:
        email_sent = "FAILED"

# ---------- SAVE TO SINGLE SHEET ----------

data_manager.add_user_record({
    "firstName": first_name,
    "lastName": last_name,
    "email": email,
    "fromCity": from_city,
    "toCity": to_city,
    "targetPrice": target_price,
    "fromIata": from_iata,
    "toIata": to_iata,
    "priceFound": price_found,
    "emailSent": email_sent
})

print("\n✅ Process completed successfully.")
