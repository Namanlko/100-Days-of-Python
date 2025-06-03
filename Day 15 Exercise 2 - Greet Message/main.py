import time  # Importing the time module to access time-related functions
timestamp = time.strftime('%H:%M:%S')  # Format current time as HH:MM:SS (24-hour clock)
print(timestamp)  # Print the formatted time
timestamp = time.strftime('%H')  # Extract and format the current hour (24-hour clock)
print(timestamp)  # Print the hour
timestamp = time.strftime('%M')  # Extract and format the current minute
print(timestamp)  # Print the minute
timestamp = time.strftime('%S')  # Extract and format the current second
print(timestamp)  # Print the second
# Reference: https://docs.python.org/3/library/time.html#time.strftime