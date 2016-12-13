# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from ncue_history.content import _
from zope import schema
from zope.interface import Interface
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.app.vocabularies.catalog import CatalogSource
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class INcueHistoryContentLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ICover(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )

    model.fieldset(
        'tab_for_cover',
        label=_(u"Tab for Cover"),
        fields=['tab_folder_1', 'tab_image_1',
                'tab_folder_2', 'tab_image_2',
                'tab_folder_3', 'tab_image_3',
                'tab_folder_4', 'tab_image_4',]
    )

    tab_folder_1 = RelationChoice(
        title=_(u"Folder for Tab 1"),
        source=CatalogSource(portal_type='Folder'),
    )

    tab_image_1 = RelationChoice(
        title=_(u"Image for Tab 1"),
        source=CatalogSource(portal_type='Image'),
    )

    tab_folder_2 = RelationChoice(
        title=_(u"Folder for Tab 2"),
        source=CatalogSource(portal_type='Folder'),
    )

    tab_image_2 = RelationChoice(
        title=_(u"Image for Tab 2"),
        source=CatalogSource(portal_type='Image'),
    )

    tab_folder_3 = RelationChoice(
        title=_(u"Folder for Tab 3"),
        source=CatalogSource(portal_type='Folder'),
    )

    tab_image_3 = RelationChoice(
        title=_(u"Image for Tab 3"),
        source=CatalogSource(portal_type='Image'),
    )

    tab_folder_4 = RelationChoice(
        title=_(u"Folder for Tab 4"),
        source=CatalogSource(portal_type='Folder'),
    )

    tab_image_4 = RelationChoice(
        title=_(u"Image for Tab 4"),
        source=CatalogSource(portal_type='Image'),
    )


    model.fieldset(
        'hero_slides',
        label=_(u"hero_slides"),
        fields=['hero_slides']
    )

    hero_slides = RelationList(
        title=_(u"Hero Slides"),
        value_type=RelationChoice(title=_(u"Related"),
                                  source=CatalogSource(portal_type='Image'),),
        required=False,
    )

