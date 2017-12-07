from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework import routers

from canrequests.views import CanRequestViewSet, PostImage


router = routers.DefaultRouter()
router.register('canrequests', CanRequestViewSet)

urlpatterns = [
    url(r'^streetratings/', include('streetratings.urls')),
    url(r'^canrequests/image/', PostImage.as_view()),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
