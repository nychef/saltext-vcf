"""State module for NSX security policies."""

from saltext.vcf.clients import nsx_security_policy as c

__virtualname__ = "vcf_nsx_security_policy"


def __virtual__():
    return __virtualname__


def _ret(name):
    return {"name": name, "changes": {}, "result": True, "comment": ""}


def present(name, domain="default", profile=None, apply=True, **spec):
    """Ensure the security policy *name* exists.

    Set *apply* to ``False`` to only perform a drift check: the state
    reports whether the policy would be created without touching NSX,
    regardless of ``test`` mode.
    """
    ret = _ret(name)
    if c.get_or_none(__opts__, name, domain=domain, profile=profile) is not None:
        ret["comment"] = f"Security policy {name} is already present"
        return ret
    if not apply:
        ret["result"] = None
        ret["changes"] = {"new": name}
        ret["comment"] = f"Security policy {name} drift detected: would be created"
        return ret
    if __opts__["test"]:
        ret["result"] = None
        ret["comment"] = f"Security policy {name} would be created"
        return ret
    c.create(__opts__, name, domain=domain, profile=profile, **spec)
    ret["changes"] = {"new": name}
    ret["comment"] = f"Security policy {name} created"
    return ret


def absent(name, domain="default", profile=None, apply=True):
    """Ensure the security policy *name* does not exist.

    Set *apply* to ``False`` to only perform a drift check: the state
    reports whether the policy would be deleted without touching NSX,
    regardless of ``test`` mode.
    """
    ret = _ret(name)
    if c.get_or_none(__opts__, name, domain=domain, profile=profile) is None:
        ret["comment"] = f"Security policy {name} is already absent"
        return ret
    if not apply:
        ret["result"] = None
        ret["changes"] = {"deleted": name}
        ret["comment"] = f"Security policy {name} drift detected: would be deleted"
        return ret
    if __opts__["test"]:
        ret["result"] = None
        ret["comment"] = f"Security policy {name} would be deleted"
        return ret
    c.delete(__opts__, name, domain=domain, profile=profile)
    ret["changes"] = {"deleted": name}
    ret["comment"] = f"Security policy {name} deleted"
    return ret
