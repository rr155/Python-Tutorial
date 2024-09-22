# strip removes whatever is passed as a argument for the string from left most and right most only.  
# By default it removes space if no argument is passed and doesnt remove anything that comes in between.

var = '  Hello World   '
print(var.strip())
print(var.rstrip())

tempstring = 'ftp://ftp.ncdc.noaa.gov/pub/data/noaa'
print(tempstring.split(':')[1].strip('//'))
