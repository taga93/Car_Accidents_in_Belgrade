import pandas as pd
import math
from gmplot import gmplot

from Complete_DataFrame import my_dataFrame


#function geolocation
def geolocation(input_data, marker_size, file_name):

    #extract only coordinates and convert them to tuple
    coordinates_data = input_data[["N", "E"]]
    coordinates_data = coordinates_data.apply(tuple, axis=1)

    #add tuple coordinates to list
    coordinate_list = []
    for coord in coordinates_data:
        coordinate_list.append(coord)

    # Scatter points
    coordinate_lats, coordinate_lons = zip(*coordinate_list)

    # Defult map location
    gmap = gmplot.GoogleMapPlotter(44.797140, 20.513460, 11)

    #Scatter dots on the map
    #gmap.scatter(coordinate_lats, coordinate_lons, 'red', size = marker_size, marker = False)

    #Heatmap zones on the map (it does not need parameter of 'marker size')
    gmap.heatmap(coordinate_lats, coordinate_lons)

    # Draw
    name = str(file_name)+".html"
    gmap.draw(name)


def location_deadly_accident():

    deadly_outcome = my_dataFrame[my_dataFrame["Outcome"] == "Sa poginulim"]
    deadly_outcome = deadly_outcome[["Outcome", "Date,Time", "N", "E"]].reset_index(drop=True)

    result = geolocation(deadly_outcome, 90, "accidents_with_deadly_outcome")
    return result

#print(location_deadly_accident())

    
def location_accidents_with_injuries():

    outcome_with_injuries = my_dataFrame[my_dataFrame["Outcome"] == "Sa povredjenim"]
    outcome_with_injuries = outcome_with_injuries[["Outcome", "Date,Time", "N", "E"]].reset_index(drop=True)

    result = geolocation(outcome_with_injuries, 50, "accidents_with_injuries")
    return result

#print(location_accidents_with_injuries())


def location_accidents_with_material_damage():
    
    outcome_with_mat_damage = my_dataFrame[my_dataFrame["Outcome"] == "Sa mat.stetom"]
    outcome_with_mat_damage = outcome_with_mat_damage[["Outcome", "Date,Time", "N", "E"]].reset_index(drop=True)
    
    result = geolocation(outcome_with_mat_damage, 50, "accidents_with_material_damage")
    return result

#print(location_accidents_with_material_damage())


def location_accidents_with_parked_cars():
    
    with_parked_cars = my_dataFrame[my_dataFrame["Type"] == "SN SA PARKIRANIM VOZILIMA"]
    with_parked_cars = with_parked_cars[["Type", "Date,Time", "N", "E"]].reset_index(drop=True)

    result = geolocation(with_parked_cars, 50, "accidents_with_parked_cars")
    return result

#print(location_accidents_with_parked_cars())

    
def location_accidents_with_passers():
    
    with_passers = my_dataFrame[my_dataFrame["Type"] == "SN SA PEŠACIMA"]
    with_passers = with_passers[["Type", "Date,Time", "N", "E"]].reset_index(drop=True)
    
    result = geolocation(with_passers, 50, "accidents_with_passers")
    return result

#print(location_accidents_with_passers())
