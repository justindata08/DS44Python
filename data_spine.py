from datetime import datetime, timedelta

start = input('Pick a start date in proper format (YYYY-MM-DD): ')
end = input('Pick an end date in proper format (YYYY-MM-DD): ')

start = datetime.strptime(start, '%Y-%m-%d')
end = datetime.strptime(end, '%Y-%m-%d')

while start < end:
    print(start)
    start = start + timedelta(days=1)