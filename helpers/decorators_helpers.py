
def is_email_valid(func):
    def wrapper(email, y, a, z, b, c):
        if "@" in email:
            if "." in email.split("@")[1]:
                func(email, y, a, z, b, c)
            else:
                print("Email invalid without dot!!!!")
        else:
            print("Email invalid without @ !!!!")
    return wrapper


def is_phone_valid(func):
    def wrapper(email, y, a, phone, b, c):
        if phone[0] == '+':
            if len(phone) == 13:
                func(email, y, a, phone, b, c)
            else:
                print("Invalid len phone!!!!")
        else:
            print("Invalid format phone !!!!")
    return wrapper
