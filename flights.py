import flightradar24
import requests
import pandas as pd


def getflight():
    airline = 'BAW'
    fr = flightradar24.Api()
    flights = fr.get_flights(airline)
    for key, value in flights.items():

        print(key,value)
    return flights

def airlines():
    flight_id = 'TK1'  # Turkish Airlines' Istanbul - New York flight
    fr = flightradar24.Api()
    flight = fr.get_flight(flight_id)
    print(flight)
    return flight
#airlines()

getflight()