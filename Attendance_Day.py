class Attendance_day:

    def __init__(self):
        self.__daily_attendance = []

    def get_attendance(self):
        return self.__daily_attendance

    def set_attendance(self, emploee):
        self.__daily_attendance = emploee

    def mark_attendance(self, employee):
        self.__daily_attendance.append(employee)

    def show(self):
        for i in self.get_attendance():
            per_day_pay = 0#emp.get_hpay() * 8
            #print("The Pay Per Day " + emp.fullname() + ", " + per_day_pay)

    def calc_total_pay(self):
        gross_pay = 0
        for i in self.get_attendance():
            print("")#gross_pay += emp.get_hpay() * 8
            
        return gross_pay

monday = Attendance_day()

for i in 10:#emp_list :
    present = input("Is employee " + i.fullname() + "Present?\n" + "Yes or No (Enter)")
    if present == "y" or present == "Y":
        monday.mark_attendance(i)

    else:
        print("")
        




