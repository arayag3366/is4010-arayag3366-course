from typing import Iterable, Dict, List, Optional

users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False}
]

def calculate_average_age(users: Iterable[Dict]) -> float:
    """
    Calculate the average age of users with valid integer ages.

    Parameters
    ----------
    users : Iterable[dict]
        An iterable of user dictionaries. Each dictionary may contain
        an "age" key whose value is expected to be an integer.

    Returns
    -------
    float
        The average age of users with valid integer ages.

    Raises
    ------
    ValueError
        If no users contain a valid integer age.
    """
    valid_ages = [user["age"] for user in users if isinstance(user.get("age"), int)]

    try:
        return sum(valid_ages) / len(valid_ages)
    except ZeroDivisionError:
        print("No users were found!")
        return 0


def get_active_user_emails(users: Iterable[Dict]) -> List[str]:
    """
    Retrieve email addresses of active users.

    Parameters
    ----------
    users : Iterable[dict]
        An iterable of user dictionaries. Each dictionary may contain
        "is_active" (bool) and "email" (str) keys.

    Returns
    -------
    list of str
        A list containing the email addresses of users who are marked
        as active and have a non-empty email value.
    """

    active_emails = []

    try:
        for user in users:
            is_active = user["is_active"]

            if is_active:
                try:
                    email = user["email"]
                except KeyError:
                    print(f"Error: user {user} is missing 'email' key.")
                    return []

                if email:
                    active_emails.append(email)

        return active_emails

    except KeyError:
        print("Error: user dictionary is missing 'is_active' key.")
        return []


if __name__ == "__main__":
    average_age = calculate_average_age(users)
    active_emails = get_active_user_emails(users)

    print(f"Average user age: {average_age:.2f}")
    print(f"Active user emails: {active_emails}")