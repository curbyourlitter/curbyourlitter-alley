from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template


def send_moderation_email(can_request):
    ctx = {
        'obj': can_request,
        'base_url': settings.BASE_URL,
    }
    text = get_template('canrequests/moderation_email.txt').render(ctx)
    html = get_template('canrequests/moderation_email.html').render(ctx)
    send_mail(settings.EMAIL_SUBJECT_PREFIX + 'New can request', text,
              settings.DEFAULT_FROM_EMAIL, settings.MODERATORS,
              html_message=html)
