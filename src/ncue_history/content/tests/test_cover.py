# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from ncue_history.content.testing import NCUE_HISTORY_CONTENT_INTEGRATION_TESTING  # noqa
from ncue_history.content.interfaces import ICover

import unittest2 as unittest


class CoverIntegrationTest(unittest.TestCase):

    layer = NCUE_HISTORY_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Cover')
        schema = fti.lookupSchema()
        self.assertEqual(ICover, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Cover')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Cover')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(ICover.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('Cover', 'Cover')
        self.assertTrue(
            ICover.providedBy(self.portal['Cover'])
        )
