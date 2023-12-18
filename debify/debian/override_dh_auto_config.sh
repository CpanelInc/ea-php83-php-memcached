#!/bin/bash

source debian/vars.sh

set -x

/opt/cpanel/ea-php83/root/usr/bin/phpize

./configure \
    --with-php-config=/opt/cpanel/ea-php83/root/usr/bin/php-config \
    --with-libdir=lib64

make
cd ..

