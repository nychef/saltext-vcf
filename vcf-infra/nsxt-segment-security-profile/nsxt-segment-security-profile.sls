{% from "nsxt-segment-security-profile/map.jinja" import cfg with context %}

{{ cfg.profile.name }}:
  vcf_nsx_segment_security_profile.present:
    - bpdu_filter_enable: {{ cfg.profile.spec.bpdu_filter_enable }}
    - dhcp_client_block_enabled: {{ cfg.profile.spec.dhcp_client_block_enabled }}
    - dhcp_server_block_enabled: {{ cfg.profile.spec.dhcp_server_block_enabled }}
    - non_ip_traffic_block_enabled: {{ cfg.profile.spec.non_ip_traffic_block_enabled }}
    - ra_guard_enabled: {{ cfg.profile.spec.ra_guard_enabled }}
