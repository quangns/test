from intervaltree import IntervalTree
import socket,struct

INTERVAL_TREE = IntervalTree()


def change_ip(ip_addr):
    numberId = struct.unpack("!L", socket.inet_aton(ip_addr))[0]
    return numberId


def analysis(file_input):
    with open(file_input) as file_:
        for line in file_:
            if "inetnum" in line:
                inetnum = line.split(' - ')
                ip_end = change_ip(inetnum[-1])
                end = inetnum[0].split(' ')
                ip_start = change_ip(end[-1])
            if "netname" in line:
                data_ = line.split(' ')[-1]
                INTERVAL_TREE[ip_start: ip_end] = data_


def get_netname(addr):
    if addr == '127.0.0.1' or addr == 'localhost':
        return 'localhost'
    else:
        analysis("netname.txt")
        ip = change_ip(addr)
        iv = sorted(INTERVAL_TREE[ip])
        print (iv[0]).data
