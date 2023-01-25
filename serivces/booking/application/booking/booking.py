"""
DTO - Data Transfer Object
Rev: 1.0
"""
from datetime import datetime

from booking.domain.booking.entities import Booking
from booking.domain.customers.entities import Customer


class BookingDTO(object):
    checkin: datetime
    checkout: datetime
    customer: Customer

    def __init__(self, checkin: datetime, checkout: datetime, customer: Customer):
        self.checkin = checkin
        self.checkout = checkout
        self.customer = customer

    def _to_domain(self):
        return Booking(self.checkin, self.checkout, self.customer)
