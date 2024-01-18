from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if response.status_code in [403, 401] and 'detail' in response.data:
            if 'code' in response.data and response.data.get("code") == "user_not_found":
                message = "Request authorization failed"
            else:
                message = response.data['detail']
            response.data = {'message': message}

    return response
