data = {
    "company": {
        "name": "Acme Corp",
        "departments": [
            {
                "name": "Engineering",
                "employees": [
                    {"name": "Alice", "id": 1},
                    {"name": "Bob", "id": 2}
                ]
            },
            {
                "name": "HR",
                "employees": [
                    {"name": "Carol", "id": 3}
                ]
            }
        ]
    },
    "meta": {"created": "2025-12-06"}
}

for department in data["company"]["departments"]:
    print(f"Department: {department['name']}")
    for employee in department["employees"]:
        print(f" - Employee Name: {employee['name']}, ID: {employee['id']}")


nestedData = {
    "company": {
        "name": "Acme Corp",
        "departments": [
            {
                "name": "Engineering",
                "employees": [
                    {"name": "Alice", "id": 1},
                    {"name": "Bob", "id": 2}
                ]
            },
            {
                "name": "HR",
                "employees": [
                    {"name": "Carol", "id": 3}
                ]
            }
        ]
    },
    "meta": {"created": "2025-12-06"}
}