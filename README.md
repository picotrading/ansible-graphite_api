graphite_api
============

Role which installs graphite-api from RPM packages. You must build the RPM
packages and place them into a YUM repo (see
[`yumrepo`](https://github.com/picotrading/ansible-yumrepo) role).

The configuraton of the role is done in such way that it should not be necessary
to change the role for any kind of configuration. All can be done either by
changing role parameters or by declaring completely new configuration as a
variable. That makes this role absolutely universal. See the examples below for
more details.

Please report any issues or send PR.


Example
-------

```
---

# Default installation requires carbon/whisper storage
- hosts: myhost1
  roles:
    - carbon
    - graphite-api

# Example of how to customize the default gunicorn configuration
- hosts: myhost2
  vars:
    # Set number of workes based on number of processors
    # Set gevent worker class
    graphite_api_gunicorn_options: '-w {{ ansible_processor_count | int * 2 + 1 }} -k gevent'
    # Install the python-gevent package for the gevent worker class
    graphite_api_pkg_deps:
      - python-gevent
  roles:
    - carbon
    - graphite_api

# Example of how to customize the default configuration
- hosts: myhost3
  roles:
    - carbon
    - role: graphite_api
      graphite_api_config:
      graphite_api_timezone: Europe/London
      graphite_api_cors_hosts: 192.168.56.105

# Example re-define all configuration
- hosts: myhost4
  roles:
    - role: graphite_api
      graphite_api_config:
        search_index: /var/lib/graphite-api/index
        finders:
          - graphite_influxdb.InfluxdbFinder
        functions:
          - graphite_api.functions.SeriesFunctions
          - graphite_api.functions.PieFunctions
        cache:
          type: filesystem
          dir: /tmp/graphite-api-cache
        time_zone: "{{ graphite_api_timezone }}"
        allowed_origins:
          - "{{ graphite_api_cors_hosts }}"
        influxdb:
           host: influxdb_server
           port: 8086
           user: root
           pass: root
           db: graphite
           schema:
             - ['', 10]
             - ['high-res-metrics', 1]
```

See
[`graphite_api_influxdb`](https://github.com/picotrading/ansible-graphite_api_inflixdb)
role if you wish to use InfluxDB as the storage backend.

This role requires [Config Encoder
Macros](https://github.com/picotrading/config-encoder-macros) which must be
placed into the same directory as the playbook:

```
$ ls -1 *.yaml
site.yaml
$ git clone https://github.com/picotrading/config-encoder-macros.git ./templates/encoder
```


Role variables
--------------

List of variables used by the role:

```
# Packege to be installed (you can force a specific version here)
graphite_api_pkg: graphite-api

# Depending packages (e.g. python-gevent for gunicorn)
graphite_api_pkg_deps: []

# Default CORS (Cross-Origin Resource Sharing) hosts
graphite_api_cors_hosts: '*'

# Default timezone
graphite_api_timezone: UTC

# Default bind address
graphite_api_bind_address: 0.0.0.0

# Default port number
graphite_api_port: 8888

# Additional gunicorn command line options
graphite_api_gunicorn_options: ''

# Default graphite-api configuration
graphite_api_config:
  search_index: /var/lib/graphite-api/index
  finders:
    - graphite_api.finders.whisper.WhisperFinder
  functions:
    - graphite_api.functions.SeriesFunctions
    - graphite_api.functions.PieFunctions
  whisper:
    directories:
      - /var/lib/carbon/whisper
  time_zone: "{{ graphite_api_timezone }}"
  allowed_origins:
    - "{{ graphite_api_cors_hosts }}"
```


Dependencies
------------

* [`carbon`](https://github.com/picotrading/ansible-carbon) role (optional)
* [Config Encoder Macros](https://github.com/picotrading/config-encoder-macros)


License
-------

MIT


Author
------

Jiri Tyr
