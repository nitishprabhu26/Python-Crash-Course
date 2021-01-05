# Dictionaries - special structure which allows to store info in key-value pairs

month_conversions= {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sept" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}

# print(month_conversions["oct"])
# KeyError: 'oct'
print(month_conversions["Oct"])
# using get function, we can specify default value
print(month_conversions.get("nov", "Not a valid key"))