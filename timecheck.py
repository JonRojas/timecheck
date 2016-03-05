import datetime
daysOfWeek = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
holidays = ['2/15/16', '5/28/16', '05/30/16', '7/2/16', '7/4/16', '9/3/16', '9/5/16', '11/24/16', '11/25/16', '11/26/16', '12/24/16', '12/25/16', '12/26/16', '12/31/16']
parsedHolidays = []
for d in holidays:
    d = datetime.datetime.strptime(d, "%m/%d/%y")
    parsedHolidays.append(d)

def printDate(date):
    return date.strftime('%m/%d/%y')

# Get starting date
print("What is the starting date? (mm/dd/yy)")
i = str(input())

# Convert input to datetime object
startDate = datetime.datetime.strptime(i, "%m/%d/%y")

# Print startDate
print("You entered: {:%m/%d/%Y}".format(startDate))

# Check which day of the week it starts on
startDay = startDate.weekday()
print("This class starts on " + daysOfWeek[startDay])

# Find out how many weeks to run
print("How many weeks is this class?")
duration = int(input())

# THE LOOP!
n = duration * 2
c = 1

# set up a toggle between 2 and 5 a la http://stackoverflow.com/questions/8381735/toggle-a-value-in-python
A = 2
B = 5
total = A + B
nextInc = A

dates = []
dates.append(printDate(startDate))
print(str(c) + ": " + printDate(startDate))
# handle starting on a Wed/Thursday
if startDay == (2 or 3):
    nextInc = 5

# trigger the main loop alternating between 2 and 5
nextDate = startDate
while c < (n):
    nextDate = nextDate + datetime.timedelta(days=nextInc)
    if nextDate in parsedHolidays:
        print("HOLIDAY: " + printDate(nextDate))
        nextInc = total - nextInc
        continue
    dates.append(printDate(nextDate))
    c = c + 1
    print(str(c) + ": " + printDate(nextDate))
    nextInc = total - nextInc
