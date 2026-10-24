"""NSX segment security profile (Policy API ``/infra/segment-security-profiles``).

Controls BPDU filtering, DHCP client/server block, and spoofguard-adjacent
switch security settings for a segment/port — attached to a segment or
segment port, not created here.
"""

import requests

from saltext.vcf.utils import nsx

PATH = "/policy/api/v1/infra/segment-security-profiles"


def list_(opts, profile=None):
    return nsx.api_get(opts, PATH, profile=profile)


def get(opts, segment_security_profile, profile=None):
    return nsx.api_get(opts, f"{PATH}/{segment_security_profile}", profile=profile)


def get_or_none(opts, segment_security_profile, profile=None):
    try:
        return get(opts, segment_security_profile, profile=profile)
    except requests.HTTPError as exc:
        if exc.response is not None and exc.response.status_code == 404:
            return None
        raise


def create(opts, segment_security_profile, profile=None, **spec):
    body = {"display_name": spec.pop("display_name", segment_security_profile)}
    body.update(spec)
    return nsx.api_put(opts, f"{PATH}/{segment_security_profile}", body=body, profile=profile)


def delete(opts, segment_security_profile, profile=None):
    return nsx.api_delete(opts, f"{PATH}/{segment_security_profile}", profile=profile)
