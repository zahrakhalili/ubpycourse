import os
import sys

a=[]

for i in sys.argv[1:]:
	a.append(i)

for item in a:
	os.system('potrace -b svg -b pdf {0} -o {1}.pdf'.format(item, item[:-4]))
