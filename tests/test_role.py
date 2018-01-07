import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize('command', [
    'docker version'
])
def test_java_tools(Command, command):
    cmd = Command('. /etc/profile && ' + command)
    assert cmd.rc == 0
