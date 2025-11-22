orig_timestamp = input('What timestamp do you want to convert to seconds?\nUse the format 5.17, 1.30, etc.\nNo hours for now, and you can only use one period.\nNo error handling yet. >>\t')
orig_seconds = int(orig_timestamp.split('.')[1])
orig_minutes = int(orig_timestamp.split('.')[0])
orig_min_as_sec = orig_minutes * 60
total_seconds = orig_min_as_sec + orig_seconds
print(f'\nFor a YouTube timestamp, use:\t{total_seconds}\n')

# to do--
# - add option to convert multiple timestamps,
# - - i.e. run loop the script
# - maybe remove additional \n
# - add error handling
# - later--add hours as an option, but not necessary for now
# - might be cool to add the youtube URL as a variable,
# - - and have tsc.py generate the entire link incl &t=___,
# - - instead of adding that manually
# - possibly send that link to system clipboard using pyperclip [Sweigart]
