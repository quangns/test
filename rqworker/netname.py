import subprocess


def analysis(input_file):
    with open(input_file) as file_:
        target = open('netname.txt', 'w')
        for line in file_:
            inetnum_ = subprocess.Popen("whois {}".format(line),
                                        shell=True, stdout=subprocess.PIPE)
            output = inetnum_.communicate()
            a = str(output).split('\\n')
            if 'inetnum' in a[5]:
                for i in range(5, 11):
                    target.write(a[i])
                    target.write("\n")
                target.write("------------------------------------------"
                             "----------------------------------------\n")
        target.close()