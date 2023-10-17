from geopy.geocoders import Nominatim

def get_coordinates(address):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(address)
    
    if location is not None:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        return None

# Usage example
address = input("Enter your address: ")

coordinates = get_coordinates(address)

if coordinates:
    latitude, longitude = coordinates
    print(f"Address: {address}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
else:
    print("Coordinates not found.")
