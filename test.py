#!/usr/bin/env python
from  ipaddress import IPv4Address
from iprange import IPv4Range

assert list(IPv4Range(0, 5)) == list(map(IPv4Address, range(5)))
assert IPv4Range(0, 5)[1] == IPv4Address(1)
assert IPv4Address(0) in IPv4Range(0, 5)
assert IPv4Address(5) not in IPv4Range(0, 5)
