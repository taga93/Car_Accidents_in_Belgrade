import pandas as pd
import math
from gmplot import gmplot

from Complete_DataFrame import my_dataFrame

#number of specific accidents for each year
def accident_info_by_year():

    dataFrame_by_year = my_dataFrame.sort_values(by="Date,Time")
    dataFrame_by_year["Date,Time"] = dataFrame_by_year["Date,Time"].dt.year
    
    total_by_year = dataFrame_by_year.groupby("Date,Time").size().rename_axis('Year').reset_index(name='Total Acc.')
    
    deadly_by_year = dataFrame_by_year[dataFrame_by_year["Outcome"] == "Sa poginulim"]
    deadly_by_year = deadly_by_year.groupby("Date,Time").size().rename_axis('Year').reset_index(name='w/ victimes')

    with_injuries_by_year = dataFrame_by_year[dataFrame_by_year["Outcome"] == "Sa povredjenim"]
    with_injuries_by_year = with_injuries_by_year.groupby("Date,Time").size().rename_axis('Year').reset_index(name='w/ injuries')
    
    with_pedestrians_by_year = dataFrame_by_year[dataFrame_by_year["Type"] == "SN SA PEŠACIMA"]
    with_pedestrians_by_year = with_pedestrians_by_year.groupby("Date,Time").size().rename_axis('Year').reset_index(name='w/ pedestrians')
    
    with_one_car_by_year = dataFrame_by_year[dataFrame_by_year["Type"] == "SN SA JEDNIM VOZILOM"]
    with_one_car_by_year = with_one_car_by_year.groupby("Date,Time").size().rename_axis('Year').reset_index(name='w/ one car')

    with_parked_car_by_year = dataFrame_by_year[dataFrame_by_year["Type"] == "SN SA PARKIRANIM VOZILIMA"]
    with_parked_car_by_year = with_parked_car_by_year.groupby("Date,Time").size().rename_axis('Year').reset_index(name='w/ parked cars')

    with_two_with_turning = dataFrame_by_year[dataFrame_by_year["Type"] == "SN SA NAJMANjE DVA VOZILA – SKRETANjE ILI PRELAZAK"]
    with_two_with_turning = with_two_with_turning.groupby("Date,Time").size().rename_axis('Year').reset_index(name='w/ 2 or more cars - w/ turning')

    with_two_without_turning = dataFrame_by_year[dataFrame_by_year["Type"] == "SN SA NAJMANjE DVA VOZILA – BEZ SKRETANjA"]
    with_two_without_turning = with_two_without_turning.groupby("Date,Time").size().rename_axis('Year').reset_index(name='w/ 2 or more cars - w/o turning')


    df_list = [total_by_year, deadly_by_year, with_injuries_by_year, with_pedestrians_by_year, with_one_car_by_year,
               with_parked_car_by_year, with_two_with_turning, with_two_without_turning]

    new_pandas = pd.DataFrame(columns = ["Year"])
    new_pandas['Year'] = total_by_year['Year']

    for i in range(len(df_list)):
        new_pandas = pd.merge(new_pandas, df_list[i], on='Year')

    return new_pandas

#print(accident_info_by_year())



#number of specific accidents for each month
def accident_info_by_month():

    dataFrame_by_year = my_dataFrame.sort_values(by="Date,Time")
    dataFrame_by_year["Date,Time"] = dataFrame_by_year["Date,Time"].dt.to_period('M')
    
    total_by_year = dataFrame_by_year.groupby("Date,Time").size().rename_axis('Year-Month').reset_index(name='Total Acc.')
    
    deadly_by_year = dataFrame_by_year[dataFrame_by_year["Outcome"] == "Sa poginulim"]
    deadly_by_year = deadly_by_year.groupby("Date,Time").size().rename_axis('Year-Month').reset_index(name='w/ victimes')

    with_injuries_by_year = dataFrame_by_year[dataFrame_by_year["Outcome"] == "Sa povredjenim"]
    with_injuries_by_year = with_injuries_by_year.groupby("Date,Time").size().rename_axis('Year-Month').reset_index(name='w/ injuries')
    
    with_pedestrians_by_year = dataFrame_by_year[dataFrame_by_year["Type"] == "SN SA PEŠACIMA"]
    with_pedestrians_by_year = with_pedestrians_by_year.groupby("Date,Time").size().rename_axis('Year-Month').reset_index(name='w/ pedestrians')
    
    with_one_car_by_year = dataFrame_by_year[dataFrame_by_year["Type"] == "SN SA JEDNIM VOZILOM"]
    with_one_car_by_year = with_one_car_by_year.groupby("Date,Time").size().rename_axis('Year-Month').reset_index(name='w/ one car')

    with_parked_car_by_year = dataFrame_by_year[dataFrame_by_year["Type"] == "SN SA PARKIRANIM VOZILIMA"]
    with_parked_car_by_year = with_parked_car_by_year.groupby("Date,Time").size().rename_axis('Year-Month').reset_index(name='w/ parked cars')

    with_two_with_turning = dataFrame_by_year[dataFrame_by_year["Type"] == "SN SA NAJMANjE DVA VOZILA – SKRETANjE ILI PRELAZAK"]
    with_two_with_turning = with_two_with_turning.groupby("Date,Time").size().rename_axis('Year-Month').reset_index(name='w/ 2 or more cars - w/ turning')

    with_two_without_turning = dataFrame_by_year[dataFrame_by_year["Type"] == "SN SA NAJMANjE DVA VOZILA – BEZ SKRETANjA"]
    with_two_without_turning = with_two_without_turning.groupby("Date,Time").size().rename_axis('Year-Month').reset_index(name='w/ 2 or more cars - w/o turning')


    df_list = [total_by_year, deadly_by_year, with_injuries_by_year, with_pedestrians_by_year, with_one_car_by_year,
               with_parked_car_by_year, with_two_with_turning, with_two_without_turning]

    new_pandas = pd.DataFrame(columns = ["Year-Month"])
    new_pandas['Year-Month'] = total_by_year['Year-Month']

    for i in range(len(df_list)):
        new_pandas = pd.merge(new_pandas, df_list[i], on='Year-Month')

    return new_pandas

