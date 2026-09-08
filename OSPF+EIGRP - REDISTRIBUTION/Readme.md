# OSPF + EIGRP - Route Redistribution

## Overview

This lab demonstrates **route redistribution between OSPF and EIGRP** using Cisco IOS in GNS3.

The topology consists of two routing domains:

- **OSPF** – R1, R2, R3 and R4
- **EIGRP** – R3, R5 and R6

R3 participates in both routing protocols and is responsible for redistributing routes between the OSPF and EIGRP domains.

The topology includes redundant paths between the routers, allowing the behavior of dynamic routing protocols and route selection to be observed.

## Topology

![OSPF + EIGRP topology](Topology/OSPF+EIGRP.png)

## Technologies

- Cisco IOS
- OSPFv2
- EIGRP
- Route Redistribution
- IPv4
- GNS3
- Loopback Interfaces

## Addressing

| Router | Protocol | Loopback |
|--------|----------|----------|
| R1 | OSPF | 1.1.1.1/32 |
| R2 | OSPF | 2.2.2.2/32 |
| R3 | OSPF / EIGRP | 3.3.3.3/32 |
| R4 | OSPF | 4.4.4.4/32 |
| R5 | EIGRP | 5.5.5.5/32 |
| R6 | EIGRP | 6.6.6.6/32 |

### Network Links

| Connection | Network |
|------------|---------|
| PC2 – R1 | 172.0.1.0/24 |
| R1 – R2 | 172.0.12.0/24 |
| R1 – R3 | 172.0.13.0/24 |
| R2 – R4 | 172.0.24.0/24 |
| R3 – R4 | 172.0.34.0/24 |
| R3 – R5 | 172.0.35.0/24 |
| R3 – R6 | 172.0.36.0/24 |
| R4 – R6 | 172.0.46.0/24 |
| R5 – R6 | 172.0.56.0/24 |
| R5 – PC1 | 10.0.5.0/24 |
| R6 – PC3 | 192.168.6.0/24 |

## OSPF

OSPF is configured on R1, R2, R3 and R4.

OSPF provides dynamic routing within the upper part of the topology. R3 participates in OSPF and EIGRP, allowing routing information to be exchanged between both routing domains.

## EIGRP

EIGRP is configured on R3, R5 and R6.

The EIGRP domain provides connectivity to the networks behind R5 and R6. EIGRP uses a composite metric based primarily on bandwidth and delay.

## Route Redistribution

R3 is configured as the redistribution point between OSPF and EIGRP.

### OSPF → EIGRP

Routes learned through OSPF are redistributed into EIGRP and appear as external EIGRP routes:

```text
D EX
