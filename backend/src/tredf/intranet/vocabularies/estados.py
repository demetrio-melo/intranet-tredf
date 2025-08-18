from tredf.intranet import _
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


OPCOES = [
    ("AC", _("Acre")),
    ("AL", _("Alagoas")),
    ("AP", _("Amapá")),
    ("AM", _("Amazonas")),
    ("BA", _("Bahia")),
    ("CE", _("Ceará")),
    ("DF", _("Distrito Federal")),
    ("ES", _("Espírito Santo")),
    ("GO", _("Goiás")),
    ("MA", _("Maranhão")),
    ("MT", _("Mato Grosso")),
    ("MS", _("Mato Grosso do Sul")),
    ("MG", _("Minas Gerais")),
    ("PA", _("Pará")),
    ("PB", _("Paraíba")),
    ("PR", _("Paraná")),
    ("PE", _("Pernambuco")),
    ("PI", _("Piauí")),
    ("RJ", _("Rio de Janeiro")),
    ("RN", _("Rio Grande do Norte")),
    ("RS", _("Rio Grande do Sul")),
    ("RO", _("Rondônia")),
    ("RR", _("Roraima")),
    ("SC", _("Santa Catarina")),
    ("SP", _("São Paulo")),
    ("SE", _("Sergipe")),
    ("TO", _("Tocantins")),
]


@provider(IVocabularyFactory)
def vocab_estados(context) -> SimpleVocabulary:
    """Estados do Brasil."""
    terms = []
    for token, title in OPCOES:
        terms.append(SimpleTerm(token, token, title))
    return SimpleVocabulary(terms)