#print(accident_info_by_month())


def number_of_accidents(imput_data):
    
    #number of accidents
    first_date = min(imput_data["Date,Time"].dt.date)
    last_date = max(imput_data["Date,Time"].dt.date)

    number = "Number of accindents between " + str(first_date) + " and " + str(last_date) + ": " + str(len(imput_data))

    return number


def avg_time_between_accidents(imput_data):

    #avrage time between two accidents:
    datetime_list = imput_data["Date,Time"].tolist()
    time_diference = []
    for i in range(len(datetime_list)-1):
        
        diference_in_days = (datetime_list[i+1] - datetime_list[i])
        time_diference.append(diference_in_days)
        
    avrage_time = sum(time_diference, datetime.timedelta()) / len(time_diference)

    days = str(avrage_time)[:6] + " |"
    hours = str(avrage_time)[6:9] + " hours | "
    minutes = str(avrage_time)[10:12] + " min | "
    seconds = str(avrage_time)[13:15] + " sec"

    avrage_time = "Avrage time between two accidents: " + days + hours + minutes + seconds

    return avrage_time


#information for full database
def full_dataframe_info():

    number = number_of_accidents(my_dataFrame)
    avrage_time = avg_time_between_accidents(my_dataFrame)

    return number, avrage_time, my_dataFrame

#print(full_dataframe_info()[0])
#print(full_dataframe_info()[1])
#print(full_dataframe_info()[2])


#informations for deadly accidents
def deadly_accidents_info():
    
    deadly_outcome_df = my_dataFrame[my_dataFrame["Outcome"] == "Sa poginulim"]
    deadly_outcome_df = deadly_outcome_df.sort_values(by="Date,Time")
    deadly_outcome_df = deadly_outcome_df[["Outcome", "Date,Time", "N", "E"]].reset_index(drop=True)

    number = number_of_accidents(deadly_outcome_df)
    avrage_time = avg_time_between_accidents(deadly_outcome_df)

    return number, avrage_time, deadly_outcome_df

#print(deadly_accidents_info()[0])
#print(deadly_accidents_info()[1])
#print(deadly_accidents_info()[2])


#informations for accidents with injuries
def accidents_with_injuries_info():

    outcome_with_injuries_df = my_dataFrame[my_dataFrame["Outcome"] == "Sa povredjenim"]
    outcome_with_injuries_df = outcome_with_injuries_df.sort_values(by="Date,Time")
    outcome_with_injuries_df = outcome_with_injuries_df[["Outcome", "Date,Time", "N", "E"]].reset_index(drop=True)

    number = number_of_accidents(outcome_with_injuries_df)
    avrage_time = avg_time_between_accidents(outcome_with_injuries_df)

    return number, avrage_time, outcome_with_injuries_df

#print(accidents_with_injuries_info()[0])
#print(accidents_with_injuries_info()[1])
#print(accidents_with_injuries_info()[2])


#informations for accidents with parked cars
def accidents_with_parked_cars_info():

    with_parked_cars_df = my_dataFrame[my_dataFrame["Type"] == "SN SA PARKIRANIM VOZILIMA"]
    with_parked_cars_df = with_parked_cars_df.sort_values(by="Date,Time")    
    with_parked_cars_df = with_parked_cars_df[["Type", "Date,Time", "N", "E"]].reset_index(drop=True)

    number = number_of_accidents(with_parked_cars_df)
    avrage_time = avg_time_between_accidents(with_parked_cars_df)

    return number, avrage_time, with_parked_cars_df

#print(accidents_with_parked_cars_info()[0])
#print(accidents_with_parked_cars_info()[1])
#print(accidents_with_parked_cars_info()[2])


#informations for accidents with pedestrians
def accidents_with_pedestrians_info():
    
    with_pedestrians_df = my_dataFrame[my_dataFrame["Type"] == "SN SA PEŠACIMA"]
    with_pedestrians_df = with_pedestrians_df.sort_values(by="Date,Time")    
    with_pedestrians_df = with_pedestrians_df[["Type", "Date,Time", "N", "E"]].reset_index(drop=True)

    number = number_of_accidents(with_pedestrians_df)
    avrage_time = avg_time_between_accidents(with_pedestrians_df)

    return number, avrage_time, with_pedestrians_df

#print(accidents_with_pedestrians_info()[0])
#print(accidents_with_pedestrians_info()[1])
#print(accidents_with_pedestrians_info()[2])
