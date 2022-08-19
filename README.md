# Getting OpenStreetMap data in Python

This code sample shows how to get OSM data using the [Geoapify Places API](https://www.geoapify.com/places-api/). You can query cities and places by specifying a city and [places category](https://apidocs.geoapify.com/docs/places/#categories).

## Run the code sample

**Important!** Sign up on Geoapify, generate an API key and replace "YOUR_API_KEY" with your API key.

You can run the Python code either locally or through an online compiler. For example, [Programiz](https://www.programiz.com/python-programming/online-compiler/).

To run the code sample locally:
1. Install Python3 from the [official page >>](https://www.python.org/downloads/)
2. Install the "requests" module. You can find detailed instructions [here >>](https://pypi.org/project/requests/)
3. Execute the Python file with "`python3 city_find.py`"

## Get OSM places for a city

You can download up to 60000 places/day with your API key for free. Learn [Geoapify Pricing policies here >>](https://www.geoapify.com/pricing/)
1. Choose a place category and put it to the `placeCategory` variable. You can find a list of categories [here >>](https://apidocs.geoapify.com/docs/places/#categories)
2. Set the `city` variable.
3. Adjust the `limitPerRequest` and `totalLimit` variables.
4. Run the Code Sample

## Learn more
* [Geoapify Location Platform](https://www.geoapify.com/) - APIs and geodata for Location-aware apps
* [Places API playground](https://apidocs.geoapify.com/playground/places/) - try the API without registration
* [Places API documentation](https://apidocs.geoapify.com/docs/places/) - learn more about API options and parameters