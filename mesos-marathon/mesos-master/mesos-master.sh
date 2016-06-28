#!/bin/bash
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E56151BF
DISTRO=$(lsb_release -is | tr '[:upper:]' '[:lower:]')
CODENAME=$(lsb_release -cs)
echo "deb http://repos.mesosphere.com/${DISTRO} ${CODENAME} main" | \
  sudo tee /etc/apt/sources.list.d/mesosphere.list
sudo add-apt-repository -y ppa:webupd8team/java
sudo apt-get -y update
sudo apt-get -y install oracle-java8-installer > /dev/null 2>&1
sudo apt-get -y install mesos marathon
cat > /etc/zookeeper/conf/zoo.cfg << EOL
dataDir=/var/lib/zookeeper
clientPort=2181
tickTime=2000
initLimit=5
syncLimit=2
server.1=192.168.33.10:2888:3888
EOL
sudo service zookeeper restart
echo zk://192.168.33.10/mesos | sudo tee /etc/mesos/zk
echo 1 | sudo tee /etc/mesos-master/quorum
sudo service mesos-slave stop
sudo sh -c "echo manual > /etc/init/mesos-slave.override"
sudo service mesos-master restart
