#!/bin/bash

# Add local user
# Either use the LOCAL_USER_ID if passed in at runtime or
# fallback

# USER_ID=${LOCAL_USER_ID:-9001}
#
# echo "Starting with UID : $USER_ID"
# useradd --shell /bin/bash -u $USER_ID -o -c "" -m user

set -e

echo "---- Start docker-entrypoint.sh ----"

UID_DATA=$(stat -c "%u" data/)
UID_LOG=$(stat -c "%u" log/)

echo "UID_DATA: $UID_DATA"
echo "UID_LOG : $UID_LOG"

if [ "$UID_DATA" = "$UID_LOG" ]; then
  echo "Starting with UID : $UID_DATA"
  useradd --shell /bin/bash -u $UID_DATA -o -c "" -m user
  echo "ls -la:"
  ls -la
  echo "---- End docker-entrypoint.sh ------"
  exec gosu user "$@"
else
  echo "Owner UID of docker folders /mosquitto/data and /mosquitto/log are not equal."
  echo "Cannot run container as 1 unique user."
  echo "---- End docker-entrypoint.sh ------"
fi
