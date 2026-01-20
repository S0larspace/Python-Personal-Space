students = {
    "Alice": {"id": "ID0001", "age": 26, "grade": "A"},
    "Ben": {"id": "ID0002", "age": 24, "grade": "B"},
    "Charles": {"id": "ID0003", "age": 22, "grade": "B+"}
}

print(students["Ben"]["age"])  # printing the data within nested dictionaries

# Note that dictionaries cannot handle duplicate keys, assigning the same key will override the existing data paired with the same key.
