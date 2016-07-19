#!/bin/bash
echo 'install oracle-java8'
sudo add-apt-repository -y ppa:webupd8team/java
sudo apt-get -y update
sudo apt-get -y install oracle-java8-installer > /dev/null 2>&1
echo 'install mesos and marathon'
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E56151BF
DISTRO=$(lsb_release -is | tr '[:upper:]' '[:lower:]')
CODENAME=$(lsb_release -cs)
echo "deb http://repos.mesosphere.com/${DISTRO} ${CODENAME} main" | \
  sudo tee /etc/apt/sources.list.d/mesosphere.list
sudo apt-get -y update
sudo apt-get -y install mesos marathon
echo 'config zookeeper'
get_ip=$(ifconfig eth1 | grep "inet addr" | cut -d ':' -f 2 | cut -d ' ' -f 1)
config="dataDir=/var/lib/zookeeper
clientPort=2181
tickTime=2000
initLimit=5
syncLimit=2
server.1="$get_ip":2888:3888"
echo -e "$config" | sudo tee /etc/zookeeper/conf/zoo.cfg
sudo service zookeeper restart
echo 'config mesos'
echo zk://"$get_ip":2181/mesos | sudo tee /etc/mesos/zk
echo 1 | sudo tee /etc/mesos-master/quorum
sudo service mesos-slave stop
sudo sh -c "echo manual > /etc/init/mesos-slave.override"
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
sudo service mesos-master restart
