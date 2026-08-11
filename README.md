# CCNP Enterprise Networking Labs

This repository contains my hands-on networking labs created while studying
enterprise networking technologies and preparing for the Cisco CCNP Enterprise certification.

The main purpose of this repository is to document practical configurations,
network topologies, troubleshooting scenarios, and verification of various
enterprise networking technologies.

Labs are primarily built using Cisco IOS devices in GNS3.

---

## Technologies & Topics

The repository covers topics including:

### Routing
- BGP
  - eBGP
  - iBGP
  - Route Reflectors
  - BGP Path Selection
  - Weight
  - Local Preference
  - AS Path
  - MED
- OSPF
  - Multi-Area OSPF
  - Stub Areas
  - Totally Stubby Areas
  - NSSA
  - Route Summarization
  - Virtual Links
- EIGRP
  - Metric calculation
  - Route summarization
  - Redistribution

### Network Services
- NAT / PAT
- DHCP
- DNS
- Access Control Lists
- Policy-Based Routing

### VPN & Tunneling
- GRE
- IPsec
- VTI
- IKEv2

### IPv6
- IPv6 Routing
- OSPFv3
- IPv6 troubleshooting
- IPv4 / IPv6 interoperability

### Enterprise Technologies
- VRF
- FHRP
- QoS
- Multicast
- Network virtualization

### Software-Defined Networking
- Cisco Catalyst SD-WAN
- Cisco SD-Access
- LISP
- VXLAN

---

## Repository Structure

Each lab is stored in a separate directory and may contain:

- Network topology diagram
- Cisco IOS configurations
- Lab objectives
- Configuration explanation
- Verification commands
- Troubleshooting notes
- Test results

Example:

    BGP/
    ├── iBGP/
    ├── eBGP/
    ├── Route-Reflector/
    └── Path-Selection/

    OSPF/
    ├── Multi-Area/
    ├── NSSA/
    └── Stub-Area/

---

## Example Lab Structure

Each lab can contain files such as:

    BGP-Weight/
    │
    ├── README.md
    ├── topology.png
    │
    ├── configs/
    │   ├── R1.cfg
    │   ├── R2.cfg
    │   └── R3.cfg
    │
    └── verification/
        ├── show-ip-bgp.txt
        └── traceroute.txt

---

## Lab Documentation

Individual labs describe:

1. **Objective** – what the lab demonstrates.
2. **Topology** – network architecture and addressing.
3. **Configuration** – relevant Cisco IOS configuration.
4. **Verification** – commands used to verify operation.
5. **Troubleshooting** – problems encountered during configuration.
6. **Key Findings** – conclusions and observed protocol behavior.

---

## Example Verification Commands

Depending on the lab, verification may include commands such as:

    show ip route
    show ip protocols
    show ip ospf neighbor
    show ip eigrp neighbors
    show ip bgp
    show ip bgp summary
    show ip bgp neighbors
    traceroute
    ping

---

## Lab Environment

The labs are primarily created using:

- GNS3
- Cisco IOS / IOSv / IOU
- Linux
- Wireshark

Some labs may also include automation or configuration tools such as:

- Python
- PowerShell

---

## Goals

The purpose of this repository is to develop and demonstrate practical skills in:

- Enterprise network design
- Routing and switching
- BGP path selection
- Dynamic routing protocols
- IPv4 and IPv6
- VPN technologies
- Network troubleshooting
- Network virtualization
- Software-defined networking
- Network automation

---

## Disclaimer

This repository is intended for educational and laboratory purposes.

Configurations are created in virtual lab environments and should not be
used directly in production networks without appropriate validation.

---

## Author

**Tworzyk**

IT Infrastructure / Network Engineering
Goal -> Network Cloud Engineer

Certifications:

- Cisco Certified Network Associate (CCNA)
- Cisco Certified Support Technician – Networking (CCST)
- Microsoft Certified: Azure Administrator Associate (AZ-104)
- Microsoft Certified: Azure Fundamentals (AZ-900)
