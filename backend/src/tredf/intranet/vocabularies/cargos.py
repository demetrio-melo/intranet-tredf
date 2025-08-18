from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


OPCOES = [
    ("servidor", "Servidor"),
    ("terceiro", "Terceirizado"),
]


@provider(IVocabularyFactory)
def vocab_cargos(context) -> SimpleVocabulary:
    """Cargos da estrutura do TRE-DF."""
    terms = []
    for token, title in OPCOES:
        terms.append(SimpleTerm(token, token, title))
    return SimpleVocabulary(terms)
