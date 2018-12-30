from re import match

rule = '^\+(a\+b*-)*-$'

print('YNEOS'[match(rule, input()) is None::2])