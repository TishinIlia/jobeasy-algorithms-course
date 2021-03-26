# When a user enters a year, the code detects if it is a leap year or not.

# Leap years have the following characteristics:
# Their number is multiple by 400 or their number is multiple by 4.
# If the year number id multiple by 100, it is not a leap year.

year = int(input('Input a year: '))



# def is_leap_year(y):
#     if y % 4 == 0 and y % 100 != 0:
#         return True
#     elif y % 100 == 0:
#         return False
#     elif y % 400 ==0:
#         return True
#     else:
#         return False


print(is_leap_year(year))
