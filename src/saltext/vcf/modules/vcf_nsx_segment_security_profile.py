"""Execution module for NSX segment security profiles."""

from saltext.vcf.clients import nsx_segment_security_profile as c

__virtualname__ = "vcf_nsx_segment_security_profile"


def __virtual__():
    return __virtualname__


def list_(profile=None):
    """List.

    CLI Example:

    .. code-block:: bash

        salt '*' vcf_nsx_segment_security_profile.list_

    """
    return c.list_(__opts__, profile=profile)


def get(segment_security_profile, profile=None):
    """Get.

    CLI Example:

    .. code-block:: bash

        salt '*' vcf_nsx_segment_security_profile.get <segment_security_profile>

    """
    return c.get(__opts__, segment_security_profile, profile=profile)


def create(segment_security_profile, profile=None, **spec):
    """Create.

    CLI Example:

    .. code-block:: bash

        salt '*' vcf_nsx_segment_security_profile.create <segment_security_profile>

    """
    return c.create(__opts__, segment_security_profile, profile=profile, **spec)


def delete(segment_security_profile, profile=None):
    """Delete.

    CLI Example:

    .. code-block:: bash

        salt '*' vcf_nsx_segment_security_profile.delete <segment_security_profile>

    """
    return c.delete(__opts__, segment_security_profile, profile=profile)
