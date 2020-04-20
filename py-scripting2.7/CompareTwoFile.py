file1list = []
file2list = []
with open('/Users/athakur/Desktop/PythonScript/Ak.txt', 'r') as file1:
    for f1 in file1.readlines():
        f = f1.split(' ')
        file1list.extend(f)
with open('/Users/athakur/Desktop/PythonScript/at.txt', 'r') as file2:
    for f2 in file2.readlines():
        f2 = f2.split(' ')
        file2list.extend(f2)

same = set(file1list).difference(file2list)
print same
# same.discard('\n')
with open('/Users/athakur/Desktop/PythonScript/Out.txt', 'w') as output:
    for i in same:
        output.write(i + '\n')
