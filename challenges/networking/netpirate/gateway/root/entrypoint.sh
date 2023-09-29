#!/bin/ash

if [ -d "/entrypoint.d" ]; then
  for SCRIPT in $(find /entrypoint.d -type f | sort); do
    if [ -x "$SCRIPT" ]; then
      SCRIPT_NAME="${SCRIPT##*/}"

      echo "info: executing $SCRIPT_NAME"
      "$SCRIPT" "$@"
  
      ECODE="$?"
      if [ "$ECODE" -ne 0 ]; then
        echo "error: script '$SCRIPT_NAME' non-zero exit code '$ECODE'"
        exit "$ECODE"
      fi
    fi
  done
fi

SSHD_PID=0
cleanup() {
  echo "info: signal caught, terminating.."

  # Stop incoming SSH connections
  if [ "$SSHD_PID" -ne 0 ]; then
    echo "info: stopped SSH server"
    kill -SIGSTOP "$SSHD_PID"
  fi

  # Remove all levels
  for SESSION_ID in $(find /tmp/sessions -mindepth 1 -maxdepth 1 -type f -exec basename "{}" \; | sort -V); do
    echo "info: cleaning up session '$SESSION_ID' .."
    LEVEL_NAME=$(echo -n "$SESSION_ID" | cut -d "-" -f1)
    (
      cd "/levels/$LEVEL_NAME"
      docker compose -p "$SESSION_ID" down -v -t0 &>/dev/null
    )
    rm "/tmp/sessions/$SESSION_ID"
  done

  exit 0
}

trap cleanup SIGTERM

echo "info: SSH server is up!"
while :; do
  /usr/sbin/sshd -D \
    -o "Subsystem=sftp /bin/false" \
    -o PasswordAuthentication=yes \
    -o GatewayPorts=no \
    -o PermitTunnel=no \
    -o X11Forwarding=no \
    -o AllowTcpForwarding=no \
    -o AllowAgentForwarding=no \
    -o Port=${PORT:-22} \
    "$@" &
  SSHD_PID="$!"
  wait "$SSHD_PID"
done
