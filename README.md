# Flight Club – Backend Flight Price Alert System

## Overview

Flight Club is a production-style Python backend automation system that tracks flight prices between user-defined routes and sends automated email alerts when prices fall below a specified threshold.

This project was built as part of my **#90DaysOfCode** challenge with an emphasis on real-world backend concerns such as input validation, API reliability, fallback logic, data persistence, and secure configuration management.

The goal was to design a system that behaves predictably under real conditions rather than a tutorial-style implementation.

---

## Key Capabilities

- Structured user input validation and normalization
- Dynamic IATA airport code resolution
- Live flight search using Amadeus APIs
- Direct-flight prioritization with indirect fallback handling
- Cheapest-flight detection with stop count analysis
- Automated email notifications using SMTP
- Centralized data storage using Sheety
- Environment-based credential management
- Modular, maintainable Python architecture

---

## Project Structure
```
flight-club-backend-price-alert/
│
├── main.py
│ └── Application orchestration and user workflow
│
├── flight_search.py
│ └── API authentication and flight search logic
│
├── flight_data.py
│ └── Flight data modeling and price comparison
│
├── data_manager.py
│ └── Persistent storage via Sheety API
│
├── notification_manager.py
│ └── Email notification service
│
└── README.md
```


---

## Workflow Summary

1. User submits personal details, route, and target price.
2. Inputs are validated and normalized.
3. IATA airport codes are resolved dynamically.
4. Flight prices are queried using live APIs.
5. Direct routes are evaluated first, followed by indirect routes if required.
6. The cheapest valid option is selected.
7. If pricing conditions are met, an automated email alert is sent.
8. User data and results are stored for tracking and auditing.

---

## Running the Project

### Clone
```
git clone https://github.com/faizhsnnn/flight-club-backend-price-alert.git
cd flight-club-backend-price-alert
```
### Install Dependencies
```
pip install requests python-dotenv
```

### Environment Variables
```
AMADEUS_API_KEY=your_key
AMADEUS_API_SECRET=your_secret

SHEETY_ENDPOINT=your_endpoint
SHEETY_USERNAME=your_username
SHEETY_PASSWORD=your_password

MY_EMAIL=your_email
MY_EMAIL_PASSWORD=your_app_password
EMAIL_PROVIDER_SMTP_ADDRESS=smtp.provider.com
EMAIL_PROVIDER_SMTP_PORT=587
```

### Run
```
python main.py
```

### Engineering Concepts Demonstrated

Backend automation design

Defensive input validation

API authentication and retry handling

Fallback strategies for unreliable data sources

Modular Python architecture

Secure credential handling

Email notification pipelines

---
### Author

Faiz Hasan

Python Automation & Backend Developer

