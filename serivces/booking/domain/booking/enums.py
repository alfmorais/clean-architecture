from enum import Enum


class ErrorCodes(Enum):
    CHECKINAFTERCHECKOUT = "Checkin date cannot be after checkout"
    UNDEFINED = "Undefined"
    CUSTOMERISREQUIRED = "Customer cannot be null, required parameter"
