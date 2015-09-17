from django.conf.urls import url

from .views import AddRatingsView


urlpatterns = [
    url(r'.*', AddRatingsView.as_view()),
]
