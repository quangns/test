import subprocess


def analysis(line):
    # whois
    result = {}
    inetnum_ = subprocess.Popen("whois {}".format(line),
                                shell=True, stdout=subprocess.PIPE)
    output = inetnum_.communicate()
    # change to string and split
    result[line] = str(output).split('\\n')
    return result[line]


def write_file():
    target = open("netname.txt", 'w')
    with open("/opt/ip") as file_:
        for line in file_:
            a = analysis(line)
            if 'inetnum' in a[5]:
                for i in range(5, 11):
                    target.write(a[i])
                    target.write("\n")
                target.write("------------------------------------------"
                             "----------------------------------------\n")
    target.close()