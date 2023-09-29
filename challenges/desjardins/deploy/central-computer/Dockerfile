# syntax=docker/dockerfile:1
FROM alpine:edge

RUN apk update \
    && apk add --no-cache sudo bash openrc openssh-server python3 py3-requests vim nano mariadb mariadb-client nginx php82-fpm php82-mysqli openssl acl \
    && mkdir -p /run/openrc \
    && touch /run/openrc/softlevel

RUN rc-update add sshd \
    && adduser -D -g 'www' www \
    && mkdir /www \
    && chmod 750 /www \
    && chown -R root:www /var/lib/nginx \
    && chown -R root:www /var/log/nginx

ADD root /
RUN adduser -D moussaillon moussaillon \
    && printf 'moussaillon:moussaillon' | chpasswd \
    && touch /home/moussaillon/.ash_history \
    && touch /home/moussaillon/.viminfo \
    && touch /home/moussaillon/.mysql_history \
    && /etc/init.d/mariadb setup \
    && sed -iE 's/command_args="/command_args="--user=www /' /etc/init.d/mariadb \
    && chown -R www:www /var/lib/mysql \
    && chown -R www:www /www \
    && chmod 750 /etc/ssh \
    && chmod -R 600 /etc/ssh/* \
    && chown -R root:root /etc/ssh \
    && printf "capitaine:%s\n" $(printf "YFuKU73zaxyTTHaEpW3KTAqYrYi4JWyjr9WMPKqs\n" | openssl passwd -stdin -apr1) >> /etc/nginx/.htpasswd \
    && printf "moussaillon:%s\n" $(printf "FLAG-UnSecretEnArgument\n" | openssl passwd -stdin -apr1) >> /etc/nginx/.htpasswd \
    && sed -iE 's/user = nobody/user = www/' /etc/php82/php-fpm.d/www.conf \
    && sed -iE 's/group = nobody/group = www/' /etc/php82/php-fpm.d/www.conf \
    && chmod -R 750 /root \
    && setfacl --recursive -m u:moussaillon:000 /www

# fix problèmes rapportés par fob le 22 septembre
RUN ln -sf /dev/null /home/moussaillon/.python_history \
    && ln -sf /dev/null /home/moussaillon/.viminfo \
    && ln -sf /dev/null /home/moussaillon/.ash_history \
    && ln -sf /dev/null /home/moussaillon/.mysql_history \
    && chown root:root /home/moussaillon/who-is-the-captain.py \
    && chmod 755 /home/moussaillon/who-is-the-captain.py \
    && chown root:moussaillon /home/moussaillon \
    && ln -sf /dev/null /var/log/nginx/error.log

ENTRYPOINT ["/root/entrypoint.sh"]
