orig_timestamp = input('\nWhat timestamp do you want to convert to seconds?\nUse the format 5.17, 1.30, etc. No hours for now--you can only use one period. > ')
orig_seconds = int(orig_timestamp)[:-2]
period_index = orig_timestamp.find('.')
orig_minutes = int(orig_timestamp)[:period_index]
orig_min_as_sec = orig_minutes * 60
total_seconds = orig_min_as_sec + orig_seconds
print(f'\nFor a YouTube timestamp, use:\t{total_seconds}\n')
