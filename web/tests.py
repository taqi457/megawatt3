# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import time
import random

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from web.models import *
from web.templatetags.custom_filters import startswith

# Create your tests here.


def makeSite():
    site = Site()
    site.name = "TEST %s" % random.randint(1, 100)
    site.save()
    return site


def makeSiteDetail(site_id):
    sd = SiteDetail()
    sd.site_id = site_id
    sd.a_value = 4
    sd.b_value = 4
    sd.detail_date = datetime.date.today()
    sd.save()
    return sd


class SiteModelTest(TestCase):

    def test_is_creation_date_working(self):

        """
            A newly created model should have current time as created_time
        """

        site = Site(name="TEST")
        site.save()
        t = timezone.now()
        self.assertAlmostEqual(site.creation_date, t, delta=datetime.timedelta(0, 1, 3000))

    def test_is_modified_date_working(self):

        """
            Modified model should have current time as last_modified
        """

        site = Site(name="TEST1")
        site.save()
        t = timezone.now()
        self.assertAlmostEqual(site.last_modified, t, delta=datetime.timedelta(0, 1, 3000))
        time.sleep(1)
        site.name = "TEST2"
        site.save()
        t = timezone.now()
        self.assertAlmostEqual(site.last_modified, t, delta=datetime.timedelta(0, 1, 3000))


class StartWithFilterTest(TestCase):

    def test_when_word_starts_with_correct_string(self):
        self.assertEqual(startswith("Hello World", "Hello"), True)

    def test_when_word_starts_with_incorrect_string(self):
        self.assertEqual(startswith("Rawr", "Meow"), False)


class AllViewsTest(TestCase):

    def test_site_page_no_sites(self):
        response = self.client.get(reverse('sites'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No sites are available")
        self.assertQuerysetEqual(response.context['all_sites'], [])

    def test_site_page_with_sites(self):
        s = makeSite()
        response = self.client.get(reverse('sites'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, s.name)
        self.assertQuerysetEqual(response.context['all_sites'], ['<Site: Site object>'])

    def test_site_detail_page_with_no_data(self):
        s = makeSite()
        response = self.client.get(reverse('site_detail', args=(s.id, )))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No data available")
        self.assertQuerysetEqual(response.context['site_details'], [])

    def test_site_detail_page_with_data(self):
        s = makeSite()
        sd = makeSiteDetail(s.id)
        response = self.client.get(reverse('site_detail', args=(s.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<td>%s.00</td>" % sd.a_value)
        self.assertContains(response, "<td>%s.00</td>" % sd.b_value)
        self.assertQuerysetEqual(response.context['site_details'], ['<SiteDetail: SiteDetail object>'])

    def test_summary_page_with_no_data(self):
        response = self.client.get(reverse('summary'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No data available")
        self.assertQuerysetEqual(response.context['summary_data'], [])

    def test_summary_page_with_data(self):
        s = makeSite()
        sd = makeSiteDetail(s.id)
        sd_two = makeSiteDetail(s.id)
        a_sum = sd.a_value+sd_two.a_value
        b_sum = sd.b_value + sd_two.b_value
        response = self.client.get(reverse('summary'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<td>%s.00</td>" % a_sum)
        self.assertContains(response, "<td>%s.00</td>" % b_sum)
        self.assertQuerysetEqual(response.context['summary_data'],
                                 [u"{'name': u'%s', 'b_summary': %s.0, 'a_summary': %s.0}" % (s.name, b_sum, a_sum)])

    def test_summary_average_page_with_no_data(self):
        response = self.client.get(reverse('summary_average'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No data available")
        self.assertQuerysetEqual(response.context['summary_data'], [])

    def test_summary_average_page_with_data(self):
        s = makeSite()
        sd = makeSiteDetail(s.id)
        sd_two = makeSiteDetail(s.id)
        a_avg = (sd.a_value + sd_two.a_value) / 2
        b_avg = (sd.b_value + sd_two.b_value) / 2
        response = self.client.get(reverse('summary_average'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<td>%s.00</td>" % a_avg)
        self.assertContains(response, "<td>%s.00</td>" % b_avg)
        self.assertQuerysetEqual(response.context['summary_data'],
                                 [u"{'name': u'%s', 'b_summary': %s.0, 'a_summary': %s.0}" % (s.name, b_avg, a_avg)])


