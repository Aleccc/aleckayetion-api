from django.core import mail
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST', ])
def send(request):
    subject = request.data.get('subject', '')
    body = request.data.get('body', '')
    to = request.data.get('to', 'alec@aleckayetion.com')
    to = [x.strip() for x in to.split(',')]

    try:
        for x in to:
            validate_email(x)
    except ValidationError:
        content = {'message': 'invalid email included', 'data': str(to)}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    if not subject and not body:
        content = {'message': 'no subject/body', 'data': request.data}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    try:
        mail.send_mail(subject, body, 'alec@aleckayetion.com', to)
        content = {'message': 'sent'}
        return Response(content, status=status.HTTP_202_ACCEPTED)
    except mail.BadHeaderError:
        content = {'message': 'BadHeaderError'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
