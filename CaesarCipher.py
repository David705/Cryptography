import sys

def encode(plaintext, key):
	ciphertext = ''
	for c in plaintext:
		if 65 <= ord(c) <= 90:
			ciphertext = ciphertext + chr(((ord(c)-65+key) % 26) + 65)
		elif 97 <= ord(c) <= 122:
			ciphertext = ciphertext + chr(((ord(c)-97+key) % 26) + 97)
		else:
			ciphertext = ciphertext + c
	print
	print 'Key: %d' % key
	print 'Given Plaintext:     %s' % (plaintext)
	print 'Produced Ciphertext: %s' % (ciphertext)

def decode(ciphertext, key):
	plaintext = ''
	for c in ciphertext:
		if 65 <= ord(c) <= 90:
			plaintext = plaintext + chr(((ord(c)-65-key) % 26) + 65)
		elif 97 <= ord(c) <= 122:
			plaintext = plaintext + chr(((ord(c)-97-key) % 26) + 97)
		else:
			plaintext = plaintext + c
	print
	print 'Key: %d' % key
	print 'Given Ciphertext:    %s' % (ciphertext)
	print 'Produced Plaintext:  %s' % (plaintext)

def usage():
	print 
	print 'Usage:'
	print '    python CaesarCipher.py [options]'
	print 'Examples:'
	print '    python CaesarCipher.py -k 10 -e "hello world" -d "rovvy gybvn"'
	print '    python CaesarCipher.py -e "a" -k 25 -d "z" -e "abc" -k 8 -e "yes"'
	print 'Options:'
	print '    -h'
	print '        Display available options'
	print '    -k <key>'
	print '        Key is a number between 1 and 25 inclusive'
	print '        Key is the number of characters to shift the alphabet by'
	print '        If no Key is provided, a default of 1 is used'
	print '    -e "<plaintext>"'
	print '        Encode provided plaintext'
	print '    -d "<ciphertext>"'
	print '        Decode provided ciphertext'

def main():
	key = 1
	index = 1
	numArguments = len(sys.argv)
	while index < numArguments:
		if sys.argv[index] == '-h':
			usage()
			break
		elif sys.argv[index] == '-k':
			try:
				try:
					tmpKey = int(sys.argv[index+1])
				except:
					print
					print '[-] No argument was given for %s' % (sys.argv[index])
					break
				if 1 <= tmpKey <= 25:
					key = tmpKey
				else:
					print 
					print '[-] Invalid Key %d' % tmpKey
					break
			except:
				print 
				print '[-] Invalid Key %s' % sys.argv[index+1]
				break
			index = index + 1
		elif sys.argv[index] == '-e':
			try:
				encode(sys.argv[index+1], key)
			except:
				print
				print '[-] No argument was given for %s' % (sys.argv[index])
				break
			index = index + 1
		elif sys.argv[index] == '-d':
			try:
				decode(sys.argv[index+1], key)
			except:
				print
				print '[-] No argument was given for %s' % (sys.argv[index])
				break
			index = index + 1
		index = index + 1
	print

if __name__ == '__main__':
	main()