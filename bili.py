import sys

if(len(sys.argv) < 2):
    sys.exit()

for a in sys.argv:
	if(a != sys.argv[0]):
		filePath = a

		pfile = open(filePath ,'rb')
		pfile.seek(3)
		byte = pfile.read()
		pfile.close()

		pfile = open(filePath ,'wb')
		pfile.seek(0)
		pfile.write(byte)
		pfile.close()

print('success')
