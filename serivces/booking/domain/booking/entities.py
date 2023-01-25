from datetime import datetime

from domain.customers.entities import Customer
from domain.rooms.entities import Room

from .exceptions import (CheckinDateCannotBeAfterCheckoutDate,
                         CustomerCannotBeBlank)


class Booking(object):
    checkin: datetime
    checkout: datetime
    customer: Customer
    margin: float
    room: Room

    def __init__(self, checkin: datetime, checkout: datetime, customer: Customer):
        self.checkin = checkin
        self.checkout = checkout
        self.customer = customer

    def close_booking(self):
        pass

    def is_valid(self):
        if self.checkin > self.checkout:
            raise CheckinDateCannotBeAfterCheckoutDate(
                "Checkin cannot be after Checkout"
            )
        elif not self.customer:
            raise CustomerCannotBeBlank("Customer is a required information")

        return True
