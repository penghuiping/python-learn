import os

basePath = "/Users/penghuiping/"

file = os.popen("ls -al {}".format(basePath))

result = file.readlines()

for r in result:
    print(r)
