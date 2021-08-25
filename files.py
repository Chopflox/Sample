hosts = open(r"C:\Users\eburkan\Desktop\SampleGit\hello.txt")

print(hosts.read(3))

print(hosts.tell())

with open(r"C:\Users\eburkan\Desktop\SampleGit\hello.txt") as the_file:

    for line in the_file:
        print(line)

with open(r"C:\Users\eburkan\Desktop\SampleGit\hello.txt") as hosts:
    print('File closed? {}'.format(hosts.closed))
    print(hosts.read())



with open(r"C:\Users\eburkan\Desktop\SampleGit\hello.txt") as the_file:

    for line in the_file:
        print(line)
    
with open(r"C:\Users\eburkan\Desktop\SampleGit\hello.txt") as the_file:    
    the_file.write('tester nå.\n')
    the_file.write('hoohhoho.\n')