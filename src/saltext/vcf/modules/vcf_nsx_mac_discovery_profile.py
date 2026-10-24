"""Execution module for NSX MAC discovery profiles."""

from saltext.vcf.clients import nsx_mac_discovery_profile as c

__virtualname__ = "vcf_nsx_mac_discovery_profile"


def __virtual__():
    return __virtualname__


def list_(profile=None):
    """List.

    CLI Example:

    .. code-block:: bash

        salt '*' vcf_nsx_mac_discovery_profile.list_

    """
    return c.list_(__opts__, profile=profile)


def get(mac_discovery_profile, profile=None):
    """Get.

    CLI Example:

    .. code-block:: bash

        salt '*' vcf_nsx_mac_discovery_profile.get <mac_discovery_profile>

    """
    return c.get(__opts__, mac_discovery_profile, profile=profile)


def create(mac_discovery_profile, profile=None, **spec):
    """Create.

    CLI Example:

    .. code-block:: bash

        salt '*' vcf_nsx_mac_discovery_profile.create <mac_discovery_profile>

    """
    return c.create(__opts__, mac_discovery_profile, profile=profile, **spec)


def delete(mac_discovery_profile, profile=None):
    """Delete.

    CLI Example:

    .. code-block:: bash

        salt '*' vcf_nsx_mac_discovery_profile.delete <mac_discovery_profile>

    """
    return c.delete(__opts__, mac_discovery_profile, profile=profile)
