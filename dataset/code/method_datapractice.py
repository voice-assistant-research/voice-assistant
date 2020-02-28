import os
import csv
import spacy

nlp=spacy.load('/home/song/Downloads/en_core_web_lg-2.2.5/en_core_web_lg/en_core_web_lg-2.2.5')



def readfile(name):
	f=open(name+'.txt','r')
	a=f.read()
	f.close()
	return a

def getpolicycontent():
	policy={}
	b=os.listdir('totaltxt')
	for i in b:
		f=open('totaltxt/'+i,'r')
		a=f.read()
		f.close()
		policy[i[:-4]]=a
	return policy


def getdescription():
	description={}
	csvfile=open('description.csv','r')
	reader=csv.reader(csvfile)
	for row in reader:
		name=row[0].replace('/','')
		if name in policy:
			description[name]=row[1]
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
	basisphrase=[]
	for i in sents:
		for j in i.noun_chunks:
			b=[j]
			basisphrase.append(getverb(j.root,b))
	backup=[]
	for i in basisphrase:
		if len(i)>1:
			backup.append(i)
	basisphrase=backup
	positive=[]
	negtive=[]
	objective=[]
	for i in test:
		if i[0].root.pos_=='-PRON-' or i[0].root.dep_=='nsubj':
			positive.append(i)
		elif i[0].root.dep_=='nsubjpass':
			positive.append(i)
		else:
			i.reverse()
			objective.append(i)
	for i in positive:
		for j in objective:
			if i[len(i)-1]==j[0]:
				new=[]
				for k in i:
					new.append(k)
				new.pop()
				for k in j:
					new.append(k) 
				negtive.append(new)
	total=''
	for i in negtive:
		phrase=''
		for j in i:
			phrase=phrase+' '+j.text
		phrase=phrase+'.'
		total=total+phrase
	doc=nlp(total)
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

def removeunrelatedphrase(phrase,threshold):
	test=[]
	for i in phrase:
		for j in phrasesset:
			if i.similarity(j)>threshold:
				test.append(i)
	return test


def compare(pol):
	try:
		pol=nlp(pol)
		polsents=pol.sents
		k=0
		for i in polsents:
			polsent=[i]
			polphrase=getphrase(polsent)
			polphrase=removeunrelatedphrase(polphrase,threshold)
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
	phrasesset=[]
	for i in noun:
		for j in verb:
			phrasesset.append(nlp(i+' '+j))
	result={}
	m=0	
	old=readfile('result_policysentence')
	for i in policy:
		m=m+1
		print(m)
		if str(i) in old:
			continue
		try:
			pol=policy[i]
			result[i]=compare(pol,threshold)
			print(i,result[i])
			f=open('result_policysentence.txt','a')
			a=f.write(i)
			a=f.write('\t')
			a=f.write(str(result[i]))
			a=f.write('\n')
			f.close()
		except:
			break

