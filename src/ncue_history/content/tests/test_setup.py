# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from ncue_history.content.testing import NCUE_HISTORY_CONTENT_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that ncue_history.content is properly installed."""

    layer = NCUE_HISTORY_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ncue_history.content is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ncue_history.content'))

    def test_browserlayer(self):
        """Test that INcueHistoryContentLayer is registered."""
        from ncue_history.content.interfaces import (
            INcueHistoryContentLayer)
        from plone.browserlayer import utils
        self.assertIn(INcueHistoryContentLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = NCUE_HISTORY_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['ncue_history.content'])

    def test_product_uninstalled(self):
        """Test if ncue_history.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ncue_history.content'))

    def test_browserlayer_removed(self):
        """Test that INcueHistoryContentLayer is removed."""
        from ncue_history.content.interfaces import INcueHistoryContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(INcueHistoryContentLayer, utils.registered_layers())
