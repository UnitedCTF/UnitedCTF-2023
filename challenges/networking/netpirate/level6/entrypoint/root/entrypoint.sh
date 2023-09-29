#!/bin/bash
# Please dont kill me.. or you will lose your session
trap "exit" SIGTERM

# and it is useless to run me unless your are init
if [ "$$" -ne 1 ]; then
  exit 0
fi

# Configure the interface eth0 to use DHCP 
cat > /etc/network/interfaces <<INTERFACES
auto lo
iface lo inet loopback

iface eth0 inet dhcp
INTERFACES

# Patch and configure dhclient to work with docker
mkdir -p /etc/dhcp
cat > /etc/dhcp/dhclient.conf <<DHCLIENT_CONF
script "/etc/dhclient-script";
send host-name "entrypoint";
DHCLIENT_CONF
sed -i 's/mv -f "\${src}" "\${dst}"/cat "\${src}" > "\${dst}" \&\& rm -f "\${src}"/g' /etc/dhclient-script

# Remove the IP given by docker
ifconfig eth0 0.0.0.0

# And use the one provided by the DHCP server
dhclient -4 -i \
  -pf /run/dhclient.eth0.pid \
  -lf /var/lib/dhcp/dhclient.eth0.leases \
  eth0

while :; do
  sleep 300 &
  wait "$!"

  if [ "$(ps -o pid | wc -l)" -eq 6 ]; then
    exit 99
  fi
done
