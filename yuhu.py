import os, sys

print ("\033[1;33m")
Username = 'MrOyek'
Password = 'GuaGansThx'

def restart():
	relog = sys.executable
	os.execl(relog, relog, *sys.argv)

def main():
	uname = raw_input("#Username : ")
	if uname == Username:
		pwd = raw_input("#Password : ")

		if pwd == Password:
			print "\n\033[1;34mWelcome Brother :) ", 
			sys.exit()
     
		else:
			print "\n\033[1;36mWrong Password !!!\033[00m"
			print "Trying Login...!!!\n"
			restart()

	else:
		print "\n\033[1;36m Wrong Username or Password !!!\033[00m"
		print "Trying Login...!!!\n"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()
