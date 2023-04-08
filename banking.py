
def is_16_digits(card_number, full_name):
    print("Validating your card number...")
    if len(str(card_number)) == 16:
        with open('payment_result.txt', 'a') as f:
            f.write(f'{card_number}\nSuccessful Payment...\n{full_name}\n')
        print("Your payment was successful, the payment factor has been created.\nPlease close this window to continue...")
    else:
        with open('payment_result.txt', 'a') as f:
            f.write(
                f'{card_number}\nUnsuccessful Payment, Try Again...\n{full_name}\n')
        print("Your payment was unsuccessful, the payment factor has been created.\nPlease close this window to continue...")


class Validator:
    def __init__(self, card_number, full_name):
        self.__card_number = card_number
        self.__full_name = full_name
        is_16_digits(self.__card_number, self.__full_name)
