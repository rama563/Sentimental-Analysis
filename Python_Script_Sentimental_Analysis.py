# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 16:13:54 2018

@author: RamaKrishna
"""

# Importing the module

import textblob
import os as os
import pandas as pd
import io
import re
from textblob import TextBlob
os.chdir("C:/Users/ramakrishna/Desktop/Sentimental Analysis")
Input1=pd.read_csv('Airtel_Tweets.csv',encoding = "ISO-8859-1")
Input2=pd.read_csv('Jio_Tweets.csv',encoding = "ISO-8859-1")

Input1["cleaned_tweet"]=''
Input2["cleaned_tweet"]=''

for k in range(0,len(Input1.index)):
    Input1.at[k,'cleaned_tweet']=" ".join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", Input1.at[k,'text']).split())
    
    
for k in range(0,len(Input2.index)):
    Input2.at[k,'cleaned_tweet']=" ".join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", Input2.at[k,'text']).split())


    
Input1["Sentiment"]=""
Input2["Sentiment"]=""  

  
for i in range(0,len(Input1.index)):
    analysis=TextBlob(Input1.at[i,'text'])
    if analysis.sentiment.polarity > 0:
            Input1.at[i,"Sentiment"]="Positive"
    elif analysis.sentiment.polarity == 0:
            Input1.at[i,"Sentiment"]="Neutral"
    else:
           Input1.at[i,"Sentiment"]="Negative"
          
            

for i in range(0,len(Input2.index)):
    analysis=TextBlob(Input2.at[i,'text'])
    if analysis.sentiment.polarity > 0:
            Input2.at[i,"Sentiment"]="Positive"
    elif analysis.sentiment.polarity == 0:
            Input2.at[i,"Sentiment"]="Neutral"
    else:
           Input2.at[i,"Sentiment"]="Negative" 
    
Result1=Input1.groupby('Sentiment').agg('count')
Result2=Input2.groupby('Sentiment').agg('count')
Result1=Result1[[1]]
Result2=Result2[[1]]
sum1=Result1["created"].sum()  
sum2=Result2["created"].sum()

Input1_Positive_Per = 100*Result1.at["Positive","created"]/sum1
Input1_Negative_Per = 100*Result1.at["Negative","created"]/sum1
Input1_Neutral_Per = 100*Result1.at["Neutral","created"]/sum1

Input2_Positive_Per = 100*Result2.at["Positive","created"]/sum2
Input2_Negative_Per = 100*Result2.at["Negative","created"]/sum2
Input2_Neutral_Per = 100*Result2.at["Neutral","created"]/sum2

print("AppleMusic:  Positive tweets percentage:{} %".format(Input1_Positive_Per))
print("AppleMusic:  Negative tweets percentage:{} %".format(Input1_Negative_Per))
print("AppleMusic:  Neutral tweets percentage:{} %".format(Input1_Neutral_Per))

print("Spotify:  Positive tweets percentage:{} %".format(Input2_Positive_Per))
print("Spotify:  Negative tweets percentage:{} %".format(Input2_Negative_Per))
print("Spotify:  Neutral tweets percentage:{} %".format(Input2_Neutral_Per))


    
    

 