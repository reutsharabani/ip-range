#!/usr/bin/env python

from ipaddress import IPv4Address

class IPv4Range():

    def __init__(self, start, end):
        start = int(IPv4Address(start))
        end = int(IPv4Address(end))
        assert start < end
        self.range = range(start, end)
    
    def __iter__(self):
        yield from map(IPv4Address, self.range)

    def __getitem__(self, offset):
        return IPv4Address(self.range[offset])

    def __contains__(self, ip_obj):

        if isinstance(ip_obj, IPv4Range):
            return self.start <= ip_obj.start and self.end >= ip_obj.end

        return int(IPv4Address(ip_obj)) in self.range

    @property
    def start(self):
        return self.range[0]

    @property
    def end(self):
        return self.range[-1] + 1

    def intersects(self, other_range):
        return self.start < other_range.end and self.end >= other_range.start

    def __or__(self, other_range):
        assert self.intersects(other_range), 'ranges [%s]-[%s] do not intersect' % (self, other_range)
        start = min(self.start, other_range.start)
        end = max(self.end, other_range.end)
        return IPv4Range(start, end)

    def __and__(self, other_range):
        assert self.intersects(other_range), 'ranges [%s]-[%s] do not intersect' % (self, other_range)
        start = max(self.start, other_range.start)
        end = min(self.end, other_range.end)
        return IPv4Range(start, end)

    def __eq__(self, other_range):
        return self.range == other_range.range

    def __str__(self):
        return '<-->'.join(map(str, map(IPv4Address, (self.start, self.end, ))))
