"""Execution module for NSX IP discovery profiles."""

from saltext.vcf.clients import nsx_ip_discovery_profile as c

__virtualname__ = "vcf_nsx_ip_discovery_profile"


def __virtual__():
    return __virtualname__


def list_(profile=None):
    """List.

    CLI Example:

    .. code-block:: bash

        salt '*' vcf_nsx_ip_discovery_profile.list_

    """
    return c.list_(__opts__, profile=profile)


def get(ip_discovery_profile, profile=None):
    """Get.

    CLI Example:

    .. code-block:: bash

        salt '*' vcf_nsx_ip_discovery_profile.get <ip_discovery_profile>

    """
    return c.get(__opts__, ip_discovery_profile, profile=profile)


def create(ip_discovery_profile, profile=None, **spec):
    """Create.

    CLI Example:

    .. code-block:: bash

        salt '*' vcf_nsx_ip_discovery_profile.create <ip_discovery_profile>

    """
    return c.create(__opts__, ip_discovery_profile, profile=profile, **spec)


def delete(ip_discovery_profile, profile=None):
    """Delete.

    CLI Example:

    .. code-block:: bash

        salt '*' vcf_nsx_ip_discovery_profile.delete <ip_discovery_profile>

    """
    return c.delete(__opts__, ip_discovery_profile, profile=profile)
