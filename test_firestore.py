import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

db.collection("test").document("connection").set({
    "status": "working"
})

print("Success — Firestore is connected!")