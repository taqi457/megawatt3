from django.views.generic import ListView, TemplateView
from django.db.models import Avg

from web.models import *


class SummaryAverageView(ListView):
    template_name = 'summary.html'
    context_object_name = 'summary_data'

    def get_queryset(self):
        return Site.objects.values('name').annotate(a_summary=Avg('sitedetail__a_value'),
                                                    b_summary=Avg('sitedetail__b_value'))


class SummaryView(TemplateView):
    template_name = 'summary.html'

    def get_context_data(self, **kwargs):
        context = super(SummaryView, self).get_context_data(**kwargs)
        context['summary_data'] = [{
                    'name': s.name,
                    'a_summary': sum([sd.a_value for sd in SiteDetail.objects.filter(site_id=s.id)]),
                    'b_summary': sum([sd.b_value for sd in SiteDetail.objects.filter(site_id=s.id)])
            } for s in Site.objects.all()]
        return context

