# Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.

def converted_date(date):
    month, day, year = date.split('/')
    return year + day.zfill(2) + month.zfill(2)
