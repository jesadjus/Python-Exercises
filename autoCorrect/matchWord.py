''' this file is for testing purposes '''

def matchWord( word ):
	for line in dictionary:
		if ( line[0:-1].lower() ) == word.lower() : # convert user input to all lower case to check
			return word.lower()
	return 0
	
word = raw_input('> ')
dictionary = open('wordlist.txt', 'r')
match = matchWord( word )
if( match != 0 ):
	print word
print match