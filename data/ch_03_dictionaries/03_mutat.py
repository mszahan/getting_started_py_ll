user_preferences = {
    'language': 'English',
    'font_size': '14px',
    'timezone': 'GMT',
    'currency': 'USD',
    'enable_location':False,
    'volume_level': 80,
    'date_format': 'MM/DD/YYYY'
}

for key, value in user_preferences.items():
    print(f'{key} - {value}')


## delete an item
del user_preferences['currency']

## delete and keep it in variable
## the second argument is for , if the key doesn't exist in the dict
removed_item = user_preferences.pop('date_format', 'N/A')

print(user_preferences)