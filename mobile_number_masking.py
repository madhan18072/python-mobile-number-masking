def mask_mobile_number(mobile):

    if mobile.isdigit() and len(mobile) == 10:
        mobile_number = mobile[:5]
        masked = mobile_number.ljust(10, '*')
        return masked

    else:
      return None


mobile = input("Enter Mobile Number: ")

result = mask_mobile_number(mobile)

if result is None:
    print("Invalid mobile number. Enter exactly 10 digits.")
else:
    print(f"Masked Mobile Number: {result}")

