from django.views.generic import TemplateView


class SummaryView(TemplateView):
    template_name = 'summary.html'

    def get_context_data(self, **kwargs):
        pass


class SummaryAverageView(TemplateView):
    template_name = 'summary.html'

    def get_context_data(self, **kwargs):
        pass

