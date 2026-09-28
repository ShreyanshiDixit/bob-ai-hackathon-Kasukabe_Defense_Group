import json
import sys
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


# ----------------------------
# Paths
# ----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

JSON_FILE = BASE_DIR / "data" / "mock_firs.json"
CHROMA_DIR = BASE_DIR / "database" / "chroma"

# ----------------------------
# Guard: JSON file must exist
# ----------------------------

if not JSON_FILE.exists():
    print(f"ERROR: JSON file not found at {JSON_FILE}")
    print("Please place mock_firs.json in the DCCTN/data/ directory.")
    sys.exit(1)

# ----------------------------
# Load FIRs
# ----------------------------

with open(JSON_FILE, "r", encoding="utf-8") as f:
    firs = json.load(f)

if not isinstance(firs, list) or len(firs) == 0:
    print("ERROR: mock_firs.json must contain a non-empty JSON array.")
    sys.exit(1)

print(f"Loaded {len(firs)} FIRs")

# ----------------------------
# Embedding Model
# ----------------------------

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# ----------------------------
# Chroma — ensure directory exists
# ----------------------------

CHROMA_DIR.mkdir(parents=True, exist_ok=True)

client = chromadb.PersistentClient(path=str(CHROMA_DIR))

# Delete existing collection so re-runs don't hit duplicate-ID errors
try:
    client.delete_collection(name="firs")
except Exception:
    pass

collection = client.get_or_create_collection(name="firs")

# ----------------------------
# Build batches then insert
# ----------------------------

batch_ids = []
batch_documents = []
batch_embeddings = []
batch_metadatas = []

for fir in firs:
    case_id = str(fir.get("case_id", ""))
    if not case_id:
        print(f"WARNING: FIR missing case_id, skipping: {fir}")
        continue

    document = (
        f"FIR Number: {fir.get('fir_number')}\n\n"
        f"Crime Category: {fir.get('crime_category')}\n"
        f"Crime Type: {fir.get('crime_type')}\n\n"
        f"District: {fir.get('district')}\n"
        f"State: {fir.get('state')}\n"
        f"Police Station: {fir.get('police_station')}\n\n"
        f"Summary:\n{fir.get('crime_summary')}\n\n"
        f"FIR:\n{fir.get('detailed_full_fir_text')}\n\n"
        f"Keywords:\n{' '.join(fir.get('keywords', []))}"
    )

    embedding = model.encode(document, convert_to_numpy=True).tolist()

    metadata = {
        "fir_number":      str(fir.get("fir_number", "")),
        "crime_type":      str(fir.get("crime_type", "")),
        "crime_category":  str(fir.get("crime_category", "")),
        "district":        str(fir.get("district", "")),
        "state":           str(fir.get("state", "")),
        "status":          str(fir.get("status", "")),
    }

    batch_ids.append(case_id)
    batch_documents.append(document)
    batch_embeddings.append(embedding)
    batch_metadatas.append(metadata)

# ----------------------------
# Insert in one batch call
# ----------------------------

if batch_ids:
    collection.add(
        ids=batch_ids,
        documents=batch_documents,
        embeddings=batch_embeddings,
        metadatas=batch_metadatas,
    )
    print(f"Successfully inserted {len(batch_ids)} FIRs into ChromaDB at {CHROMA_DIR}")
else:
    print("No valid FIRs to insert.")
