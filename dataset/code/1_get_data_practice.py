import os
import csv
import spacy

nlp=spacy.load('en_core_web_sm-2.2.5')



def readfile(name):
	f=open(name+'.txt','r')
	a=f.read()
	f.close()
	return a

def getpolicycontent():
	policy={}
	b=os.listdir('privacy_policy/')
	for i in b:
		f=open('privacy_policy/'+i,'r',encoding='iso-8859-15')
		a=f.read()
		f.close()
		policy[i[:-4]]=a
	return policy


def getdescription():
	description={}
	csvfile=open('../dataset/skills.csv','r')
	reader=csv.reader(csvfile)
	for row in reader:
		if row[0] in policy:
			description[row[0]]=row[7]
	csvfile.close()
	return description

def getverb(a,b):
	if a.head.pos_=='VERB':
		b.append(a.head)
		return b
	elif a.head==a:
		return 0
	else:
		b.append(a.head)
		return getverb(a.head,b)

def getphrase(sents):
	test=[]
	for i in sents:
		test2=[]
		for j in i.noun_chunks:
			b=[j]
			result=getverb(j.root,b)
			if result!=0:
				test2.append(result)
		test3=[]
		for j in test2:
			for k in test2:
				if j!=k and j[len(j)-1].head==k[len(k)-1]:
					a=j[:-1]
					a.append(k[-1])
					test3.append(a)
					a=k[:-1]
					a.append(j[-1])
					test3.append(a)
		for j in test2:
			test.append(j)
		for j in test3:
			test.append(j)
	test2=[]
	for i in test:
		if len(i)>1:
			test2.append(i)
	test=test2
	test2=[]
	test3=[]
	test4=[]
	for i in test:
		if i[0].root.pos_=='-PRON-' or i[0].root.dep_=='nsubj':
			test2.append(i)
		elif i[0].root.dep_=='nsubjpass':
			test3.append(i)
		else:
			i.reverse()
			test4.append(i)
	for i in test2:
		for j in test4:
			if i[len(i)-1]==j[0]:
				new=[]
				for k in i:
					new.append(k)
				new.pop()
				for k in j:
					new.append(k) 
				test3.append(new)
	test5=''
	for i in test3:
		phrase=''
		for j in i:
			phrase=phrase+' '+j.text
		phrase=phrase+'.'
		test5=test5+phrase
#	doc=nlp(test5)
	return test5



def removeneg(sents):
	test=[]
	for i in sents:
		if set(i.lemma_.split())-(set(i.lemma_.split())-set(negtive))!=set():
			test.append(i)
	return list(set(sents)-set(test))


def removeyou(phrase):
	test=[]
	for i in phrase:
		for j in i:
			if j.dep_=='nsubj' and (j.text=='you' or j.text=='You'):
				if i.root.lemma_!='need' and i.root.lemma_!='provide':
					test.append(i)
					break
	return list(set(phrase)-set(test))

def removeunrelatedphrase(phrase):
	test=[]
	for j in range(0,int(len(phrase)/100000)+1):
		k=phrase[j*100000:(j+1)*100000]
		k=nlp(k).sents
		for i in k:
			if set(i.lemma_.split())-(set(i.lemma_.split())-set(verb))!=set() and set(i.lemma_.split())-(set(i.lemma_.split())-set(noun))!=set():
				test.append(i)
				break
		if test!=[]:
			break
	return test


def removeunrelatedsents(sents):
	test=[]
	for i in sents:
		if set(i.lemma_.split())-(set(i.lemma_.split())-set(verb))!=set() and set(i.lemma_.split())-(set(i.lemma_.split())-set(noun))!=set():
			test.append(i)
	return test

def compare(pol):
	try:
		pol=nlp(pol)
		polsents=pol.sents
		polsents=removeunrelatedsents(polsents)
		k=0
		for i in polsents:
			polsent=[i]
			polphrase=getphrase(polsent)
			polphrase=removeunrelatedphrase(polphrase)
			if polphrase!=[]:
						k=k+1
	except:
		return -2
	return k

if __name__ == '__main__':
	policy=getpolicycontent()
	negtive=readfile('negtive').split()
	noun=readfile('noun').split('\n')[0].split(',')
	verb=readfile('verb').split('\n')[0].split(',')
	verb.append('save')
	noun.append('information')
	result={}
	m=0
	for i in policy:
		m=m+1
		print(m)
		try:
			pol=policy[i]
			result[i]=compare(pol)
			print(i,result[i])
			f=open('1_result_data_practice.txt','a')
			a=f.write(i)
			a=f.write('\t')
			a=f.write(str(result[i]))
			a=f.write('\n')
			f.close()
		except:
			break

