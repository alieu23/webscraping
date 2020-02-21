import flightradar24
import requests
import pandas as pd
from pandas import DataFrame


def getflight():
    air = []
    airline = 'BAW'
    fr = flightradar24.Api()
    flights = fr.get_flights(airline)
    data= list(flights.values())
    x=2
    while x>=2:
        x=x+1
        data1 = data[x][11:14]
        air.append(data1)
        df = pd.DataFrame(air)
        df.to_csv('flights.csv', index=False)
        print(data1)

    return flights

def airlines():
    flight_id = 'TK1'  # Turkish Airlines' Istanbul - New York flight
    fr = flightradar24.Api()
    flight = fr.get_flight(flight_id)
    print(flight)
    return flight
#airlines()

getflight()