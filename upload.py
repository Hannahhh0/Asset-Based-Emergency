#this code will be used for uploading spreadsheet data into firestore

import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import re


##firebase setup
if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()



##Excel Sheet Loaded
df = pd.read_excel(
    "dummy_data.xlsx",
    sheet_name="FPP 2026"
)
df.columns = df.columns.str.strip()

print(f"Loaded {len(df)} rows")


print(df.columns.tolist())

##Helper functions
def to_bool(value):
    if str(value).strip().lower() in ["yes", "true", "y"]:
        return True
    if str(value).strip().lower() in ["no", "false", "n"]:
        return False
    return None

def parse_geocode(value):
    try:
        lng, lat = value.split(",")
        return float(lat.strip()), float(lng.strip())
    except:
        return None, None

def parse_paired(value):
    if not value or str(value).strip() == "":
        return {
            "paired": False,
            "partner": None
        }

    text = str(value).strip()

    if text[0].lower() == "y":
        match = re.search(r"\[(.*?)\]", text)

        partner = match.group(1).strip() if match else None

        return {
            "paired": True,
            "pairedWith": partner
        }

    return {
        "paired": False,
        "pairedWith": None
    }



##Upload loop (creates collections, documents, and fields)
for _, row in df.iterrows():

    participant_id = str(row["Unique Identifier"]).strip()

    lat, lng = parse_geocode(row["GeoCode"])

    paired_data = parse_paired(row["Paired?"])

    doc_ref = db.collection("participants").document(participant_id)

    data = {
        "groupAssignment": row["Group Assignment"],
        "name": str(row["Name"]).strip(),

        "contact": {
            "primaryPhone": row["Phone Number (xxx-xxx-xxxx)"],
            "alternatePhone": row["Phone Details or Alternative Phone #"],
            "email": row["Email Address"],
            "textsPreferred": to_bool(row["Texts Preferred?"]),
            "canReceiveTexts": to_bool(row["Able to Receive Texts?"])
        },

       "status": {
            "paired": paired_data["paired"],
            "pairedWith": paired_data["pairedWith"],
            "annualSurveyComplete": to_bool(row["Annual Re-enrollment Survey Complete?"])
        },

        "household": {
            "size": row["Household size"],
            "bags": row["# of Bags"]
        },

        "address": {
            "fullAddress": row["Address"],
            "street": row["Street"],
            "city": row["City"],
            "state": row["State/Region"],
            "postalCode": row["Postal"],
            "country": row["Country"]
        },

        "location": {
            "latitude": lat,
            "longitude": lng,
            "distanceFromFFS": row["GeoCode Distance From FFS"],
            "driveTimeMinutes": row["GeoCodeDriveTimefromFFS"]
        },

        "delivery": {
            "lockedBuilding": to_bool(row["Locked building?"]),
            "driverNotes": row["Notes for Drivers (Route Info)"]
        },

        "demographics": {
            "preferredLanguage": row["Preferred Language"],
            "pronouns": row["Pronouns$"],
            "raceEthnicity": row["Race/ Ethnicity$"]
        },

        "medical": {
            "medicalConsent": to_bool(row["Consent to Access Medical Record, if Necessary?"])
        },

        "notes": {
            "teamNotes": row["Notes to FPP Team"]
        },

        "metadata": {
            "geocodedDate": row["GeoCoded Date"]
        }
    }

    doc_ref.set(data)

print("Upload complete")

##To do: add subcollection, either in loop or separate (need to look up) 