# Python Practice File
# We'll use this file to run and test things during the lesson

# ── LISTS ──────────────────────────────────────────────────────────────────────
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words = ["apple", "banana", "cherry", "date", "elderberry"]

# ── DICTIONARIES ───────────────────────────────────────────────────────────────
user = {
    "name": "Clay",
    "role": "developer",
    "active": True,
    "score": 42,
}

users = [
    {"name": "Clay",  "role": "developer", "score": 42},
    {"name": "Sarah", "role": "admin",     "score": 88},
    {"name": "Mike",  "role": "tester",    "score": 31},
    {"name": "Jones", "role": "developer", "score": 75},
]

# ── NESTED DICT ────────────────────────────────────────────────────────────────
server = {
    "name": "prod-1",
    "location": "us-east",
    "specs": {
        "cpu": 8,
        "ram": 32,
        "disk": 500,
    },
    "status": "running",
}
