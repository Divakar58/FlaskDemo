import requests #type:ignore
from bs4 import BeautifulSoup #type:ignore
#import csv
import pandas as pd #type:ignore
from App.config import WEATHER_URL

def GetWeather():
    response = requests.get(WEATHER_URL)
    if(response.status_code==200):
        soup = BeautifulSoup(response.text, 'html.parser')
        weather=soup.find(class_="wr-day-carousel__scrollable")
        if(weather):
            days=weather.find_all('li')
            print(len(days))
            if(len(days)>0):
                day=[]
                desc=[]
                tmp=[]
                dis={}
                for weather in days:
                    day=weather.find(class_="wr-date").get_text()
                    day.append(day)
                    description=weather.find(class_="wr-day__weather-type-description-container").get_text()
                    desc.append(description)
                    temp=weather.find(class_="wr-day-temperature").get_text()
                    tmp.append(temp)
                dis["Day"]=day
                dis["Description"]=desc
                dis["Temperature"]=tmp
                df=pd.DataFrame(dis)
                if(len(df.index)>0):
                    df.to_csv('weather.csv')
                    return df
                else:
                    df=pd.DataFrame({})
                    return df
    else:
        raise Exception("Not able to get data from weather url "+response.status_code+" "+ response.text)
