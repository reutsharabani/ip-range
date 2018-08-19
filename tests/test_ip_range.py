#!/usr/bin/env python
import pytest

from ipaddress import IPv4Address
from iprange.iprange import IPv4Range


# parametrize all tests to run much more data

@pytest.mark.parametrize('ip_range, expected_output',
        [
            (IPv4Range(0, 3), [IPv4Address(0), IPv4Address(1), IPv4Address(2)]),
            (IPv4Range(0, 1), [IPv4Address(0)])
        ])
def test_list(ip_range, expected_output):
    assert list(ip_range) == expected_output


@pytest.mark.parametrize('ip_range,index,expected_output',
        [
            (IPv4Range(0, 1), 0, IPv4Address(0)),
            (IPv4Range(0, 1), -1, IPv4Address(0)),
            (IPv4Range(0, 2), -1, IPv4Address(1)),
            (IPv4Range(0, 2), -2, IPv4Address(0)),
        ])
def test_getitem(ip_range, index, expected_output):
    assert ip_range[index] == expected_output


@pytest.mark.parametrize('ip_address, ip_range, expected_output',
        [
            (IPv4Address(0), IPv4Range(0, 1), True),
            (IPv4Address(1), IPv4Range(0, 1), False),
            (IPv4Address(0), IPv4Range(1, 2), False),
            (IPv4Address(2), IPv4Range(1, 3), True),
        ])
def test_contains(ip_address, ip_range, expected_output):
    assert (ip_address in ip_range) == expected_output



@pytest.mark.parametrize('ip_range1, ip_range2, expected_output',
        [
            (IPv4Range(1,2), IPv4Range(1, 3), IPv4Range(1,3)),
            (IPv4Range(1,2), IPv4Range(2, 3), IPv4Range(1,3)),
        ])
def test_or_eq(ip_range1, ip_range2, expected_output):
    assert ip_range1 | ip_range2 == expected_output


@pytest.mark.parametrize('ip_range, expected_output',
        [
            (IPv4Range(1,2), 1),
            (IPv4Range(0, 5), 5),
        ])
def test_len(ip_range, expected_output):
    assert len(ip_range) == expected_output
