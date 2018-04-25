# Write a function that uses list comprehension to return whether a password meets a minimum threshold:
# it contains a mixture of upper- and lowercase letters, and at least one number
# Write a function that uses list comprehension to return a password's strength rating.
# This function should return a lower integer for a weak password and a higher integer for a stronger password. (Suggested scale: 1-10) Consider these criteria:
# mixture of upper- and lower-case
# inclusion of numerals
# inclusion of these non-alphanumeric chars: . ? ! & # , ; : - _ *



def passwordReq(passw):
	uppers = [ char for char in passw if char.isupper()]
	lowers = [ char for char in passw if char.islower()]
	nums = [ char for char in passw if char.isdigit()]
	if (len(uppers) == 0 or len(lowers) == 0 or len(nums) == 0):
		print "Invalid password"
	else:
		print "Valid password"

passwordReq("password23D")
passwordReq("password")
passwordReq("12345")

def passwordStrength(passw):
	uppers = [ char for char in passw if char.isupper()]
	lowers = [ char for char in passw if char.islower()]
	nums = [ char for char in passw if char.isdigit()]
	others = [ char for char in passw if (char not in uppers and char not in lowers and char not in nums)]
	
	if len(uppers) == 0:
		upperCount = -1
	elif len(uppers) > 3:
		upperCount = 3
	else:
		upperCount = len(uppers)
	
	if len(lowers) == 0:
		lowerCount = -1
	elif len(lowers) > 3:
		lowerCount = 3
	else:
		lowerCount = len(lowers)
	
	if len(nums) == 0:
		numCount = -1
	elif len(nums) > 3:
		numCount = 3
	else:
		numCount = len(nums)
		
	if len(others) == 0:
		otherCount = -1
	elif len(others) > 3:
		otherCount = 3
	else:
		otherCount = len(others)
	
	stren = (upperCount + lowerCount + numCount + otherCount) 
	if stren < 0:
		print 0
	if stren > 10:
		print 10
	else:
		print stren

passwordStrength("asldkaQWOIE12038!!!!")
passwordStrength("asldka!!!")
passwordStrength("asIE12038!!")
passwordStrength("aASDLKJ!!")
passwordStrength("abcD")
	
	