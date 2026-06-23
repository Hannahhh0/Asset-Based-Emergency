##DON'T RUN

import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

participants = db.collection("participants").stream()

for p in participants:
    calls_ref = db.collection("participants").document(p.id).collection("calls")
    calls = calls_ref.stream()

    for c in calls:
        c.reference.delete()

print("All call histories deleted")