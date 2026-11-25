username = input("Enter your username: ")
email = input("Enter your email: ").strip().lower()
age_input = input("Enter your age: ").strip()
age = int(age_input) if age_input.isdecimal() else None
password = input("Enter your password: ")

def data_validation(user = username, mail = email, user_age = age, user_password = password):
    summary = ""
    if user == "":
        summary += "Username cannot be empty.\n"
    if " " in user:
        summary += "Username cannot contain spaces.\n"
    if len(user) < 5:
        summary += "Username must be at least 5 characters long.\n"
    if user and user[0].isdigit():
        summary += "Username cannot start with a digit.\n"

    if mail.count("@") != 1:
        summary += "Email must contain exactly one '@' symbol.\n"

    if user_age is None:
        summary += "Age must contain only digits.\n"
    elif user_age < 16:
        summary += "Age must be at least 16.\n"

    if user_password == "":
        summary += "Password cannot be empty.\n"
    if " " in user_password:
        summary += "Password cannot contain spaces.\n"
    if len(user_password) < 8:
        summary += "Password must be at least 8 characters long.\n"
    if len(set(user_password)) == 1:
        summary += "Password cannot consist of the same character.\n"

    if summary != "":
        return "Invalid inputs found:\n" + summary
    return "All inputs are valid."

print(data_validation())