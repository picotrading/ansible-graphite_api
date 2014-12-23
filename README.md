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
# CORS (Cross-Origin Resource Sharing) is disabled by default
graphite_api_cors: false

# Default CORS hosts
graphite_api_cors_hosts: '*'

# Default timezone
graphite_api_timezone: UTC

# Default bind address
graphite_api_bind_address: 0.0.0.0

# Default port number
graphite_api_port: 8888

# Additional gunicorn command line options
graphite_api_gunicorn_options: ''
```


Dependencies
------------

* [`carbon`](https://github.com/picotrading/ansible-carbon) role


License
-------

License name


Author
------

Author Name
