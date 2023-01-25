class CheckinDateCannotBeAfterCheckoutDate(Exception):
    def __init__(self, message) -> None:
        self.message = message


class CustomerCannotBeBlank(Exception):
    def __init__(self, message) -> None:
        self.message = message
