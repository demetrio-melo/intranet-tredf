"""Portal settings tests."""

from plone import api

import pytest


class TestPortalSettings:
    """Test that Portal configuration is correctly done."""

    @pytest.mark.parametrize(
        "key,expected",
        [
            ["plone.site_title", "Intranet do TRE-DF"],
            ["plone.email_from_name", "Intranet TRE-DF"],
            ["plone.smtp_host", "localhost"],
            ["plone.smtp_port", 25],
        ],
    )
    def test_setting(self, portal, key: str, expected: str | int):
        """Test registry setting."""
        value = api.portal.get_registry_record(key)
        assert value == expected
