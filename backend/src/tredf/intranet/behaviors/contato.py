from plone.autoform.interfaces import IFormFieldProvider
from plone.schema.email import Email
from plone.supermodel import model
from tredf.intranet import _
from tredf.intranet.utils import validadores
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class IContato(model.Schema):
    """Provê campos de contato."""

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
        constraint=validadores.is_valid_email,
    )

    telefone = schema.TextLine(
        title=_("Telefone"),
        description=_("Informe o telefone de contato"),
        required=False,
        constraint=validadores.is_valid_telefone,
    )
