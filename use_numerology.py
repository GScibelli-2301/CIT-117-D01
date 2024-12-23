import re
from Numerology import Numerology

def is_valid_date(date_str):
    """Validates the date format mm-dd-yyyy."""
    return bool(re.match(r'^\d{2}[-/]\d{2}[-/]\d{4}$', date_str))

def main():
    # User Input
    name = input("Enter your full name: ").strip()
    while not name:
        name = input("Name cannot be empty. Please enter your full name: ").strip()

    dob = input("Enter your birthdate (mm-dd-yyyy): ").strip()
    while not is_valid_date(dob):
        dob = input("Invalid date format. Please enter your birthdate (mm-dd-yyyy): ").strip()

    # Numero object
    numerology = Numerology(name, dob)

    # Output numbers
    print("\nNumerology Reading:")
    print(f"Name: {numerology.getName()}")
    print(f"Birthdate: {numerology.getBirthdate()}")
    print(f"Life Path Number: {numerology.getLifePath()}")
    print(f"Birthday Number: {numerology.getBirthDay()}")
    print(f"Attitude Number: {numerology.getAttitude()}")
    print(f"Soul Number: {numerology.getSoul()}")
    print(f"Personality Number: {numerology.getPersonality()}")
    print(f"Power Name Number: {numerology.getPowerName()}")

if __name__ == "__main__":
    main()
