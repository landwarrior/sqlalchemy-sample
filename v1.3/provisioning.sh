#!/usr/bin/env bash

set -e

# sudo su
# で root ユーザになってから実行する

dnf install -y mysql-server

systemctl enable mysqld
systemctl start mysqld

mysql -e "create user root@'%' identified by 'root'"
mysql -e "grant all privileges on *.* to root@'%' with grant option"
mysql -e "set password for root@localhost = 'root'"
mysql -uroot -proot -e "create database testdb default charset utf8mb4 COLLATE utf8mb4_bin"

dnf install -y python3.11 python3.11-pip python3.11-devel
dnf groupinstall -y "Development Tools"
