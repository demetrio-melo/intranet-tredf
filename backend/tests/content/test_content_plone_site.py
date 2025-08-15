from AccessControl.users import nobody
from plone import api

import pytest


class TestPloneSite:
    """Testa que o Plone Site está configurado corretamente."""

    def test_workflow_state(self, portal):
        """Validar se o estado de workflow está correto."""
        expected = "internal"
        # Obtem estado de workflow do Plone Site
        value = api.content.get_state(portal)
        assert value == expected, (
            f"Estado de workflow é {value}, esperávamos {expected}"
        )

    @pytest.mark.parametrize(
        "permission,expected",
        [
            ["Access contents information", False],
            ["Modify portal content", False],
            ["View", False],
        ],
    )
    def test_anonymous_permissions(self, portal, permission: str, expected: bool):
        with api.env.adopt_user(user=nobody):
            user = api.user.get_current()
            has_permission = api.user.has_permission(permission, user=user, obj=portal)
            assert has_permission is expected, (
                f"Erro: Permissão {permission} para usuário Anônimo: {has_permission}"
            )
