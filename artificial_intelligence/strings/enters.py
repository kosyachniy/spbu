import re
s=''
with open('text.txt', 'r') as file:
	for i in file:
		s+=i[:-1]+' '
with open('cont.txt', 'w') as file:
	print(s.replace('"', '\\"').replace('	', ' '), end='', file=file)