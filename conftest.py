import pytest
from env.devices.device import DevicePool

def pytest_addoption(parser):
    parser.addoption(
        '--config',
        action='store',
        default='config.yaml',
        help='Config File Path'
    )

@pytest.fixture(scope='session')
def device_pool(request):
    config_file = request.config.getoption('--config')
    return DevicePool(config_file)

@pytest.fixture(scope='function')
def dev(device_pool):
    dev = device_pool.get()
    yield dev
    device_pool.put(dev)