from django.views.generic import ListView
from web.models import *


class SitesView(ListView):
    template_name = 'site_list.html'
    context_object_name = 'all_sites'
    model = Site


class SitesDetailView(ListView):

    template_name = 'sitedetail_list.html'
    context_object_name = 'site_details'

    def get_queryset(self):
        return SiteDetail.objects.filter(site_id=self.kwargs['site_id'])

    def get_context_data(self, **kwargs):
        context = super(SitesDetailView, self).get_context_data(**kwargs)
        context['site_name'] = Site.objects.get(id=self.kwargs['site_id']).name
        return context
