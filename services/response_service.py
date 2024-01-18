from rest_framework import status
from rest_framework.response import Response


class ResponseService:

    def send_bad_request(self, error):
        return self.send_json({"error": error}, response_status=status.HTTP_400_BAD_REQUEST)

    def send_validation_error(self, errors):
        return self.send_json({"errors": errors}, response_status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def send_server_error(self, error):
        return self.send_json({"error": error}, response_status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def send_json(self, data, response_status=None):
        if isinstance(data, dict):
            data = {"data": data}

        if not response_status:
            response_status = status.HTTP_200_OK

        return Response(data, status=response_status)
