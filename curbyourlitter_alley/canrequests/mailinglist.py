from django.conf import settings

import mailchimp_subscribe


def subscribe(email_address):
    mailchimp_subscribe.subscribe(settings.MAILCHIMP_API_KEY,
                                  settings.MAILCHIMP_LIST_ID, email_address)
