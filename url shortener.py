import pyshorteners

long_url = "www.http://www.thisisaverylongurlanditwouldbegoodifitwereshorter.com"

type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)
print(short_url)