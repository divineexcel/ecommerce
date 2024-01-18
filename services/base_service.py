from commerce.errors.app_errors import AppError


class BaseService:

    def __init__(self, request):
        self.request = request

    @classmethod
    def make_error(cls, error):
        return AppError(error)

