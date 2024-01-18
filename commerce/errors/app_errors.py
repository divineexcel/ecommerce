import traceback
from builtins import staticmethod


class AppError(object):

    def __init__(self, message=None):
        self.message = message

    def get_message(self):
        return self.message

    def __str__(self):
        return self.message


class AppLogger:

    @staticmethod
    def report(e):
        print(e)
        traceback.print_exc()
