from datetime import datetime, date


def validate_c(validate_ssn: str) -> bool:
    ssn_digits = [int(digit) for digit in validate_ssn]
    special_number = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    control_digit = 0

    for digit in range(12):
        control_digit += ssn_digits[digit] * special_number[digit]

    control_digit = 1 if control_digit % 11 == 10 else control_digit % 11

    return control_digit == ssn_digits[-1]


def date_validation(ssn: str) -> bool:
    try:
        century = int(ssn[0])
        month = int(ssn[3:5])
        day = int(ssn[5:7])
        year = int(ssn[1:3])

        if century in [1, 2, 7, 8, 9]:
            year += 1900
        elif century in [3, 4]:
            year += 1800
        else:
            year += 2000

        input_date = f'{year}/{month}/{day}'
        valid_date = datetime.strptime(input_date, '%Y/%m/%d').date()

        if century in [1, 2, 7, 8, 9] and not (date(1900, 1, 1) <= valid_date <= date(1999, 12, 31)):
            raise ValueError
        elif century in [3, 4] and not (date(1800, 1, 1) <= valid_date <= date(1899, 12, 31)):
            raise ValueError
        elif century in [5, 6] and not (date(2000, 1, 1) <= valid_date <= datetime.now().date()):
            raise ValueError

    except ValueError:
        return False
    return True


def check_jj(ssn: str) -> bool:
    jj = int(ssn[7:9])

    if 1 <= jj <= 46 or jj in [51, 52]:
        return True

    return False


def check_nnn(ssn: str) -> bool:
    nnn = int(ssn[9:12])
    return nnn != 0


def ssn_validation(ssn: str) -> str:
    if len(ssn) != 13 or not ssn.isdigit():
        return "Invalid"

    return "Valid" if date_validation(ssn) and validate_c(ssn) and check_jj(ssn) and check_nnn(ssn) else "Invalid"


input_ssn = input("Input a Social Security Number: ")
# input_ssn = '1971113373381'
print(ssn_validation(input_ssn))