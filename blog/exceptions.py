
from rest_framework.exceptions import APIException
class IdNotAvailable(APIException):
    default_detail = 'Specified Blog id is not available'
