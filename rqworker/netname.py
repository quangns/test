from ipwhois import IPWhois
from netaddr import *


# tim cac subnet co the co
def find_subnet(ip, cidr):
    subnets = list(ip.subnet(cidr))
    length = len(subnets)
    # tranh whois subnets[0] them 1 lan nua
    for i in range(length):
        if i == length:
            break
        else:
            analysis(subnets[i+1])


# kiem tra xem dai ip da co trong ban ghi chua
def check(value):
    with open("netname.txt") as file_:
        for line in file_:
            if value in line:
                return False
    return True


def analysis(ip):
    target = open("netname.txt", 'a')
    obj = IPWhois(ip.network)
    res = obj.lookup_whois()
    result = res['nets'][0]
    # kiem tra inetnum co trong ban ghi khong
    if 'range' in result:
        if check(result['range']):
            if "\n" in result['description']:
                description_ = result['description'].split('\n')
                target.write("description:  %s %s\n" % (description_[0], description_[-1]))
            else:
                target.write("description:  %s\n" % (result['description']))
            target.write("inetnum:      %s\n" % (result['range']))
            target.write("netname:      %s\n" % (result['name']))
            target.write("cidr:         %s\n" % (result['cidr']))
            target.write("------------------------------------------"
                         "----------------------------------------\n")
            return result['cidr'].split('/')[-1]
    target.close()


def main_(line):
    ip = IPNetwork(line)
    cidr = analysis(ip)
    find_subnet(ip, int(cidr))
