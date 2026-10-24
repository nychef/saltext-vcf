{% from "nsxt-segment-mac-discovery-profile/map.jinja" import cfg with context %}

{{ cfg.profile.name }}:
  vcf_nsx_mac_discovery_profile.present:
    - mac_learning_enabled: {{ cfg.profile.spec.mac_learning_enabled }}
    - mac_limit: {{ cfg.profile.spec.mac_limit }}
    - mac_limit_policy: {{ cfg.profile.spec.mac_limit_policy }}
    - unknown_unicast_flooding_enabled: {{ cfg.profile.spec.unknown_unicast_flooding_enabled }}
