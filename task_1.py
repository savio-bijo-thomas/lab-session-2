from datetime import datetime

now = datetime.now()

print("Current date and time:", now)

print("Format [YYYY-MM-DD HH:MM:SS]:", now.strftime("%Y-%m-%d %H:%M:%S"))

print("Format [MM/DD/YYYY]:", now.strftime("%m/%d/%Y"))

print("Format [Day, Month DD, YYYY]:", now.strftime("%A, %B %d, %Y"))

print("Format [Day, Month DD, YYYY HH:MM:SS AM/PM]:", now.strftime("%A, %B %d, %Y %I:%M:%S %p"))

formatted_date = now.strftime("%a-%b-%d %H:%M:%S IST %Y")
print("Format [Abbr Weekday Name-Abbr month name-DD HH:MM:SS IST YYYY]:", formatted_date)

print("ISO format:", now.isoformat())

print("Date only:", now.strftime("%Y-%m-%d"))

print("Time only:", now.strftime("%H:%M:%S"))

print("Month only:", now.strftime("%B"))

print("Year only:", now.strftime("%Y"))