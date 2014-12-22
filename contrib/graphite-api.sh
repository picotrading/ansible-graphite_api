#!/bin/bash

# Name of the project
NAME=graphite-api

# PID file location
PIDFILE=/var/run/${NAME}.pid

# Return value
RETVAL=0

# Read default params
if [ -e /etc/default/${NAME} ]; then
        source /etc/default/${NAME}
fi

function start() {
    if [ -e $PIDFILE ]; then
        echo "ERROR: PID file exists"
        RETVAL=1
        return
    fi

    # Start the server on background
    gunicorn graphite_api.app:app -b ${BIND_ADDRESS:-127.0.0.1}:${PORT:-8888} $GUNICORN_OPTIONS 1>/var/log/$NAME.log 2>&1 &

    echo $! > $PIDFILE
}


function stop() {
    # Kill the main process and its child
    (kill -- $(ps -o pid,ppid --no-heading --ppid $(cat $PIDFILE))) 2>/dev/null || echo "ERROR: Nothing to kill"

    # Remove the PID file
    rm -f $PIDFILE
}


PARAM=$1
echo "Action: $PARAM"

case $PARAM in
    'start')
        start
        shift
        ;;
    'stop')
        stop
        shift
        ;;
    *)
        echo "ERROR: Unknown action: $PARAM"
        shift
        ;;
esac

exit $RETVAL
