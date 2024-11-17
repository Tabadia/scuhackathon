from flask import Flask, jsonify , Blueprint, render_template, request
import json, requests
import numpy as np
# import geopandas as gpd

routes = Blueprint('routes', __name__)
CRASH_DATA_URL = 'https://data.sanjoseca.gov/api/3/action/datastore_search?resource_id=15408d78-9734-4ea1-b3e5-a0f99568dd9b&limit=5&q=title:jones' 
@routes.route('/crashes', methods=['GET'])
def get_crash_data():
    uResponse = requests.get(CRASH_DATA_URL)
    if uResponse.status_code == 200:
        data = uResponse.json()
    return jsonify(data)



# SAN_JOSE_API_URL = "https://geo.sanjoseca.gov/server/rest/services/OPN/OPN_OpenDataService/MapServer/549/query"

# def fetch_neighborhood_data():
#     params = {
#         "where": "1=1",
#         "outFields": "*",
#         "outSR": "4326",
#         "f": "json"
#     }
#     response = requests.get(SAN_JOSE_API_URL, params=params)
#     response.raise_for_status()  # Raise an error if the request fails
#     return response.json()

class Data:
   def __init__(self, neighborhood):
    self.neighborhood = []
    
class Neighborhood:
    def __init__(self, name, score):
        self.name = "Fowler Creek"
        self.score = 7.4

@routes.route("/neighborhood.html")
def neighborhood():
    nName = request.args.get('nName')
    # make request to bedrock with neighbor name
    # parse json request
    # return request as Neighborhood Class
    #return it  below VVVV
    return render_template("neighborhood.html", nName=nName)

@routes.route("/")
def index():
    return render_template("index.html")

# @routes.route("/api/neighborhoods")
# def get_neighborhoods():
#     data = fetch_neighborhood_data()

#     return jsonify(data)

@routes.route("/api/coordinates")
def get_coordinates():
    neighborhoods = []
    data = fetch_neighborhood_data()
    for feature in data.get('features', []):
        name = feature['properties'].get('name', 'Unknown')
        coordinates = feature['geometry'].get('coordinates',[])
        neighborhoods.append({'name':name, 'coordinates': coordinates})
    neighborhoods = neighborhoods.sort(key=lambda x: x['name'])    
    return(neighborhoods)

# @routes.route("/map")
# def createMap():
#     data = fetch_neighborhood_data()
    
