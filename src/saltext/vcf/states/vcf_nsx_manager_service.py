"""State module for NSX Manager node service running state."""

from saltext.vcf.clients import nsx_manager_service as c

__virtualname__ = "vcf_nsx_manager_service"


def __virtual__():
    return __virtualname__


def _ret(name):
    return {"name": name, "changes": {}, "result": True, "comment": ""}


def running(name, running=True, profile=None):  # pylint: disable=redefined-outer-name
    """Ensure NSX Manager service *name* is running (or stopped, if *running* is False)."""
    ret = _ret(name)
    current = c.get(__opts__, name, profile=profile) or {}
    current_state = current.get("runtime_state")
    desired_state = "running" if running else "stopped"

    if current_state == desired_state:
        ret["comment"] = f"Service {name} already {desired_state}"
        return ret
    if __opts__["test"]:
        ret["result"] = None
        ret["comment"] = f"Service {name} would change from {current_state} to {desired_state}"
        return ret
    if running:
        c.start(__opts__, name, profile=profile)
    else:
        c.stop(__opts__, name, profile=profile)
    ret["changes"] = {"runtime_state": {"old": current_state, "new": desired_state}}
    ret["comment"] = f"Service {name} set to {desired_state}"
    return ret
