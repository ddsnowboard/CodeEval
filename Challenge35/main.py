import re
from sys import argv
email = re.compile(r"[A-Za-z0-9_]+@[A-Za-z0-9_]+[.][a-z.]{2-5}")
with open(argv[1]) as f:
	for i in f:
		print(str(email.match(i) is not None).lower())