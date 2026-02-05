class FlightData:
    def __init__(self, price, origin, destination, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin
        self.destination_airport = destination
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops


def find_cheapest_flight(data):
    if not data or not data.get("data"):
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    cheapest = data["data"][0]
    lowest = float(cheapest["price"]["grandTotal"])

    segments = cheapest["itineraries"][0]["segments"]
    best = FlightData(
        lowest,
        segments[0]["departure"]["iataCode"],
        segments[-1]["arrival"]["iataCode"],
        segments[0]["departure"]["at"].split("T")[0],
        cheapest["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0],
        len(segments) - 1
    )

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest:
            segments = flight["itineraries"][0]["segments"]
            best = FlightData(
                price,
                segments[0]["departure"]["iataCode"],
                segments[-1]["arrival"]["iataCode"],
                segments[0]["departure"]["at"].split("T")[0],
                flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0],
                len(segments) - 1
            )
            lowest = price

    return best
