from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class IArea(model.Schema):
    """Definição de uma Área."""


@implementer(IArea)
class Area(Container):
    """Uma Área no TRE-DF."""
