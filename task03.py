import string

def check_password_strength(password):
    # Criteria weights
    length_weight = 2
    uppercase_weight = 2
    lowercase_weight = 2
    digit_weight = 2
    special_char_weight = 3

    # Initialize scores
    length_score = len(password) * length_weight
    uppercase_score = sum(1 for c in password if c.isupper()) * uppercase_weight
    lowercase_score = sum(1 for c in password if c.islower()) * lowercase_weight
    digit_score = sum(1 for c in password if c.isdigit()) * digit_weight
    special_char_score = sum(1 for c in password if c in string.punctuation) * special_char_weight

    # Calculate total score
    total_score = length_score + uppercase_score + lowercase_score + digit_score + special_char_score

    # Determine strength level based on total score
    if total_score >= 100:
        strength = "Very Strong"
    elif total_score >= 80:
        strength = "Strong"
    elif total_score >= 60:
        strength = "Moderate"
    elif total_score >= 40:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return total_score, strength

if __name__ == "__main__":
    password = input("Enter a password to assess its strength: ")
    score, strength = check_password_strength(password)
    print(f"Password Strength: {strength}")
    print(f"Total Score: {score}")
