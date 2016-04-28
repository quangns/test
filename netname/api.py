import socket, struct
from intervaltree import Interval, IntervalTree
import re

# Chuyen tu ip ve dang int
def change_ip(ip_addr):
    numberId = struct.unpack("!L", socket.inet_aton(ip_addr))[0]
    return numberId


def length_file(file_input):
    length = open(file_input).read().count("\n") + 1
    t = IntervalTree()
    with open(file_input) as file_:
        for line in file_:
            # tim kiem dong co chu inetnum va netname
            if re.search("inetnum", line):
                inetnum = line.split(' - ')
                print inetnum
                begin_ = change_ip(inetnum[-1])
                line1 = inetnum[0].split('        ')
                end_ = change_ip(line1[-1])
            if re.search("netname", line):
                data_ = line.split('        ')[-1]
                print begin_,end_,data_
                t.addi({} , {}, {}).format(begin_, end_, data_)

            #print sorted(t[20447231])


if __name__ == "__main__":
    # print "nhap vao mot ip  "
    # ip_addr = raw_input()
    file_input = 'netname.txt'
    # change_ip(ip_addr)
    length_file(file_input)