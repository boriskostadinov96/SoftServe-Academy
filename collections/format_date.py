def format_date(str_date):
    month, day, year = str_date.split("/")
    return f"{year}-{day}-{month}"


print(format_date("11/12/2019"))
print(format_date("12/31/2019"))
print(format_date("01/15/2019"))
