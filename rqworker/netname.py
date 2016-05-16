import subprocess


def analysis(line, result):
    # whois
    inetnum_ = subprocess.Popen("whois {}".format(line),
                                shell=True, stdout=subprocess.PIPE)
    output = inetnum_.communicate()
    # change to string and split
    result[line] = str(output).split('\\n')
    return result[line]


def write_file(result, target):

    if 'inetnum' in result[5]:
        for i in range(5, 11):
            target.write(result[i])
            target.write("\n")
        target.write("------------------------------------------"
                     "----------------------------------------\n")
