Ansible Role: docker
========================


Role to install the [docker](https://docker.io) container engin (CE).

Requirements
------------

* Ansible >= 2.0

* Linux Distribution

    * Debian Family

        * Ubuntu

            * Xenial (16.04)

Role Variables
--------------

### `docker_version`

Specify the version of docker.
Default value: '17.03.2~ce-0~ubuntu-xenial'

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: fawaz-moh.docker
```

License
-------

MIT

Author Information
------------------

Fawaz Mohammed
fawaz.moh.ibraheem@gmail.com
