import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST', ])
def verify(request):
    key = request.data.get('secret', '')
    token = request.data.get('response', '')
    if key and token:
        url = 'https://www.google.com/recaptcha/api/siteverify'
        content = requests.post(url=url, data={'secret': key, 'response': token}).content
        return Response(content, status=status.HTTP_202_ACCEPTED)
    content = {'success': False,
               'challenge_ts': '',
               'hostname': '',
               'error-codes': [],
               }
    return Response(content, status=status.HTTP_400_BAD_REQUEST)
