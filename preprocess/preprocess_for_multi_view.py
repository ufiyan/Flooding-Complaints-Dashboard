import pandas as pd
import os

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    raw_csv = os.path.join(root, "Flooding_Complaints_to_311_20250128.csv")
    out_dir = os.path.join(root, "data")
    os.makedirs(out_dir, exist_ok=True)

    # Load and clean
    df = pd.read_csv(raw_csv, low_memory=False)
    df["CREATED_DATE"] = pd.to_datetime(df["CREATED_DATE"], errors="coerce")
    df = df.dropna(subset=["CREATED_DATE"])

    df.columns = df.columns.str.strip().str.upper().str.replace(" ", "_", regex=False)
    df["YEAR"] = df["CREATED_DATE"].dt.year
    df["MONTH_NUM"] = df["CREATED_DATE"].dt.month
    df["MONTH"] = df["CREATED_DATE"].dt.strftime("%B")

    max_year = df["YEAR"].max()
    df = df[df["YEAR"] >= (max_year - 4)]

    # Process ZIP codes: top 10
    df["INCIDENT_ZIP"] = df["ZIP_CODE"].astype(str).str.extract(r"(\d{5})")[0]
    df = df.dropna(subset=["INCIDENT_ZIP"])

    top_zips = df["INCIDENT_ZIP"].value_counts().nlargest(10).index.tolist()
    df["INCIDENT_ZIP"] = df["INCIDENT_ZIP"].where(df["INCIDENT_ZIP"].isin(top_zips), "Other")

    # Process Boroughs: top 15
    df.rename(columns={"SR_TYPE": "COMPLAINT_TYPE", "COMMUNITY_AREA": "BOROUGH"}, inplace=True)
    top_boroughs = df["BOROUGH"].value_counts().nlargest(15).index.tolist()
    df["BOROUGH"] = df["BOROUGH"].where(df["BOROUGH"].isin(top_boroughs), "Other")

    # Save filtered flooding_complaints_preprocessed.json
    df_out = df[["YEAR", "MONTH", "MONTH_NUM", "BOROUGH", "INCIDENT_ZIP", "COMPLAINT_TYPE"]]
    df_out.to_json(os.path.join(out_dir, "flooding_complaints_preprocessed.json"), orient="records", indent=2)

    print(f"✅ Preprocessing complete: {len(df_out)} rows saved.")

if __name__ == "__main__":
    main()