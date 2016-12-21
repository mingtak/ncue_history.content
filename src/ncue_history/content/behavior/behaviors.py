# -*- coding: utf-8 -*-
from ncue_history.content import _
from plone.supermodel import directives
from zope import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope.component import adapts
from zope.interface import alsoProvides, implements
from zope.interface import provider
from z3c.relationfield.schema import RelationList, RelationChoice
from plone.app.vocabularies.catalog import CatalogSource
from plone.dexterity.interfaces import IDexterityContent


class IFlicker(model.Schema):
    """Add a field to fill Flicker embedded code
    """

    directives.fieldset(
            'Flicker',
            label=_(u'Flicker'),
            fields=('flickerEmbedCode',),
        )

    flickerEmbedCode = schema.TextLine(
        title=_(u"Flicker Embed Code"),
        required=False,
    )


class IBxSlider(model.Schema):
    """Add a field to select images for BxSlider
    """

    directives.fieldset(
            'BxSlider',
            label=_(u'BxSleder'),
            fields=('bxSlider',),
        )

    bxSlider = RelationList(
        title=_(u"BxSlider Selector"),
        value_type=RelationChoice(title=_(u"Related"),
                                  source=CatalogSource(portal_type='Image'),),
        required=False,
    )


alsoProvides(IFlicker, IFormFieldProvider)
alsoProvides(IBxSlider, IFormFieldProvider)


def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class Flicker(object):
    implements(IFlicker)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
    flickerEmbedCode = context_property("flickerEmbedCode")


class BxSlider(object):
    implements(IBxSlider)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
    bxSlider = context_property("bxSlider")
