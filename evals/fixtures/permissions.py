"""Local access-control fixture for investigating the gap beyond a green baseline."""


def can_read(user, document):
    return user["role"] == "admin" or user["id"] == document["owner_id"]
