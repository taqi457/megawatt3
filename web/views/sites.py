from django.views.generic import TemplateView


class SitesView(TemplateView):
    template_name = 'sites.html'

    def get_context_data(self, **kwargs):
        pass


class SitesDetailView(TemplateView):

    template_name = 'site_detail.html'

    def get_context_data(self, **kwargs):
        pass
