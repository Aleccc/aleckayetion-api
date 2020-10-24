from django.core import mail
from rest_framework.decorators import api_view


@api_view(['POST', ])
def send(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        body = request.POST.get('body', '')
        if subject and body:
            try:
                mail.send_mail(subject, body, 'alec@aleckayetion.com', ['alec@aleckayetion.com'])
            except mail.BadHeaderError:
                return False
        return True  # Response({"message": "Got some data!", "data": request.data})
    return False


# with mail.get_connection() as connection:
#     mail.EmailMessage(
#         # subject1, body1, from1, [to1],
#         'test', 'body', 'no-reply@aleckayetion.com', ['alec.kaye@gmail.com',],
#         connection=connection,
#     ).send()
