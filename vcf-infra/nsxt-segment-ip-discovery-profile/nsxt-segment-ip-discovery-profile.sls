{% from "nsxt-segment-ip-discovery-profile/map.jinja" import cfg with context %}

{{ cfg.profile.name }}:
  vcf_nsx_ip_discovery_profile.present:
    - arp_snooping_enabled: {{ cfg.profile.spec.arp_snooping_enabled }}
    - dhcp_snooping_enabled: {{ cfg.profile.spec.dhcp_snooping_enabled }}
    - vmtools_enabled: {{ cfg.profile.spec.vmtools_enabled }}
    - nd_snooping_enabled: {{ cfg.profile.spec.nd_snooping_enabled }}
