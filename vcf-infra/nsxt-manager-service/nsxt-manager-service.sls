{% from "nsxt-manager-service/map.jinja" import cfg with context %}

{{ cfg.service.name }}:
  vcf_nsx_manager_service.running:
    - running: {{ cfg.service.running }}
