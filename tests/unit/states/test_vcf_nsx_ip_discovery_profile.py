"""Tests for states.vcf_nsx_ip_discovery_profile."""

import pytest

from saltext.vcf.clients import nsx_ip_discovery_profile as c
from saltext.vcf.states import vcf_nsx_ip_discovery_profile as st


@pytest.fixture(autouse=True)
def inject_opts(monkeypatch, opts):
    monkeypatch.setattr(st, "__opts__", opts, raising=False)


def test_present_already_exists(monkeypatch):
    monkeypatch.setattr(c, "get_or_none", lambda opts, name, profile=None: {"id": name})
    ret = st.present("ip-discovery-01")
    assert ret["changes"] == {}


def test_present_creates(monkeypatch):
    calls = []
    monkeypatch.setattr(c, "get_or_none", lambda opts, name, profile=None: None)
    monkeypatch.setattr(
        c, "create", lambda opts, name, profile=None, **spec: calls.append((name, spec))
    )
    ret = st.present("ip-discovery-01", arp_snooping_enabled=True)
    assert ret["changes"] == {"new": "ip-discovery-01"}
    assert calls == [("ip-discovery-01", {"arp_snooping_enabled": True})]


def test_present_test_mode(monkeypatch):
    monkeypatch.setattr(c, "get_or_none", lambda opts, name, profile=None: None)
    monkeypatch.setattr(st, "__opts__", {"test": True}, raising=False)
    ret = st.present("ip-discovery-01")
    assert ret["result"] is None


def test_absent_already_absent(monkeypatch):
    monkeypatch.setattr(c, "get_or_none", lambda opts, name, profile=None: None)
    ret = st.absent("ip-discovery-01")
    assert ret["changes"] == {}


def test_absent_deletes(monkeypatch):
    calls = []
    monkeypatch.setattr(c, "get_or_none", lambda opts, name, profile=None: {"id": name})
    monkeypatch.setattr(c, "delete", lambda opts, name, profile=None: calls.append(name))
    ret = st.absent("ip-discovery-01")
    assert ret["changes"] == {"deleted": "ip-discovery-01"}
    assert calls == ["ip-discovery-01"]


def test_absent_test_mode(monkeypatch):
    monkeypatch.setattr(c, "get_or_none", lambda opts, name, profile=None: {"id": name})
    monkeypatch.setattr(st, "__opts__", {"test": True}, raising=False)
    ret = st.absent("ip-discovery-01")
    assert ret["result"] is None
