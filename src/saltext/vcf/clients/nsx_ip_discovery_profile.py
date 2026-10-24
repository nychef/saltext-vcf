"""NSX IP discovery profile (Policy API ``/infra/ip-discovery-profiles``).

Controls how a segment/port learns VM IP addresses (ARP snooping, DHCP
snooping, VMware Tools, ND snooping) — attached to a segment or segment
port, not created here.
"""

import requests

from saltext.vcf.utils import nsx

PATH = "/policy/api/v1/infra/ip-discovery-profiles"


def list_(opts, profile=None):
    return nsx.api_get(opts, PATH, profile=profile)


def get(opts, ip_discovery_profile, profile=None):
    return nsx.api_get(opts, f"{PATH}/{ip_discovery_profile}", profile=profile)


def get_or_none(opts, ip_discovery_profile, profile=None):
    try:
        return get(opts, ip_discovery_profile, profile=profile)
    except requests.HTTPError as exc:
        if exc.response is not None and exc.response.status_code == 404:
            return None
        raise


def create(opts, ip_discovery_profile, profile=None, **spec):
    body = {"display_name": spec.pop("display_name", ip_discovery_profile)}
    body.update(spec)
    return nsx.api_put(opts, f"{PATH}/{ip_discovery_profile}", body=body, profile=profile)


def delete(opts, ip_discovery_profile, profile=None):
    return nsx.api_delete(opts, f"{PATH}/{ip_discovery_profile}", profile=profile)
