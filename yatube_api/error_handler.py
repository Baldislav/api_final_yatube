from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None and 'detail' in response.data:
        detail = response.data['detail']
        # Проверка, что detail — это объект с .code
        if hasattr(detail, 'code') and detail.code == 'not_authenticated':
            response.data['detail'] = (
                'Не авторизованным пользователям '
                'не доступен функционал подписок!'
            )
    return response
