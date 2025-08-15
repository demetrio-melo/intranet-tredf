from plone import api
from plone.base.interfaces.installable import INonInstallable
from Products.GenericSetup.tool import SetupTool
from tredf.intranet import logger
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles:
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "tredf.intranet:uninstall",
        ]


def fecha_intranet(portal_setup: SetupTool):
    """Aplica novo workflow para a intranet."""
    wf_tool = api.portal.get_tool("portal_workflow")
    wf_tool.updateRoleMappings()
    # Loga que modificação foi realizada
    logger.info("Permissões de workflow atualizadas")
