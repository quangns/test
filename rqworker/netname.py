from ipwhois import IPWhois


def analysis(line):
    target = open("netname.txt", 'a')
    obj = IPWhois(line)
    res = obj.lookup_whois()
    result = res['nets'][0]
    if 'range' in result:
        if "\n" in result['description']:
            descrip = result['description'].split('\n')
            target.write("description:  %s %s\n" % (descrip[0], descrip[-1]))
        else:
            target.write("description:  %s %s\n" % (result['description']))
        target.write("inetnum:      %s\n" % (result['range']))
        target.write("netname:      %s\n" % (result['name']))
        target.write("cidr:         %s\n" % (result['cidr']))
        target.write("------------------------------------------"
                     "----------------------------------------\n")
    target.close()