def main():
    # Step 1: Prompt for First and Last Name
    sName = input("Enter your First and Last name: ")
    
    # Step 4: Extract initials
    names = sName.split()
    sInitials = names[0][0].upper() + names[1][0].upper()

    while True:
        # Step 3: Prompt for desired password
        sPassword = input("Enter your desired password: ")

        # Step 5: Check length
        if not (8 <= len(sPassword) <= 12):
            print("Password must be between 8 and 12 characters.")
            continue

        # Step 6: Check if password starts with "Pass" or "pass"
        if sPassword.lower().startswith("pass"):
            print("Password can't start with Pass.")
            continue

        # Step 7: Check for at least 1 uppercase letter
        if not any(c.isupper() for c in sPassword):
            print("Password must contain at least 1 uppercase letter.")
            continue

        # Step 8: Check for at least 1 lowercase letter
        if not any(c.islower() for c in sPassword):
            print("Password must contain at least 1 lowercase letter.")
            continue

        # Step 9: Check for at least 1 number
        if not any(c.isdigit() for c in sPassword):
            print("Password must contain at least 1 number.")
            continue

        # Step 10: Check for special characters
        special_chars = "!@#$%^"
        if not any(c in special_chars for c in sPassword):
            print("Password must contain at least 1 of these special characters: ! @ # $ % ^")
            continue

        # Step 11: Check for initials
        if sInitials.lower() in sPassword.lower():
            print("Password must not contain user initials.")
            continue

        # Step 12: Check for duplicate characters
        char_count = {}
        duplicate_chars = []
        for c in sPassword:
            char_lower = c.lower()
            char_count[char_lower] = char_count.get(char_lower, 0) + 1
            if char_count[char_lower] == 2:
                duplicate_chars.append(char_lower)

        if duplicate_chars:
            print("These characters appear more than once:")
            for char in duplicate_chars:
                print(f"{char}: {char_count[char]}")
            continue

        # Step 13: If all checks pass
        print("Password is valid and OK to use.")
        break

if __name__ == "__main__":
    main()
