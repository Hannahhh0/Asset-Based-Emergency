##This code is a scrap worksheet, can edit and change to test or explore data

import pandas as pd

file = "dummy_data.xlsx"
sheet = "FPP 2026"

df = pd.read_excel(file, sheet_name=sheet)


df.columns = df.columns.str.strip()

print("\nTOTAL ROWS:", len(df))
print("\nCOLUMNS:\n")

for i, col in enumerate(df.columns):
    print(i, repr(col))

print("\nCALL NOTE COLUMNS ONLY:\n")
call_cols = [c for c in df.columns if "Call Notes" in str(c)]
for c in call_cols:
    print("-", repr(c))

print("\nUNNAMED COLUMNS:\n")
print([c for c in df.columns if "Unnamed" in str(c)])

print("\nFIRST ROW SAMPLE:\n")
print(df.head(1).to_dict())





<script type="module">
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/12.15.0/firebase-app.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  const firebaseConfig = {
    apiKey: "AIzaSyCTFi3yRm9DEoj9jqTPGX5tbVS2kxhbkiI",
    authDomain: "asset-based-emergency.firebaseapp.com",
    projectId: "asset-based-emergency",
    storageBucket: "asset-based-emergency.firebasestorage.app",
    messagingSenderId: "166630111593",
    appId: "1:166630111593:web:9f8942e7301ca552e565f8"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
</script>