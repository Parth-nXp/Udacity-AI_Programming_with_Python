'''
Write a function called generate_password that selects three random words from the list of words word_list and concatenates them into a single string. 
Your function should not accept any arguments and should reference the global variable word_list to build the password.
'''

# Use an import statement at the top
import random
word_file = "03_Introduction_to_Python/01_05_Scripting/21_Quiz_The_Standard_Library/words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and list_of_words
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password(list_of_words):
	password = ""
	for each_word in range(3):
		password = password + random.choice(list_of_words)

##def generate_password():
##    return ''.join(random.sample(word_list,3))

	return password

# test your function
print(generate_password(word_list))