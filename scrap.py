import pandas as pd

file = "dummy_data.xlsx"

xls = pd.ExcelFile(file)

for sheet in xls.sheet_names:
    print("\nSHEET:", sheet)

    df = pd.read_excel(file, sheet_name=sheet)

    print(df.head())