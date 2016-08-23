#!/bin/bash
echo 'install oracle-java8'
sudo add-apt-repository -y ppa:webupd8team/java
sudo apt-get -y update
sudo apt-get -y install oracle-java8-installer > /dev/null 2>&1

