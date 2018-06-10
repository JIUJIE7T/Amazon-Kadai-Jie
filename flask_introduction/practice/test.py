import re
text = "3+(2-5)afa"

if re.match('^[0-9\+\-\*\-\(\)]+$', text):
	print('yes')
else:
    print('no') 