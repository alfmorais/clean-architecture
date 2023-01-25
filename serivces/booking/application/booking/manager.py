from booking.booking import BookingDTO
from booking.domain.booking.enums import ErrorCodes
from booking.domain.booking.exceptions import (
    CheckinDateCannotBeAfterCheckoutDate, CustomerCannotBeBlank)


class BookingManager(object):
    def create_new_booking(self, booking_dto: BookingDTO):
        domain_object = booking_dto._to_domain()

        try:
            if domain_object.is_valid():
                return "save"
            else:
                return "don't save"
        except CheckinDateCannotBeAfterCheckoutDate as error:
            return {"message": error.message, "code": ErrorCodes.CHECKINAFTERCHECKOUT}
        except CustomerCannotBeBlank as error:
            return {"message": error.message, "code": ErrorCodes.CUSTOMERISREQUIRED}
        except Exception as error:
            return {"message": error.message, "code": ErrorCodes.UNDEFINED}
