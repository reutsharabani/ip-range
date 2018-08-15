#!/usr/bin/env python

from ipaddress import IPv4Address

class IPv4Range():

    def __init__(self, start, end):
        start = int(IPv4Address(start))
        end = int(IPv4Address(end))
        self.range = range(start, end)
    
    def __iter__(self):
        yield from map(IPv4Address, self.range)

    def __getitem__(self, offset):
        return IPv4Address(self.range[offset])

    def __contains__(self, ip):
        return int(IPv4Address(ip)) in self.range

