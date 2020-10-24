from django.core import mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST', ])
def send(request):
    subject = request.POST.get('subject', '')
    body = request.POST.get('body', '')
    if subject and body:
        try:
            mail.send_mail(subject, body, 'alec@aleckayetion.com', ['alec@aleckayetion.com'])
            content = {'message': 'sent'}
            return Response(content, status=status.HTTP_202_ACCEPTED)
        except mail.BadHeaderError:
            content = {'message': 'BadHeaderError'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
    content = {'message': 'no subject/body'}
    return Response(content, status=status.HTTP_400_BAD_REQUEST)


# with mail.get_connection() as connection:
#     mail.EmailMessage(
#         # subject1, body1, from1, [to1],
#         'test', 'body', 'no-reply@aleckayetion.com', ['alec.kaye@gmail.com',],
#         connection=connection,
#     ).send()
