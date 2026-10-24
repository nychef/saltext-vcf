"""Tests for states.vcf_nsx_manager_service."""

import pytest

from saltext.vcf.clients import nsx_manager_service as c
from saltext.vcf.states import vcf_nsx_manager_service as st


@pytest.fixture(autouse=True)
def inject_opts(monkeypatch, opts):
    monkeypatch.setattr(st, "__opts__", opts, raising=False)


def test_running_already_matches(monkeypatch):
    monkeypatch.setattr(
        c, "get", lambda opts, service_name, profile=None: {"runtime_state": "running"}
    )
    ret = st.running("ntp", running=True)
    assert ret["changes"] == {}


def test_running_starts_stopped_service(monkeypatch):
    calls = []
    monkeypatch.setattr(
        c, "get", lambda opts, service_name, profile=None: {"runtime_state": "stopped"}
    )
    monkeypatch.setattr(
        c, "start", lambda opts, service_name, profile=None: calls.append(service_name)
    )
    ret = st.running("ntp", running=True)
    assert ret["changes"] == {"runtime_state": {"old": "stopped", "new": "running"}}
    assert calls == ["ntp"]


def test_running_stops_running_service(monkeypatch):
    calls = []
    monkeypatch.setattr(
        c, "get", lambda opts, service_name, profile=None: {"runtime_state": "running"}
    )
    monkeypatch.setattr(
        c, "stop", lambda opts, service_name, profile=None: calls.append(service_name)
    )
    ret = st.running("ntp", running=False)
    assert ret["changes"] == {"runtime_state": {"old": "running", "new": "stopped"}}
    assert calls == ["ntp"]


def test_running_test_mode(monkeypatch):
    monkeypatch.setattr(
        c, "get", lambda opts, service_name, profile=None: {"runtime_state": "stopped"}
    )
    monkeypatch.setattr(st, "__opts__", {"test": True}, raising=False)
    ret = st.running("ntp", running=True)
    assert ret["result"] is None
