from datetime import datetime

timestamp_ms =  1704177271826  
timestamp_seconds = timestamp_ms / 1000.0  # Convert milliseconds to seconds

# Convert the timestamp to a datetime object
datetime_object = datetime.utcfromtimestamp(timestamp_seconds)

# Format the datetime object as a string
formatted_datetime = datetime_object.strftime('%Y-%m-%d %H:%M:%S UTC')

print(formatted_datetime)
