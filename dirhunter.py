#Library
from string import ascii_lowercase
import itertools, os, sys, time ,requests

#pre-defined variable
arg_start=1
arg_end=10
file_name="result.txt"
directory=""

#coloring
class color:
	VIOLET = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	NORMAL = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

#splash
def splash_screen():
	print color.GREEN + color.BOLD + "\t\t ____  _                _   _             _            "
	print "\t\t|  _ \(_)_ __          | | | |_   _ _ __ | |_ ___ _ __ "
	print "\t\t| | | | | '__|  _____  | |_| | | | | '_ \| __/ _ \ '__|"
	print "\t\t| |_| | | |    |_____| |  _  | |_| | | | | ||  __/ |   "
	print "\t\t|____/|_|_|            |_| |_|\__,_|_| |_|\__\___|_|   "
	print "                                                       " + color.NORMAL
	print "\t\t\t\t\t\t\t\t  "+color.BOLD+"By:"+color.UNDERLINE+"Clavin June"+color.NORMAL+color.RED
	print '-'*80
	print color.BLUE+'\t0x00 Input URL with "http://" or "https://"'
	print '\t0x01 Input URL without "/" behind'
	print '\t0x02 Input URL like this "http://localhost" or "https://facebook.com"'
	print '\t0x03 DO NOT input URL like this "localhost" or "facebook.com/"'
	print '\t0x04 Dir-Hunter speed depends on your connection speed'
	print '\t0x05 "CTRL + C" for reset || "CTRL + Z" for stop'
	print '\t0x06 HAPPY HUNTING'+color.NORMAL+color.RED
	print '-'*80

#checking argument
try:
	if "--start" in sys.argv[1]:
		arg_start = int(sys.argv[2])
	if "--end" in sys.argv[1]:
		arg_end = int(sys.argv[2])
	if "--out" in sys.argv[1]:
		file_name = str(sys.argv[2])


	if "--start" in sys.argv[3]:
		arg_start = int(sys.argv[4])
	if "--end" in sys.argv[3]:
		arg_end = int(sys.argv[4])
	if "--out" in sys.argv[3]:
		file_name = str(sys.argv[4])

	if "--start" in sys.argv[5]:
		arg_start = int(sys.argv[6])
	if "--end" in sys.argv[5]:
		arg_end = int(sys.argv[6])
	if "--out" in sys.argv[5]:
		file_name = str(sys.argv[6])
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
	os.system("clear")
	splash_screen()
	print color.NORMAL,
	try:
		url = raw_input('[+] Input URL --> ')
	except:
		print ""
	try:
		file=open(file_name,'w')
		response = requests.get(url)
		response_code = response.status_code

		if response_code == 200: 
			for directory in iter_all_strings():
				link = url+"/"+directory
				if requests.get(link).status_code == 200:
					print " [*] "+color.GREEN+link+" "+color.BOLD+"FOUND"+color.NORMAL
					file.write(link+"\n")
		else:
			print ""
	except:
		print ""

	print "End of Bruteforce in '"+ directory+"'"
	print "\n"+color.BOLD+color.GREEN+'directory has stored in '+file_name+color.NORMAL
	file.close()
	try:
		time.sleep(1)
		print "."
		time.sleep(1)
		print "."
		enter=raw_input()
	except:
		print ""