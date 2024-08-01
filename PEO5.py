def make_shirt(size, message):
    print(f"The shirt size is {size} and the message on it is '{message}'.")

# Calling the function with positional arguments
make_shirt('Medium', 'Hello, World!')

# Calling the function with keyword arguments
make_shirt(size='Large', message='Code')

def make_shirt(size='Large', message='Class 201'):
    print(f"The shirt size is {size} and the message on it is '{message}'.")

# Making a large shirt with default message
make_shirt()

# Making a medium shirt with default message
make_shirt(size='Medium')

# Making a shirt of any size with a different message
make_shirt(size='Small', message='Win')

def describe_city(city, country='USA'):
    print(f"{city} is in {country}.")

# Calling the function for three different cities
describe_city('New York')
describe_city('Madrid', country='Spain')
describe_city('Tokyo', country='Japan')

def show_messages(messages):
    for message in messages:
        print(message)

# List of short text messages
messages_list = ["Hello!", "Ready?", "Lets go!", "Goodbye!"]

# Passing the list to the function
show_messages(messages_list)

def count_upper_lower(s):
    upper_case = sum(1 for c in s if c.isupper())
    lower_case = sum(1 for c in s if c.islower())
    print(f"No. of Upper case characters: {upper_case}")
    print(f"No. of Lower case characters: {lower_case}")

# Sample string
sample_string = 'The quick Brow Fox'

# Counting upper and lower case characters
count_upper_lower(sample_string)
