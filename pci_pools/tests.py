from pci_pools import pick


def test_get_two_pci():
    requests = [
        {'physnet': 'net_A'},
        {'physnet': 'net_B'}
    ]
    pools = [
        {'physnet': 'net_A', 'switch': 'sw_A', 'pf': 'pf_3'},
        {'physnet': 'net_A', 'switch': 'sw_B', 'pf': 'pf_3'},
        {'physnet': 'net_B', 'switch': 'sw_A', 'pf': 'pf_4'},
        {'physnet': 'net_B', 'switch': 'sw_B', 'pf': 'pf_3'},
    ]
    unique_tags = ['switch', 'pf']
    updated_requests = pick(pools, requests, unique_tags)
    assert {'physnet': 'net_A', 'switch': 'sw_B', 'pf': 'pf_3'} \
        in updated_requests
    assert {'physnet': 'net_B', 'switch': 'sw_A', 'pf': 'pf_4'} \
        in updated_requests


def test_fail_for_non_unique():
    requests = [
        {'physnet': 'net_A'},
        {'physnet': 'net_B'}
    ]
    pools = [
        {'physnet': 'net_A', 'switch': 'sw_A', 'pf': 'pf_3'},
        {'physnet': 'net_B', 'switch': 'sw_A', 'pf': 'pf_4'},
    ]
    unique_tags = ['switch', 'pf']
    assert pick(pools, requests, unique_tags) is None


def test_overlapped_requests():
    requests = [
        {'physnet': 'net_A'},
        {'vendor': 'abc'}
    ]
    pools = [
        {'subnet': 'blue', 'physnet': 'net_A'},
        {'subnet': 'red', 'physnet': 'net_A', 'vendor': 'abc'},
        {'subnet': 'blue', 'vendor': 'abc'},
    ]
    unique_tags = ['subnet']
    updated_requests = pick(pools, requests, unique_tags)
    assert {'physnet': 'net_A', 'subnet': 'blue'} in updated_requests
    assert {'vendor': 'abc', 'subnet': 'red'} in updated_requests
