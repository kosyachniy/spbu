import sys
sys.path.append("perceptron")

from func import *

def decide(cont):
	word=read(name='base')[0]
	ww=numread('weights').T

	cont=text(cont)

	result=[]
	for j in range(len(ww)):
		w=ww[j]
		k=0
		su=w[0]
		for i in cont:
			if i in word:
				k+=1
				su+=w[word.index(i)+1]

		su=round(su, 2) if k else 0
		result.append(su)

	print(result)
	for i in range(len(result)):
		if math.isinf(result[i]):
			result[i]=0

	m=sorted(result)[::-1]
	#print(m)
	'''
	ma = max(m)
	return m.index(ma), ma
	'''
	tex = ''

	for k in range(len(m)):
		if m[k]<=0:
			break

		for i in range(countcat):
			if result[i]==m[k]:
				tex+=categories[i]+' ('+str(int(m[k]*100) if m[k] < 1 else 99)+'%)\n'

	return tex if len(tex) else 'По этим данным невозможно определить категорию!'

if __name__ == '__main__':
	print(decide(input()))