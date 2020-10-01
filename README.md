#DirHunter
Dir-Hunter is an open-source simple and amazing tools for checking availabality website directory by brute-forcing, made by Clavin June,

before using dir-hunter you must have "python-requests" library
Dir-Hunter speed depends on your connection speed,

contact me at : cjuneardo@gmail.com

Dir-Hunter Lite : "python dirhunter_lite.py (website) [--start (number)] [--end (number)]"

	<website>		: must be starts with "http://" or "https://"
	--start <number>	: start brute-force from <number>, default 1
	--end <number>		: start brute-force until <number>, default 10

	example :
		python dirhunter_lite.py http://localhost
		[+] starts from a - zzzzzzzzzz
		python dirhunter_lite.py http://localhost --start 2
		[+] starts from aa - zzzzzzzzzz
		python dirhunter_lite.py http://localhost --end 3
		[+] starts from a - zzz
		python dirhunter_lite.py http://localhost --start 2 --end 4
		[+] starts from aa - zzzz

Dir-Hunter : "python dirhunter.py [--start (number)] [--end (number)] [--out (filename)]"

	--start <number>	: start brute-force from <number>, default 1
	--end <number>		: start brute-force until <number>, default 10
	--out <filename>	: making an output file named <filename> in dirhunter directory, default "result.txt"

	example :
		python dirhunter.py
		[+] starts from a - zzzzzzzzzz, output result.txt
		python dirhunter.py --start 2
		[+] starts from aa - zzzzzzzzzz, output result.txt
		python dirhunter.py --end 3
		[+] starts from a - zzz, output result.txt
		python dirhunter.py --out directory.txt
		[+] starts from a - zzzzzzzzzz, output directory.txt
		python dirhunter.py --start 2 --end 4 --out a.txt
		[+] starts from aa - zzzz, output a.txt
