"""megawatt3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from web.views import sites, summary


urlpatterns = [

    # SITES VIEWS
    url(r'^sites/(?P<site_id>\d+)', sites.SitesDetailView.as_view(), name="site_detail"),
    url(r'^(sites)?$', sites.SitesView.as_view(), name="sites"),

    # SUMMARY VIEWS
    url(r'^summary-average', summary.SummaryAverageView.as_view(), name="summary_average"),
    url(r'^summary', summary.SummaryView.as_view(), name="summary"),

]
