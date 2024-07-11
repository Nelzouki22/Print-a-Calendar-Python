import calendar

# Function to print calendar of a given month and year
def print_calendar(year, month):
    # Create a plain text calendar
    cal = calendar.TextCalendar(calendar.SUNDAY)
    # Print the month's calendar
    calendar_str = cal.formatmonth(year, month)
    print(calendar_str)

# Example usage
year = 2024
month = 7
print_calendar(year, month)

