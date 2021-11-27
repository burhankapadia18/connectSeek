from celery import shared_task

from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_welcome_mail(email, name):
    subject = f'Hey {name},\tWelcome to connectSeek'
    message = '''
Our objective through this portal is to provide a single place to students from where they can do all the study related activities without login to different websites. In other words, to provide a single place for all kind of jobs.
        
We hope you will learn better things from the platform.
        
        
Regards,
Burhan Kapdawala (Lead Engineer)
    '''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list, fail_silently=False)
    return None
