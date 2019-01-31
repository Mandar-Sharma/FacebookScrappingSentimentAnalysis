from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import regex as re 
import csv

index = {'love':0.9765,'like':0.8,'wow':0.0235,'haha':0.5,'sad':0.5,'angry':-0.9765}
analyser = SentimentIntensityAnalyzer()
list_of_values =[]
total_pos=0
total_neg=0
total_neu=0
total_analyzed=0
error_count=0
#Functions
        
def vader_get_sentiment(sentence):
    snt = analyser.polarity_scores(sentence)
    return snt

def remove_n(given_list):   
    new_list = []
    for i in range(0,len(given_list)-1):
        if i % 2 !=0:
            new_list.append(given_list[i])
    return new_list

#Kaam    
path = 'C:\Users\Mandar PC\Desktop\NLP\Cleaned_Deuba'
#Dest
sentiment_total= open(path+'\SentimentAnalysis.csv','a')
writer = csv.writer(sentiment_total, delimiter=',')
#Source
current_file = open(path+'\Total.json','rb')
#Reading
lines = current_file.read().split(']')
#Loops start from 1 because 0 describes data type. Ends in -2 because ....
end = len(lines)-2

for i in range(1,end):
	try:
		whatIwant= lines[i][1:].split('"')
		whatIneed = remove_n(whatIwant)
		comment = whatIneed[0].strip()
		sentiment_man=vader_get_sentiment(comment)
		likes = int(re.sub(r'[^\w]', '', whatIneed[4].strip()))
		loves = int(re.sub(r'[^\w]', '', whatIneed[5].strip()))
		#wows = int(re.sub(r'[^\w]', '', whatIneed[6].strip()))
		#hahas= int(re.sub(r'[^\w]', '', whatIneed[7].strip()))
		#sads = int(re.sub(r'[^\w]', '', whatIneed[8].strip()))
		angrys= int(re.sub(r'[^\w]', '', whatIneed[9].strip()))
		writer.writerow([comment,sentiment_man])
		list_of_values.append(sentiment_man['compound'])
		total_analyzed = total_analyzed+1
		#print(comment,sentiment_man,likes,loves,wows,hahas,sads,angrys)
		if sentiment_man['compound'] > 0:
			total_pos= total_pos + 1
			state = 'pos'
	 	elif sentiment_man['compound'] == 0:
	 		total_neu = total_neu + 1
	 		state = 'neu'
	 	else:
			total_neg = total_neg + 1
			state = 'neg'
		if likes != 0: 
	 		for i in range(1,likes+1):
	 			list_of_values.append(sentiment_man['compound'])
	 			total_analyzed = total_analyzed+1
	 			if state == 'pos':
	 				total_pos= total_pos + 1
	 			if state == 'neu':
	 				total_neu= total_neu + 1
	 			if state == 'neg':
	 				total_neg= total_neg + 1
	 	if loves != 0: 
	 		for i in range(1,loves+1):
	 			total_analyzed = total_analyzed+1
	 			list_of_values.append(sentiment_man['compound'])
	 			if state == 'pos':
	 				total_pos= total_pos + 1
	 			if state == 'neu':
	 				total_neu= total_neu + 1
	 			if state == 'neg':
	 				total_neg= total_neg + 1
	 	if angrys != 0: 
	 		for i in range(1,angrys+1):
	 			total_analyzed = total_analyzed+1
	 			list_of_values.append(-sentiment_man['compound'])
	 			if state == 'neg':
	 				total_pos= total_pos + 1
	 			if state == 'pos':
	 				total_neg= total_neg + 1
	
	except Exception as e:
		pass

youtube = open(path+'\Total_Youtube.json','rb')
lines = youtube.read().split(']')
#Loops start from 1 because 0 describes data type. Ends in -2 because ....
end = len(lines)-2

for i in range(1,end):
	try:
		whatIwant= lines[i][1:].split('"')
		whatIneed = remove_n(whatIwant)
		comment = whatIneed[0].strip()
		sentiment_man=vader_get_sentiment(comment)
		list_of_values.append(sentiment_man['compound'])
		total_analyzed = total_analyzed+1
		if sentiment_man['compound'] > 0:
			total_pos= total_pos + 1
			state = 'pos'
	 	elif sentiment_man['compound'] == 0:
	 		total_neu = total_neu + 1
	 		state = 'neu'
	 	else:
			total_neg = total_neg + 1
			state = 'neg'
	
	except Exception as e:
		pass
#Stats from Post
postlove = 60
postangry = 301
eff_angry = 241

total_neg = total_neg + 241
total_analyzed = total_analyzed+ 241
for a in range(1,242):
	list_of_values.append(-0.9765)

print (total_pos,total_neu,total_neg,total_analyzed)
ppos = (float(total_pos)/float(total_analyzed))*100
pneg = (float(total_neg)/float(total_analyzed))*100
pneu = (float(total_neu)/float(total_analyzed))*100
print ("Percent Positive Responses:", ppos)
print ("Percent Neutral Responses:", pneu)
print ("Percent Negative Responses:", pneg)

plt.hist(list_of_values, normed=True, bins=30)
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.title('Sentiment Histogram')
plt.show()