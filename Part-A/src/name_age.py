"""Summary of the program's purpose.
    Calculate user's approximate birth year based on their name and age.

Input:
    Major input, including its type and source.
        input_name: str - User's name, entered via input prompt.
        input_age: int - User's age, entered via input prompt.

Process:
    Major processing step.
        birth_year = CURRENT_YEAR - input_age

Output:
    Major output, including its type and destination.
        birth_year: int - User's approximate birth year.

Typical usage example:
    Input prompt and original name-input example.
        What is your name? Alice

    Input prompt and original age-input example.
        What is your age? 30

    Resulting output from those inputs.
        Hello, Alice! You were born in approximately 1993.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    # get user's name as a string.
    input_name = input("What is your name? ")
    # get user's age as an integer.
    input_age = int(input("How old are you? "))
    # Calculate user's approximate birth year.
    # process data. Subtract user's age from current year to estimate birth year.
    birth_year = CURRENT_YEAR - input_age

    # Output personalized message with user's name and birth year.
    # output formatted results.
    print(f"Hello {input_name}! You were born in {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# References for sources used in the program.
# zyBooks. (n.d.). *Introduction to programming with Python*. Retrieved from https://learn.zybooks.com/zybook/IT140M2Spring2024
# Python Software Foundation. (n.d.). *Python Tutorial*. Retrieved from https://docs.python.org/3/tutorial/index.html
# W3Schools. (n.d.). *Python Tutorial*. Retrieved from https://www.w3schools.com/python/
