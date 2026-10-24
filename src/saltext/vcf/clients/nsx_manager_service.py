"""NSX Manager node services lifecycle (``/api/v1/node/services``).

Generic start/stop/restart for any NSX Manager node service (``ntp``,
``ssh``, ``syslog``, ``manager``, etc.) — distinct from
:mod:`nsx_node_services`, which manages fields deep inside the ``http``
service's own config, not its running state.
"""

from saltext.vcf.utils import nsx

PATH = "/api/v1/node/services"


def list_(opts, profile=None):
    return nsx.api_get(opts, PATH, profile=profile)


def get(opts, service_name, profile=None):
    return nsx.api_get(opts, f"{PATH}/{service_name}", profile=profile)


def start(opts, service_name, profile=None):
    return nsx.api_post(opts, f"{PATH}/{service_name}", params={"action": "start"}, profile=profile)


def stop(opts, service_name, profile=None):
    return nsx.api_post(opts, f"{PATH}/{service_name}", params={"action": "stop"}, profile=profile)


def restart(opts, service_name, profile=None):
    return nsx.api_post(
        opts, f"{PATH}/{service_name}", params={"action": "restart"}, profile=profile
    )
