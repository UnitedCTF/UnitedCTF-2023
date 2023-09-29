#!/bin/bash
/etc/init.d/mariadb start
mysql -sfu root < /root/entrypoint-init.d/sql/mysql_secure_installation.sql
mysql -sfu root < /root/entrypoint-init.d/sql/init.sql
/etc/init.d/mariadb restart
