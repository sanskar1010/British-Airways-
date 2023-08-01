import pandas as pd
from afinn import Afinn
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_excel('Britishairways.xlsx')
df=df.dropna(subset=['Seat Comfort','Cabin Staff Service',
       'Food & Beverages','Inflight Entertainment','Ground Service',
       'Value For Money','Wifi & Connectivity'])

# 1)Perform sentiment analysis on the customer comments in the "title" column to identify positive, negative, or neutral sentiments regarding their experiences.

def sentence(v):
    result=Afinn().score(v)
    if result==0:
        return 'neutral'
    elif result>0:
        return 'Positive'
    else:
        return 'Negative'
# df['Sentiment']=df['title'].apply(sentence)

#2) Calculate the average ratings for each parameter (Value For Money, Recommended, Seat Comfort, Cabin Staff Service, Ground Service, Food & Beverages, Inflight Entertainment, Wifi & Connectivity).

columns=df[['Seat Comfort','Cabin Staff Service',
       'Food & Beverages','Inflight Entertainment','Ground Service',
       'Value For Money','Wifi & Connectivity']]
columns=columns.apply(pd.to_numeric)
average_rating=columns.mean()
# average_rating.plot(kind='bar')
# plt.show()

#3) Determine the overall average rating for each type of traveler (Couple Leisure, Business, Solo Leisure).

traveler_rating=df.groupby('Type Of Traveller')[['Seat Comfort','Cabin Staff Service',
       'Food & Beverages','Inflight Entertainment','Ground Service',
       'Value For Money','Wifi & Connectivity']].mean()
# print(traveler_rating)
# traveler_rating.plot(kind='bar')
# plt.show()

#4) Analyze the overall average rating for each seat type (Premium Economy, Economy Class, Business Class).

seat_type_rating=df.groupby('Seat Type')[['Seat Comfort','Cabin Staff Service',
       'Food & Beverages','Inflight Entertainment','Ground Service',
       'Value For Money','Wifi & Connectivity']].mean()
# print(seat_type_rating)
# seat_type_rating.plot(kind='bar')
# plt.xticks(rotation=45)
# plt.show()

#5)Analyze the number of flights taken by date to identify peak travel periods.

no_of_flights_taken=df['Date Flown'].value_counts().reset_index()
a=no_of_flights_taken['count'].argmax()
peak_period=no_of_flights_taken['Date Flown'][a]
# print(peak_period)
# plt.plot(no_of_flights_taken['Date Flown'],no_of_flights_taken['count'])
# plt.xlabel('date')
# plt.xticks(rotation=90)
# plt.show()

#6)Identify the most commonly traveled routes (origin and destination pairs) based on the "Route" column.

most_commonly_routes=df['Route'].value_counts()
# print(most_commonly_routes.head())

#7)Aircraft Analysis:
    # a)Identify the most frequently used aircraft based on the "Aircraft" column.
#     # b)Analyze the ratings based on different aircraft models.
most_frequently_used_aircraft=df['Aircraft'].value_counts()
aircraft_rating_analysis=df.groupby('Aircraft')[['Seat Comfort','Cabin Staff Service',
       'Food & Beverages','Inflight Entertainment','Ground Service',
       'Value For Money','Wifi & Connectivity']].mean().reset_index()
# plt.bar(aircraft_rating_analysis['Aircraft'],aircraft_rating_analysis['Seat Comfort'],label='Seat Comfort')
# plt.bar(aircraft_rating_analysis['Aircraft'],aircraft_rating_analysis['Cabin Staff Service'],label='Cabin Staff Service')
# plt.bar(aircraft_rating_analysis['Aircraft'],aircraft_rating_analysis['Food & Beverages'],label='Food & Beverages')
# plt.bar(aircraft_rating_analysis['Aircraft'],aircraft_rating_analysis['Ground Service'],label='Ground Service')
# plt.bar(aircraft_rating_analysis['Aircraft'],aircraft_rating_analysis['Value For Money'],label='Value For Money')
# plt.bar(aircraft_rating_analysis['Aircraft'],aircraft_rating_analysis['Wifi & Connectivity'],label='Wifi & Connectivity')
# plt.legend()
# plt.xlabel('aircraft')
# plt.ylabel('ratings')
# plt.xticks(rotation=90)
# plt.show()

#8) Calculate the percentage of customers who recommended the airline or service.

recommended_counts=df.loc[df['Recommended']=='yes']
yes_counts=recommended_counts['Recommended'].value_counts()
percentage_yes_counts=(yes_counts/len(df['Recommended']))*100
#print(percentage_yes_counts)

#                          OR

# recommended_customers = df[df['Recommended'] == 'yes'].shape[0]
# total_customers = df.shape[0]
# print((recommended_customers / total_customers) * 100)

#9)Identify the relationship between "Value For Money" ratings and other factors, such as seat type, type of traveler, or aircraft.

seat_type_grouped = df.groupby('Seat Type')['Value For Money'].mean()
traveler_grouped = df.groupby('Type Of Traveller')['Value For Money'].mean()
aircraft_grouped = df.groupby('Aircraft')['Value For Money'].mean()
# seat_type_grouped.plot(kind='bar')
# plt.title('Mean Value For Money ratings by Seat Type')
# plt.xlabel('Seat Type')
# plt.ylabel('Mean Value For Money rating')
# plt.show()
# traveler_grouped.plot(kind='bar')
# plt.title('Mean Value For Money ratings by Type Of Traveller')
# plt.xlabel('Type Of Traveller')
# plt.ylabel('Mean Value For Money rating')
# plt.show()
# aircraft_grouped.plot(kind='bar')
# plt.title('Mean Value For Money ratings by Aircraft')
# plt.xlabel('Aircraft')
# plt.ylabel('Mean Value For Money rating')
# plt.show()


#10) Determine the satisfaction levels with "Inflight Entertainment" and its impact on overall ratings.

#  ****************************(yet to solved)*************************************


