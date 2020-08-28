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
		return b
	else:
		b.append(a.head)
		return getverb(a.head,b)

def getphrase(sents):
	test=[]
	for i in sents:
		for j in i.noun_chunks:
			b=[j]
			test.append(getverb(j.root,b))
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
	doc=nlp(test5)
	return list(doc.sents)


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
	for i in phrase:
		if set(i.lemma_.split())-(set(i.lemma_.split())-set(verb))!=set():
			obj=[]
			if i.root.tag_=='VBN':
				for j in i:
					if j.i<i.root.i:
						obj.append(j.lemma_)
			else:
				for j in i:
					if j.i>i.root.i:
						obj.append(j.lemma_)
			if set(obj)-(set(obj)-set(noun))!=set():
				test.append(i)
	return test

def compare(des,pol):
	try:
		des=nlp(des)
		dessents=list(des.sents)
		dessents=removeneg(dessents)
		desphrase=getphrase(dessents)
		desphrase=removeyou(desphrase)
		desphrase=removeunrelatedphrase(desphrase)
		pol=nlp(pol)
		polsents=list(pol.sents)
		polsents=removeneg(polsents)
		polphrase=getphrase(polsents)
	except:
		return -2
	test=[]
	for i in desphrase:
		for j in polphrase:
			if i.similarity(j)>0.9:
				test.append(i)
				break
	result=list(set(desphrase)-set(test))
	return result

if __name__ == '__main__':
	policy=getpolicycontent()
	description=getdescription()
	negtive=readfile('negtive').split()
	noun=readfile('noun').split('\n')[0].split(',')
	noun.remove('datum')
	verb=readfile('verb').split('\n')[0].split(',')
	result={}
	m=0
	for i in policy:
		m=m+1
		print(m)
		try:
			pol=policy[i]
			des=description[i]
			result[i]=compare(des,pol)
			print(i,result[i])
			f=open('2_result_inconsistent_skill.txt','a')
			a=f.write(i)
			a=f.write('\t')
			if result[i]==[]:
				a=f.write('0')
			else:
				a=f.write(str(result[i]).replace('\n',''))	
			a=f.write('\n')
			f.close()
		except:
			break

