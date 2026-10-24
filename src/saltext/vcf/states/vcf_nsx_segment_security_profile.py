"""State module for NSX segment security profiles."""

from saltext.vcf.clients import nsx_segment_security_profile as c

__virtualname__ = "vcf_nsx_segment_security_profile"


def __virtual__():
    return __virtualname__


def _ret(name):
    return {"name": name, "changes": {}, "result": True, "comment": ""}


def present(name, profile=None, **spec):
    """Ensure segment security profile *name* exists.

    Policy API PUT is idempotent, so this only checks presence — it does
    not diff/update fields on an already-existing profile.
    """
    ret = _ret(name)
    if c.get_or_none(__opts__, name, profile=profile) is not None:
        ret["comment"] = f"Segment security profile {name} is already present"
        return ret
    if __opts__["test"]:
        ret["result"] = None
        ret["comment"] = f"Segment security profile {name} would be created"
        return ret
    c.create(__opts__, name, profile=profile, **spec)
    ret["changes"] = {"new": name}
    ret["comment"] = f"Segment security profile {name} created"
    return ret


def absent(name, profile=None):
    """Ensure segment security profile *name* does not exist."""
    ret = _ret(name)
    if c.get_or_none(__opts__, name, profile=profile) is None:
        ret["comment"] = f"Segment security profile {name} is already absent"
        return ret
    if __opts__["test"]:
        ret["result"] = None
        ret["comment"] = f"Segment security profile {name} would be deleted"
        return ret
    c.delete(__opts__, name, profile=profile)
    ret["changes"] = {"deleted": name}
    ret["comment"] = f"Segment security profile {name} deleted"
    return ret
