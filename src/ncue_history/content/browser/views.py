# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api


class FlickerView(BrowserView):
    """ Flicker View
    """
    index = ViewPageTemplateFile('template/flicker_view.pt')

    def __call__(self):
        return self.index()


class CoverView(BrowserView):
    """ Cover View
    """
    index = ViewPageTemplateFile('template/cover_view.pt')

    def __call__(self):
        return self.index()
