
#palindrome test

word = '123321'
print ('length = ' + str(len(word)))
end = len(word)-1
for i in range (0,len(word)):
	print ('check {}: {} vs {}'.format(i,word[i],word[end-i]))
	if word[i] == word[end-i]:
		nextCheck = True
	else:
		nextCheck = False

if nextCheck == True:
	print("word is a palindrome")
else:
	print("word is not a palindrome")
