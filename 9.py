"""Python program to calculate gross pay (Hourly paid employee) using class and Object.
Take the input as No. of Hour work and any extra hours work.
The payments made to the employee are based on the hours he has worked. Ideal
working hours per day is 8 hours and for that 1500 is paid to the employee.
The calculation of salary based on hours worked is,
Hours worked = 8, payment = 1500.
Hours worked < 8, pay less, 75 per hour.
Hours worked > 8, pay more, 75 per hour"""


class Employee:
    def __init__(self, hours_worked, extra_hours):
        self.hours_worked = hours_worked
        self.extra_hours = extra_hours

    def calculate_gross_pay(self):
        if self.hours_worked > 8:
            return 1500 + ((self.hours_worked + self.extra_hours) - 8) * 75
        elif self.hours_worked == 8:
            return 1500
        else:
            return self.hours_worked * 75



if __name__ == "__main__":
    hours_worked = int(input("Enter hours worked: "))
    extra_hours = int(input("Enter extra hours worked: "))

    employee = Employee(hours_worked, extra_hours)

    print("The gross pay of the employee",
          employee.calculate_gross_pay())
