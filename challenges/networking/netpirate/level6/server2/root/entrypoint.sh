#!/bin/ash
trap "exit" SIGTERM

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
send host-name "server2";
DHCLIENT_CONF
sed -i 's/mv -f "\${src}" "\${dst}"/cat "\${src}" > "\${dst}" \&\& rm -f "\${src}"/g' /etc/dhclient-script

# Remove the IP given by docker
ifconfig eth0 0.0.0.0

exec /entrypoint.py
