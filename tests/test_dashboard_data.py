from learn_unsloth_lab.dashboard_data import collect_dashboard_data
def test_dashboard_data_collects(): assert 'datasets' in collect_dashboard_data('.')
