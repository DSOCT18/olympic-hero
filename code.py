# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
#load data
data= pd.read_csv(path)
#rename the column Total to Total_Medals.
data.rename(columns={'Total':'Total_Medals'}, inplace=True)
#print first 10 records of the dataframe.
print(data.head(10))



# --------------
#Code starts here
#Create a new column Better_Event that stores the comparision between the total medals won in Summer event and Winter event 
data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')
data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])
#Store the value counts to check which has been a better event in a new variable.
better_event = data['Better_Event'].value_counts().index.values[0]
print(better_event)


# --------------
#Code starts here

#Subsetting the dataframe
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

#Dropping the last column
top_countries=top_countries[:-1]

#Function for top 10
def top_ten(data, col):
    
    #Creating a new list
    country_list=[]
    
    #Finding the top 10 values of 'col' column
    country_list= list((data.nlargest(10,col)['Country_Name']))
    
    #Returning the top 10 list
    return country_list



#Calling the function for Top 10 in Summer
top_10_summer=top_ten(top_countries,'Total_Summer')
print("Top 10 Summer:\n",top_10_summer, "\n")

#Calling the function for Top 10 in Winter
top_10_winter=top_ten(top_countries,'Total_Winter')
print("Top 10 Winter:\n",top_10_winter, "\n")

#Calling the function for Top 10 in both the events
top_10=top_ten(top_countries,'Total_Medals')
print("Top 10:\n",top_10, "\n")

#Extracting common country names from all three lists
common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))

print('Common Countries :\n', common, "\n")

#Code ends here


# --------------
#Code starts here

#For Summer

#Creating the dataframe for Summer event
summer_df= data[data['Country_Name'].isin(top_10_summer)]

#Plotting the bar graph
plt.figure(figsize=(20, 6))
plt.bar(summer_df['Country_Name'], summer_df['Total_Summer'])

#Changing the graph title
plt.title('Top 10 Summer')

#Changing the x-axis label
plt.xlabel('Country Name')

#Changing the y-axis label
plt.ylabel('Total Medals')


#For Winter

#Creating the dataframe for Winter event
winter_df=data[data['Country_Name'].isin(top_10_winter)]

#Plotting the bar graph
plt.figure(figsize=(20, 6))
plt.bar(winter_df['Country_Name'], winter_df['Total_Winter'])

#Changing the graph title
plt.title('Top 10 Winter')

#Changing the x-axis label
plt.xlabel('Country Name')

#Changing the y-axis label
plt.ylabel('Total Medals')



#For both the events

#Creating the dataframe for both the events
top_df=data[data['Country_Name'].isin(top_10)]

#Plotting the bar graph
plt.figure(figsize=(20, 6))
plt.bar(top_df['Country_Name'], top_df['Total_Medals'])

#Changing the graph title
plt.title('Top 10')

#Changing the x-axis label
plt.xlabel('Country Name')

#Changing the y-axis label
plt.ylabel('Total Medals')





# --------------
#Code starts here
#In the dataframe 'summer_df'(created in the previous function) , create a new column Golden_Ratio which is the quotient after dividing the two columns Gold_Summer and Total_Summer.
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
#Find the max value of Golden_Ratio and the country associated with and store them in 'summer_max_ratio' and 'summer_country_gold' respectively.
summer_max_ratio= summer_df['Golden_Ratio'].max()
print('summer_max_ratio:',summer_max_ratio)
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print('summer_country_gold:',summer_country_gold)
#In the dataframe 'winter_df'(created in the previous function) , create a new column Golden_Ratio which is the quotient after dividing the two columns Gold_Winter and Total_Winter.
winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
#Find the max value of Golden_Ratio and the country associated with and store them in 'winter_max_ratio' and 'winter_country_gold' respectively.
winter_max_ratio= max(winter_df['Golden_Ratio'])
print('winter_max_ratio:',winter_max_ratio)
winter_country_gold= winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
print('winter_country_gold:',winter_country_gold)
#In the dataframe top_df'(created in the previous function) , create a new column Golden_Ratio which is the quotient after dividing the two columns Gold_Total and Total_Medals.
top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
#Find the max value of Golden_Ratio and the country associated with and store them in top_max_ratio' and 'top_country_gold' respectively.
top_max_ratio= top_df['Golden_Ratio'].max()
print('top_max_ratio:',top_max_ratio)
top_country_gold= top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
print('top_country_gold:',top_country_gold)





# --------------
#Code starts here
#Drop the last row from the dataframe(The last row contains the total of all the values calculated vertically) and save the result in 'data_1'
data_1= data[:-1]
#Update the dataframe 'data_1' to include a new column called Total_Points which is a weighted value where each gold medal counts for 3 points, silver medals for 2 points, and bronze medals for 1 point.
data_1['Total_Points']= data_1['Gold_Total']*3 +data_1['Silver_Total']*2 + data_1['Bronze_Total']*1
print(data_1)
#Find the max value of Total_Points in 'data_1' and the country assosciated with it and store it in variables 'most_points' and 'best_country' respectively.
most_points= data_1['Total_Points'].max()
print('most_points:',most_points)
best_country= data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print('best_country:',best_country)


# --------------
#Code starts here
best= data[data['Country_Name']== best_country]
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot(kind='bar',stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()


