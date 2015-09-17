from django.conf import settings
from django.views.generic import TemplateView

from braces.views import StaffuserRequiredMixin


class AddRatingsView(StaffuserRequiredMixin, TemplateView):
    login_url = '/admin/login/'
    template_name = 'streetratings/add.html'

    def get_context_data(self, **kwargs):
        ctx = super(AddRatingsView, self).get_context_data(**kwargs)
        ctx['cartodbApiKey'] = settings.CARTODB_SYNC['API_KEY']
        return ctx
