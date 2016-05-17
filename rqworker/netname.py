import subprocess


def analysis(line):
    target = open("netname.txt", 'a')
    inetnum_ = subprocess.Popen("whois {}".format(line),
                                shell=True, stdout=subprocess.PIPE)
    output = inetnum_.communicate()
    result = str(output).split('\\n')
    if 'inetnum' in result[5]:
        for i in range(5, 11):
            target.write(result[i])
            target.write("\n")
        target.write("------------------------------------------"
                     "----------------------------------------\n")
    target.close()
