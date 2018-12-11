import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_keycloak_user(host):
    u = host.user('keycloak')
    assert u.exists
    assert u.group == 'keycloak'


def test_keycloak_group(host):
    g = host.group('keycloak')
    assert g.exists


def test_keycloak_base_direcory_exists(host):
    f = host.file('/opt/keycloak')
    assert f.exists
    assert f.user == 'keycloak'
    assert f.group == 'keycloak'


def test_keycloak_current_symlink(host):
    f = host.file('/opt/keycloak/current')
    assert f.exists
    assert f.is_symlink


def test_keycloak_is_a_service(host):
    service = host.service('keycloak')
    assert service.is_running
    assert service.is_enabled


def test_keycloak_listen_on_8080(host):
    socket = host.socket('tcp://0.0.0.0:8080')
    socket.is_listening
