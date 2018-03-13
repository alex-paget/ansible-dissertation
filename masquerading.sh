#!/bin/bash
# This script enables masquerading for a HPC Orchestator cluster
# Giving compute nodes access to the internet
# Add masquerading to work zone
firewall-cmd --zone=work --add-masquerade --permanent
# Reload firewalld rules
firewall-cmd --reload
# Add masquerading to trusted zone
firewall-cmd --zone=trusted --add-masquerade --permanent
# Reload firewalld rules
firewall-cmd --reload
# Add postrouting to external interface
firewall-cmd --direct --add-rule ipv4 nat POSTROUTING 0 -o eno1 -j MASQUERADE
# Forward packets from internal into external interface
firewall-cmd --direct --add-rule ipv4 filter FORWARD 0 -i eno2 -o eno1 -j ACCEPT
# Forward RELATED and ESTABLISHED packets from external to internal interface
firewall-cmd --direct --add-rule ipv4 filter FORWARD 0 -i eno1 -o eno2 -m state --state RELATED,ESTABLISHED -j ACCEPT
