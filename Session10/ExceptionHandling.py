#Below is a code that reveals your exact age once you input your birthday

from datetime import datetime

# Custom Exceptions
class InvalidDateFormatError(Exception):
    pass

class FutureDateError(Exception):
    pass

class UnrealisticAgeError(Exception):
    pass

def calculate_age(birthday_str):
    try:
        birthday = datetime.strptime(birthday_str, "%Y-%m-%d")
    except ValueError:
        raise InvalidDateFormatError("Invalid date format. Please use YYYY-MM-DD.")

    today = datetime.today()

    if birthday > today:
        raise FutureDateError("You entered a date in the future.")

    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

    if age > 130:
        raise UnrealisticAgeError("Age exceeds realistic human lifespan.")

    return age

# Example Usage
if __name__ == "__main__":
    user_input = input("Enter your birthday (YYYY-MM-DD): ")

    try:
        age = calculate_age(user_input)
        print(f"You are {age} years old.")
    except (InvalidDateFormatError, FutureDateError, UnrealisticAgeError) as e:
        print(f"Error: {e}")
