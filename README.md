
An Ansible Role that installs Keycloak on RedHat/CentOS or Debian/Ubuntu.

[![Build Status](https://travis-ci.org/FlxPeters/ansible-role-keycloak.svg?branch=master)](https://travis-ci.org/FlxPeters/ansible-role-keycloak)

Requirements
------------

Requires at least Java 8. The role does NOT install Java. 

Todo
----
- [ ] Keycloak configuration and JDBC support
- [x] Tests with Tetinfra
- [ ] Tests with multiple plattforms
- [ ] Standalone-HA mode
- [ ] Domain mode

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: flxpeters.keycloak }

License
-------

MIT

Author Information
------------------

This role was created in 2018 by [Felix Peters](https://www.felixpeters.de/).