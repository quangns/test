```bash
Tao cac may ao, dat ip cua may master la 192.168.33.10
May ao cai mesos-slave thi chay file mesos-slave.sh
May ao cai mesos-master thi chay file mesos-master.sh
```

```bash
Trong file mesos-slave.sh, tai dong 14, chinh lai ip cua mesos-master
Vd:
    echo zk://[ip mesos-master]:2181/mesos | sudo tee /etc/mesos/zk
```

```bash
$ sudo chmod +x mesos-master.sh install_javas8.sh
$ ./install_java8.sh
# trong khi cai java8 co the no bi ngung 1 thoi gian, can an enter
$ ./mesos-master.sh
```

```bash
$ sudo chmod +x mesos-slave.sh
$ ./mesos-slave.sh
```
