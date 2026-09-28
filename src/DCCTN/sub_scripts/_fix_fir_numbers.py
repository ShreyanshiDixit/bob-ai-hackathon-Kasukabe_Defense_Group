"""
One-shot utility: assigns unique random FIR numbers to mock_firs.json.
Format: NNNN/YYYY  (zero-padded 4-digit sequential number, shuffled for randomness)
A backup is saved as mock_firs.json.bak before writing.
"""
import json
import random
import shutil
from collections import Counter
from pathlib import Path

JSON_FILE = Path(__file__).resolve().parent.parent / "data" / "mock_firs.json"

with open(JSON_FILE, "r", encoding="utf-8") as f:
    firs = json.load(f)

print(f"Loaded {len(firs)} FIRs")

# Report duplicates before fix
fir_nums_before = [fir.get("fir_number") for fir in firs]
dupes_before = {k: v for k, v in Counter(fir_nums_before).items() if v > 1}
print(f"Duplicate fir_numbers before fix: {len(dupes_before)}")

# Build a shuffled pool of sequential numbers (1 … N)
pool = list(range(1, len(firs) + 1))
random.shuffle(pool)

for i, fir in enumerate(firs):
    # Preserve year from original fir_number, default to 2026
    existing = fir.get("fir_number", "")
    year = existing.split("/")[-1].strip() if "/" in existing else "2026"
    fir["fir_number"] = f"{pool[i]:04d}/{year}"

# Verify uniqueness
fir_nums_after = [fir["fir_number"] for fir in firs]
dupes_after = {k: v for k, v in Counter(fir_nums_after).items() if v > 1}
assert len(dupes_after) == 0, f"Still have duplicates: {dupes_after}"

# Backup then write
shutil.copy(JSON_FILE, JSON_FILE.with_suffix(".json.bak"))
print(f"Backup saved to {JSON_FILE.with_suffix('.json.bak')}")

with open(JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(firs, f, indent=2, ensure_ascii=False)

print(f"Done. {len(firs)} FIRs now have unique fir_numbers.")
print(f"Sample: {fir_nums_after[:5]}")
