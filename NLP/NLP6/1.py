from textblob import  TextBlob

s1 = "Eminem is God"

t1 = TextBlob(s1)

print t1.sentiment
if t1.sentiment.subjectivity == 0:
	print 'It a known fact'
if 1 > t1.sentiment.polarity > 0:
	print 'Positive'
if -1 > t1.sentiment.polarity > 0:
	print 'Negative'
if t1.sentiment.polarity ==0:
	print 'Neutral'