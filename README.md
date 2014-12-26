graphite_api
============

Role which installs graphite-api from RPM packages. It supports Carbon and
InfluxDB as the storage backend.


Example
-------

```
---

# Example how to use the role
- hosts: myhost
  roles:
    - graphite-api
```


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

* [`carbon`](https://github.com/picotrading/ansible-carbon) role


License
-------

MIT


Author
------

Author Name
