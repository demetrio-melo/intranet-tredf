from plone.dexterity.content import Container
from plone.schema.email import Email
from plone.supermodel import model
from tredf.intranet import _
from zope import schema
from zope.interface import implementer


class IArea(model.Schema):
    """Definição de uma Área."""

    model.fieldset(
        "contato",
        _("Contato"),
        fields=[
            "email",
            "telefone",
        ],
    )
    email = Email(
        title=_("Email"),
        required=True,
    )

    telefone = schema.TextLine(
        title=_("Telefone"),
        description=_("Informe o telefone de contato"),
        required=False,
    )


@implementer(IArea)
class Area(Container):
    """Uma Área no TRE-DF."""
