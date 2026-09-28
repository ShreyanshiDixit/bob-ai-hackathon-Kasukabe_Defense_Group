import json
import sqlite3
from pathlib import Path

# --------------------------------------------------
# PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "database" / "firs.db"
JSON_PATH = BASE_DIR / "data" / "mock_firs.json"

# --------------------------------------------------
# CREATE DATABASE FOLDER IF NEEDED
# --------------------------------------------------

DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# CONNECT SQLITE
# --------------------------------------------------

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# --------------------------------------------------
# CREATE TABLE IF NOT EXISTS
# --------------------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS firs (

    fir_number TEXT PRIMARY KEY,

    case_id INTEGER,
    status TEXT,

    case_registration_date TEXT,
    incident_occurrence_date TEXT,

    reporting_officer TEXT,

    police_station TEXT,
    station_number TEXT,
    district TEXT,
    state TEXT,

    crime_category TEXT,
    crime_type TEXT,

    complainant_name TEXT,
    complainant_age INTEGER,
    complainant_gender TEXT,

    victim_name TEXT,
    victim_age INTEGER,
    victim_gender TEXT,

    accused_names TEXT,
    suspect_phone_numbers TEXT,

    place_of_incident TEXT,

    loss_amount REAL,

    crime_summary TEXT,

    detailed_full_fir_text TEXT,

    keywords TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

print("✓ Table verified")

# --------------------------------------------------
# LOAD JSON
# --------------------------------------------------

with open(JSON_PATH, "r", encoding="utf-8") as f:
    firs = json.load(f)

print(f"✓ Loaded {len(firs)} FIRs")

# --------------------------------------------------
# INSERT FIRS
# --------------------------------------------------

inserted = 0
skipped = 0

for fir in firs:

    fir_number = fir.get("fir_number")

    cursor.execute(
        "SELECT fir_number FROM firs WHERE fir_number = ?",
        (fir_number,)
    )

    exists = cursor.fetchone()

    if exists:
        skipped += 1
        continue

    cursor.execute("""
    INSERT INTO firs (

        fir_number,
        case_id,
        status,

        case_registration_date,
        incident_occurrence_date,

        reporting_officer,

        police_station,
        station_number,
        district,
        state,

        crime_category,
        crime_type,

        complainant_name,
        complainant_age,
        complainant_gender,

        victim_name,
        victim_age,
        victim_gender,

        accused_names,
        suspect_phone_numbers,

        place_of_incident,

        loss_amount,

        crime_summary,

        detailed_full_fir_text,

        keywords

    )
    VALUES (
        ?,?,?,?,?,?,
        ?,?,?,?,
        ?,?,
        ?,?,?,
        ?,?,?,
        ?,?,
        ?,
        ?,
        ?,
        ?,
        ?
    )
    """, (

        fir.get("fir_number"),
        fir.get("case_id"),
        fir.get("status"),

        fir.get("case_registration_date"),
        fir.get("incident_occurrence_date"),

        fir.get("reporting_officer"),

        fir.get("police_station"),
        fir.get("station_number"),
        fir.get("district"),
        fir.get("state"),

        fir.get("crime_category"),
        fir.get("crime_type"),

        fir.get("complainant_name"),
        fir.get("complainant_age"),
        fir.get("complainant_gender"),

        fir.get("victim_name"),
        fir.get("victim_age"),
        fir.get("victim_gender"),

        json.dumps(fir.get("accused_names", [])),
        json.dumps(fir.get("suspect_phone_numbers", [])),

        fir.get("place_of_incident"),

        fir.get("loss_amount"),

        fir.get("crime_summary"),

        fir.get("detailed_full_fir_text"),

        json.dumps(fir.get("keywords", []))
    ))

    inserted += 1

conn.commit()

print(f"✓ Inserted: {inserted}")
print(f"✓ Skipped : {skipped}")

# --------------------------------------------------
# VERIFY
# --------------------------------------------------

cursor.execute("SELECT COUNT(*) FROM firs")
total = cursor.fetchone()[0]

print(f"✓ Total FIRs in DB: {total}")

conn.close()