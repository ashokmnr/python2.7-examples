#!/usr/bin/python2.7


def get_file_name(reprompt=False):
    if reprompt:
        print("Please enter a file name.")

    file_name = raw_input("Destination file name: ").strip()
    return file_name or get_file_name(True)


file_name = get_file_name()

print("Please enter your content. Entering an empty line will write the content to %s:\n" % file_name)

with open(file_name, "w") as f:
    con = False
    lines = []

    while not con:
        line = raw_input()
        if line.strip():
            lines.append("%s\n" % line)
        else:
            con = True

    f.writelines(lines)
    print("Lines written to %s" % file_name)
