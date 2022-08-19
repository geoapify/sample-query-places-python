import requests
import urllib.parse

# You need a Geoapify API key to call the Places API (https://www.geoapify.com/places-api/)
# Sign up on https://www.geoapify.com/ and generate an API key
# The Free Plan (https://www.geoapify.com/pricing/) lets you download up to 3000*20 = 60000 places/day
# Replace "YOUR_API_KEY" with API key
apiKey = "YOUR_API_KEY"

# The limit parameter specifies the maximum number of places one API request returns. The Geoapify Places API can return up to 500 places with one request.
# Please be aware that more places in one request will require more processing time and yield a larger response object.
limitPerRequest = 20

# The API can return thousands of places depending on a place category and city.
# Set the maximum number of search results to avoid long execution times.
# Try to query by city districts for big cities.
totalLimit = 200

# The Places API supports more than 500 unique categories - https://apidocs.geoapify.com/docs/places/#categories
# You can search for places by multiple categories, separated by commas.
placeCategory = "commercial.books"

# We use the Geoapify Geocoding API to find a city's location - https://www.geoapify.com/geocoding-api/
city="Paris, France"

def getCityPlaces(city):
    cityData = getCityData(city)
    if(cityData):
        # We may need to make several API calls to retrieve all the places in the city. The offset parameter is used for pagination.
        places = getPlacesRecursively([], 0, placeCategory, cityData["place_id"])
        print(places)
    else:
        print("The city is not found")

def getCityData(city):
    cityUrl = urllib.parse.quote_plus(city)
    url = "https://api.geoapify.com/v1/geocode/search?text=" + cityUrl + "&format=json&apiKey=" + apiKey
    response = requests.get(url)
    resJson = response.json()
    if(resJson and resJson["results"] and len(resJson["results"])):
        cityData = resJson["results"][0]
    else:
        cityData = null
    print(cityData)
    return cityData


def getPlacesRecursively(foundPlaces, offset, category, cityId):
    url = "https://api.geoapify.com/v2/places?categories=" + category + "&filter=place:" + cityId + "&limit=" + str(limitPerRequest) + "&apiKey=" +  apiKey + "&offset=" + str(offset)
    response = requests.get(url)
    places = response.json()
    for place in places["features"]:
        foundPlaces.append(place["properties"])

    if (len(places["features"]) == 0 or len(foundPlaces) >= totalLimit):
        return foundPlaces
    else:
        print(str(len(foundPlaces)) + ' places found. Querying more places...')
        return getPlacesRecursively(foundPlaces, offset + limitPerRequest, category, cityId)
    

getCityPlaces(city)