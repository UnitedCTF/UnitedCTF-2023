#!/bin/sh
# This script allows to block or unblock the level's internet access
# By default, this script blocks access to all interfaces starting with eth or enp
# We have to do it manually since its easier for testing and using an internal network blocks broadcast packets which are needed for some levels

if [ "$(id -u)" -ne 0 ]; then
  sudo -ku root "IFACES=$IFACES" "$0" "$@"
  exit $?
fi

# This matches all interfaces starting with eth or enp
if [ -z "$IFACES" ]; then
  IFACES="eth+,enp+"
fi

is_blocked() {
  while read IFACE; do
    iptables -C DOCKER-USER -i np-+ -o "$IFACE" -j DROP 2>/dev/null
    return $?
  done < <(echo "$IFACES" | sed 's/,/\n/g')
}

block() {
  while read IFACE; do
    iptables -I DOCKER-USER -i np-+ -o "$IFACE" -j DROP
  done < <(echo "$IFACES" | sed 's/,/\n/g')
}

unblock() {
  while read IFACE; do
    iptables -D DOCKER-USER -i np-+ -o "$IFACE" -j DROP
  done < <(echo "$IFACES" | sed 's/,/\n/g')
}

case "$1" in
  "status")
    if is_blocked; then
      echo -e "Level network access to '$IFACES' is \e[1;32mblocked\e[0m"
    else
      echo -e "Level network access to '$IFACES' is \e[1;31munblocked\e[0m"
    fi
  ;;
  "toggle")
    if is_blocked; then
      unblock
      echo -e "Level network access to '$IFACES' is now \e[1;31munblocked\e[0m"
    else
      block
      echo -e "Level network access to '$IFACES' is now \e[1;32mblocked\e[0m"
    fi
  ;;
  "enable")
    if is_blocked; then
      echo -e "Level network access to '$IFACES' is already \e[1;32mblocked\e[0m"
      exit 0
    fi
    block
    echo -e "Level network access to '$IFACES' is now \e[1;32mblocked\e[0m"
  ;;
  "disable")
    if ! is_blocked; then
      echo -e "Level network access to '$IFACES' is already \e[1;31munblocked\e[0m"
      exit 0
    fi
    unblock
    echo -e "Level network access to '$IFACES' is now \e[1;31munblocked\e[0m"
  ;;
  *)
    echo "$0 [status|toggle|enable|disable|help]"
  ;;
esac
