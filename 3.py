# function to check if year is leap year
def check_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
            else:
                print("Not a leap year")
        else:
            print("Leap year")
    else:
        print("Not a leap year")
        
if __name__ == "__main__":
  print(check_leap_year(int(input("Enter a year: "))))
