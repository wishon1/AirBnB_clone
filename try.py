from datetime import datetime

# Create a kwargs dictionary with a created_at key and value
kwargs = {"created_at": "2021-09-23T13:02:11.123456"}

# Convert the string to a datetime object using the strptime() method
created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')

# Print the datetime object
print(created_at)
# Output: 2021-09-23 13:02:11.123456

