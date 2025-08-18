from AccessControl import Unauthorized
from plone import api
from plone.dexterity.fti import DexterityFTI
from tredf.intranet.content.area import Area
from zope.component import createObject

import pytest


CONTENT_TYPE = "Area"


@pytest.fixture
def area_payload() -> dict:
    """Return a payload to create a new area."""
    return {
        "type": "Area",
        "id": "ti",
        "title": "Tecnologia da Informação",
        "description": ("Área responsável por TI"),
        "email": "ti@tre-df.jus.br",
        "telefone": "6132101234",
        "endereco": "Praça Municipal Qd. 02, Lote 06",
        "complemento": "",
        "cidade": "Brasília",
        "estado": "DF",
        "cep": "70094-901",
    }


class TestArea:
    @pytest.fixture(autouse=True)
    def _setup(self, get_fti, portal):
        self.fti = get_fti(CONTENT_TYPE)
        self.portal = portal

    def test_fti(self):
        assert isinstance(self.fti, DexterityFTI)

    def test_factory(self):
        factory = self.fti.factory
        obj = createObject(factory)
        assert obj is not None
        assert isinstance(obj, Area)

    @pytest.mark.parametrize(
        "behavior",
        [
            "plone.basic",
            "plone.namefromtitle",
            "plone.shortname",
            "plone.excludefromnavigation",
            "plone.versioning",
            "tredf.intranet.behavior.contato",
            "tredf.intranet.behavior.endereco",
            "volto.blocks",
            "plone.constraintypes",
            "volto.preview_image",
        ],
    )
    def test_has_behavior(self, get_behaviors, behavior):
        assert behavior in get_behaviors(CONTENT_TYPE)

    @pytest.mark.parametrize(
        "role,allowed",
        [
            ["Manager", True],
            ["Site Administrator", True],
            ["Editor", False],
            ["Reviewer", False],
            ["Contributor", False],
            ["Reader", False],
        ],
    )
    def test_create(self, area_payload, role: str, allowed: bool):
        with api.env.adopt_roles([role]):
            if allowed:
                content = api.content.create(container=self.portal, **area_payload)
                assert content.portal_type == CONTENT_TYPE
                assert isinstance(content, Area)
            else:
                with pytest.raises(Unauthorized):
                    api.content.create(container=self.portal, **area_payload)
