functionnames = {"addstock","sell","checkstock","deleteall","checksales"}

def check(name):
	if name in functionnames:
		return True
	else:
		return False

check('addstock')
check('qwefbio')