"""Execution module for NSX Manager node services lifecycle."""

from saltext.vcf.clients import nsx_manager_service as c

__virtualname__ = "vcf_nsx_manager_service"


def __virtual__():
    return __virtualname__


def list_(profile=None):
    """List.

    CLI Example:

    .. code-block:: bash

        salt '*' vcf_nsx_manager_service.list_

    """
    return c.list_(__opts__, profile=profile)


def get(service_name, profile=None):
    """Get.

    CLI Example:

    .. code-block:: bash

        salt '*' vcf_nsx_manager_service.get <service_name>

    """
    return c.get(__opts__, service_name, profile=profile)


def start(service_name, profile=None):
    """Start.

    CLI Example:

    .. code-block:: bash

        salt '*' vcf_nsx_manager_service.start <service_name>

    """
    return c.start(__opts__, service_name, profile=profile)


def stop(service_name, profile=None):
    """Stop.

    CLI Example:

    .. code-block:: bash

        salt '*' vcf_nsx_manager_service.stop <service_name>

    """
    return c.stop(__opts__, service_name, profile=profile)


def restart(service_name, profile=None):
    """Restart.

    CLI Example:

    .. code-block:: bash

        salt '*' vcf_nsx_manager_service.restart <service_name>

    """
    return c.restart(__opts__, service_name, profile=profile)
