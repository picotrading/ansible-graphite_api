graphite_api
============

Role which installs graphite-api from RPM packages.


Example
-------

```
---

# Default installation requires carbon/whisper storage
- hosts: myhost1
  roles:
    - carbon
    - graphite-api

# Example how to customize the default configuration
- hosts: myhost2
  roles:
    - carbon
    - role: graphite_api
      graphite_api_config:
      graphite_api_timezone: Europe/London
      graphite_api_cors_hosts: 192.168.56.105

# Example re-define all configuration
- hosts: myhost3
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


Role variables
--------------

List of variables used by the role:

```
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


License
-------

MIT


Author
------

Jiri Tyr
