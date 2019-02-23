import random
from random import randint, randrange
import os, time, string, sys
from time import sleep

os.system("clear")

def textByFrame(str):
	i = 0
	while i < len(str):
		sleep(0.01)
		sys.stdout.write(str[i])
		sys.stdout.flush()
		i += 1


textByFrame("\033[1;31m------------------ \033[1;37mTool for scanning giftcards with balances \033[1;31m------------------\n") #####
textByFrame("\033[1;31m------------------------- \033[1;37mWriten by: \033[1;36mNuclearFallout \033[1;31m---------------------------\n")
textByFrame("\033[1;37m-------------------------------------------------------------------------------\n")
textByFrame("\033[1;31m---------------------------- \033[1;37mStarting Card Scanner! \033[1;31m---------------------------\n")
textByFrame("\033[1;31m------------------ \033[1;37mScanning starting, all findings outputted\033[1;31m ------------------\n")
textByFrame("\033[1;37m-------------------------------------------------------------------------------\n")
textByFrame("\033[1;31m------------------------ \033[1;37mTitle is findings this session \033[1;31m-----------------------\n")
textByFrame("\033[1;37m-------------------------------------------------------------------------------\n")
textByFrame("\033[1;31m----------------------------- \033[1;37mFindings are below \033[1;31m------------------------------\n")
textByFrame("\033[1;37m-------------------------------------------------------------------------------\n")


amazonF = 0
googleF = 0
xboxF = 0
psnF = 0
itunesF = 0
youtubeF = 0

while True:
	cardMoney = ''.join(["%s" % randint(1, 9) for num in range(1)])
	cardPin = ''.join(["%s" % randint(1, 9) for num in range(6)])
	cardCent = ''.join(["%s" % randint(1, 9) for nummm in range(0, 2)])
	cardNumber = ''.join(["%s" % randint(1, 9) for nummmm in range(20)])
	cardChoice = randrange(1, 10)
	accType = 	randrange(1, 7)
	cardCash = cardMoney + "." + cardCent
	time.sleep(0.6)
	if cardChoice > 7:
		print("\033[1;31m[\033[1;37mDetails\033[1;31m] -> (\033[1;36m%s\033[1;31m) - [\033[1;37mBalance\033[1;31m] -> (\033[1;32m$0\033[1;31m)" % (cardNumber))
	if cardChoice < 7:
		if accType == 1:
			accData = 'Amazon'
			amazonF += 1
			os.system("echo '[%s : %s] -> [$%s]' >> reports/amazon.txt" % (cardNumber, cardPin, cardCash))
		if accType == 2:
			accData = 'Google'
			googleF += 1
			os.system("echo '[%s : %s] -> [$%s]' >> reports/google.txt" % (cardNumber, cardPin, cardCash))
		if accType == 3:
			xboxF += 1
			accData = 'Xbox'
			os.system("echo '[%s : %s] -> [$%s]' >> reports/xbox.txt" % (cardNumber, cardPin, cardCash))
		if accType == 4:
			psnF += 1
			accData = 'PSN'
			os.system("echo '[%s : %s] -> [$%s]' >> reports/psn.txt" % (cardNumber, cardPin, cardCash))
		if accType == 5:
			accData = 'iTunes'
			itunesF += 1
			os.system("echo '[%s : %s] -> [$%s]' >> reports/itunes.txt" % (cardNumber, cardPin, cardCash))
		if accType == 6:
			accData = 'Youtube'	
			youtubeF += 1	
			os.system("echo '[%s : %s] -> [$%s]' >> reports/youtube.txt" % (cardNumber, cardPin, cardCash))
		sys.stdout.write(b'\33]0;Amazon[%d] - Google[%d] - Xbox[%s] - PSN[%s] - iTunes[%d] - Youtube[%d]\a' % (amazonF, googleF, xboxF, psnF, itunesF, youtubeF))
		sys.stdout.flush()
		print("\033[1;31m[\033[1;37mDetails\033[1;31m] -> (\033[1;36m%s \033[1;37m: \033[1;36m%s\033[1;31m - \033[1;36m%s\033[1;31m) - [\033[1;37mBalance\033[1;31m] -> (\033[1;32m$%s\033[1;31m)" % (cardNumber, cardPin, accData, cardCash))
