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





