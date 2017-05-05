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
    assert {'physnet': 'net_A', 'switch': 'sw_B', 'pf': 'pf_3'} in updated_requests
    assert  {'physnet': 'net_B', 'switch': 'sw_A', 'pf': 'pf_4'} in updated_requests
