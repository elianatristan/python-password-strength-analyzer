def has_number(password):
    for character in password:
        if character.isdigit():
            return True
    return False

def has_uppercase(password):
    for character in password:
        if character.isupper():
            return True
    return False

def calculate_score(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if has_number(password):
        score += 1

    if has_uppercase(password):
        score += 1

    return score

password = input("Enter a password: ")

score = calculate_score(password)

print("\nPassword Analysis")

if score == 3:
    print("Strong Password")
elif score == 2:
    print("Moderate Password")
else:
    print("Weak Password")
