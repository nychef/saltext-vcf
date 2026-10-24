"""NSX MAC discovery profile (Policy API ``/infra/mac-discovery-profiles``).

Controls MAC learning/change limits and unknown-unicast flooding for a
segment/port — attached to a segment or segment port, not created here.
"""

import requests

from saltext.vcf.utils import nsx

PATH = "/policy/api/v1/infra/mac-discovery-profiles"


def list_(opts, profile=None):
    return nsx.api_get(opts, PATH, profile=profile)


def get(opts, mac_discovery_profile, profile=None):
    return nsx.api_get(opts, f"{PATH}/{mac_discovery_profile}", profile=profile)


def get_or_none(opts, mac_discovery_profile, profile=None):
    try:
        return get(opts, mac_discovery_profile, profile=profile)
    except requests.HTTPError as exc:
        if exc.response is not None and exc.response.status_code == 404:
            return None
        raise


def create(opts, mac_discovery_profile, profile=None, **spec):
    body = {"display_name": spec.pop("display_name", mac_discovery_profile)}
    body.update(spec)
    return nsx.api_put(opts, f"{PATH}/{mac_discovery_profile}", body=body, profile=profile)


def delete(opts, mac_discovery_profile, profile=None):
    return nsx.api_delete(opts, f"{PATH}/{mac_discovery_profile}", profile=profile)
