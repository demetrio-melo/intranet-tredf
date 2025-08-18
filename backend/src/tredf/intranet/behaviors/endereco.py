from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from tredf.intranet import _
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class IEndereco(model.Schema):
    """Provê campos de endereço."""

    model.fieldset(
        "endereco",
        _("Endereço"),
        fields=[
            "endereco",
            "complemento",
            "cidade",
            "estado",
            "cep",
        ],
    )
    endereco = schema.TextLine(
        title=_("Endereço"),
        required=False,
        default="",
    )
    complemento = schema.TextLine(
        title=_("Complemento"),
        description=_("Ex. Anexo, Sala"),
        required=False,
        default="",
    )
    cidade = schema.TextLine(
        title=_("Cidade"),
        required=False,
        default="",
    )
    estado = schema.Choice(
        title=_("Estado"),
        vocabulary="tredf.intranet.vocabulary.estados",
        required=False,
    )
    cep = schema.TextLine(
        title=_("CEP"),
        required=False,
        default="",
    )
