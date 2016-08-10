#!/bin/bash
echo 'install mesos'
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E56151BF
DISTRO=$(lsb_release -is | tr '[:upper:]' '[:lower:]')
CODENAME=$(lsb_release -cs)
echo "deb http://repos.mesosphere.com/${DISTRO} ${CODENAME} main" | \
  sudo tee /etc/apt/sources.list.d/mesosphere.list
sudo apt-get -y update
sudo apt-get -y install mesos
get_ip=$(ifconfig eth1 | grep "inet addr" | cut -d ':' -f 2 | cut -d ' ' -f 1)
echo 'config mesos'
sudo service zookeeper stop
sudo sh -c "echo manual > /etc/init/zookeeper.override"
echo zk://192.168.33.10:2181/mesos | sudo tee /etc/mesos/zk
sudo service mesos-master stop
sudo sh -c "echo manual > /etc/init/mesos-master.override"
host="127.0.0.1 localhost

# The following lines are desirable for IPv6 capable hosts
::1 ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
ff02::3 ip6-allhosts
"$get_ip" $(hostname)"
echo -e "$host" | sudo tee /etc/hosts

sudo service mesos-slave restart

