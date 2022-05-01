import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.settings import RECAPTCHA_SECRET_KEY


@api_view(['POST', ])
def verify(request):
    token = request.data.get('response', '')
    error_msg = 'no token'
    try:
        if token:
            url = 'https://www.google.com/recaptcha/api/siteverify'
            content = requests.post(url=url, data={'secret': RECAPTCHA_SECRET_KEY, 'response': token}).content
            return Response(content, status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        error_msg = str(e)
    content = {'success': False,
               'challenge_ts': '',
               'hostname': '',
               'error-codes': [error_msg],
               }
    return Response(content, status=status.HTTP_400_BAD_REQUEST)
