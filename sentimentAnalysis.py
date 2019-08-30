import tweepy
from textblob import TextBlob

print('Sentimental Analysis')
""" Sentimential Analysyis is used to measure the polarity of a given text 
    Algorithm Natural Language Processing is used where a given text is divided into Lexiams or 
	token and each token is seperatly analysed """
auth = tweepy.OAuthHandler('7ueNHhXrcNVPVU6dFfHR1ihDP','vNhCCTHE6IsT6DNtPOol0mIbnvSC4huA1y57trwXPmxMRdlybz')
#To auth the developer
auth.set_access_token('839480539098796033-ybDruAv4ATW6VhYeOC3mQByCGQcdEUk','xhMwJsCJOBoCXcpbsk9lIcx18WW5fGTVUmpAtw2a7rfDV')
#to access the api created by a app via twitter
api = tweepy.API(auth)
#authorization 
search_tweet = api.search('MachineLearning')
#searching tweets which has keyword 'MachineLearning' 
for tweet in search_tweet:
	#Itterating to all the posiable searched tweets 
	print(tweet.text)
	#printing the tweets which has the keyword "Machine Learning"
	analysis = TextBlob(tweet.text)
	#all the text are initialised onto analysis using Textblob Libraries
	print(analysis.sentiment)
	"""sentiment for the analysis is printed Two constrains are given by this function 

	1. Polatity : Range of value lies from -1 to 1 where negetive value tells that the respective tweet is Negetive
	these include worls like  Unlikely, doesnot or other similar kinds of words
	positive word like likely , has  or other similar kinds of  word range in positive value


	2.Subjectivity: the value ranges from 0 to 1 It tells how a given tweet is relatiable to the searched word where
	 0 represent that the tweet is unrelated to the searched dispite the word mention in the tweet
	 1 represent that the tweet is purely related to the searched word 
	
	 """