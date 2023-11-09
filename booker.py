import requests

# Define the URL
url = "https://duke.libcal.com/ajax/space/book"

# Define the data
data = {
    "session": (None, "39605291"),
    "fname": (None, "N"),
    "lname": (None, "W"),
    "email": (None, "nw128@duke.edu"),
    "q15103": (None, "Yes"),
    "bookings": (None, json.dumps([{"id":1,"eid":49578,"seat_id":0,"gid":12858,"lid":7266,"start":"2023-11-11 16:00","end":"2023-11-11 18:00","checksum":"4bfc869986dff96b199aadf9ca713c17"}])),
    "returnUrl": (None, "/reserve/edge"),
    "pickupHolds": (None, ""),
    "method": (None, "11"),
}

# Send the POST request
response = requests.post(url, files=data)

# Check the response
if response.status_code == 200:
    print("Request was successful.")
    print("Response content:", response.content)
else:
    print("Request failed. Status code:", response.status_code)