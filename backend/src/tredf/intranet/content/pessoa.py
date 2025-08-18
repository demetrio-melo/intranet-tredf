from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class IPessoa(model.Schema):
    """Definição de uma Pessoa."""


@implementer(IPessoa)
class Pessoa(Container):
    """Uma Pessoa colaboradora do TRE-DF."""
