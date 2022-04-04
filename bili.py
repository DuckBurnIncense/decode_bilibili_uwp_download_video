import sys

if(len(sys.argv) != 2):
    exit()

filePath = sys.argv[1]

pfile = open(filePath ,'rb')
pfile.seek(3)
byte = pfile.read()
pfile.close()

pfile = open(filePath ,'wb')
pfile.seek(0)
pfile.write(byte)
pfile.close()

print('success')
