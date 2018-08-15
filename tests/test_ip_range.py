#!/usr/bin/env python
from ipaddress import IPv4Address
from iprange.iprange import IPv4Range


# parametrize all tests to run much more data


def test_list():
    assert list(IPv4Range(0, 5)) == list(map(IPv4Address, range(5)))


def test_getitem():
    assert IPv4Range(0, 5)[1] == IPv4Address(1)


def test_contains():
    assert IPv4Address(0) in IPv4Range(0, 5)


def test_not_contains():
    assert IPv4Address(5) not in IPv4Range(0, 5)


def test_or_eq():
    assert IPv4Range(0, 5) | IPv4Range(5,10) == IPv4Range(0, 10)


def test_len():
    assert len(IPv4Range(0, 5)) == 5
