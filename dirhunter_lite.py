#Library
from string import ascii_lowercase
import itertools, os, sys, requests

#pre-defined variable
arg_start=1
arg_end=10
directory=""
url= str(sys.argv[1])

#checking argument
try:
	if "--start" in sys.argv[2]:
		arg_start = int(sys.argv[3])
	if "--end" in sys.argv[2]:
		arg_end = int(sys.argv[3])


	if "--start" in sys.argv[4]:
		arg_start = int(sys.argv[5])
	if "--end" in sys.argv[4]:
		arg_end = int(sys.argv[5])
except:
	print ""

#checking directory length
if arg_start > arg_end:
	arg_end = arg_start+2

#bruteforce
def iter_all_strings():
	size = arg_start
	while size <= arg_end:
		for directory in itertools.product(ascii_lowercase, repeat=size):
        		yield "".join(directory)
		size +=1

#main program
while True:
	try:
		response = requests.get(url)
		response_code = response.status_code
		if response_code == 200: 
			for directory in iter_all_strings():
				link = url+"/"+directory
				if requests.get(link).status_code == 200:
					print " [*] "+link+" "+'\033[92m'+'\033[1m'+"FOUND"+'\033[0m'
		else:
			print ""
	except:
		print ""
	print "End of Bruteforce in '"+ directory+"'"
	break