from geopy.geocoders import Nominatim

# Initialize the geolocator with a user agent
geolocator = Nominatim(user_agent="myzipcodeapp_sajinkp_v1")

# Input from user
pincode_data = input("Enter the Pincode or Zipcode: ")

# Get the location info using geocode
location = geolocator.geocode(pincode_data)

print("📍 Zipcode or Pincode: ",pincode_data)
print("🌍 Location details: ")

# Display location info if found
if location:
    print(f"📌 Location address: {location.address}")
    print(f"🧭 Location latitude: {location.latitude}")
    print(f"🧭 Location longitude: {location.longitude}")
# Display error message if location not found
else:
    print("❌Location not found. Please check the Zipcode or Pincode.")