while True:
    print("-----COMPANY B ALTERNATIVE PAYROLL-----")
    print("\t\t\t SET B")

    Amil_employee = input("Enter employee name: ").title()
    Amil_position = input("Enter Job position \nJanitor"
                          "\nClerk"
                          "\nCashier"
                          "\nManager\n").title()
    Amil_actual_hours = float(input("Enter actual hours worked: "))

    match Amil_position.lower():
        case"janitor":
            Amil_monthly_salary = 20000
        case "clerk":
            Amil_monthly_salary = 25000
        case "cashier":
            Amil_monthly_salary = 28000
        case "manager":
            Amil_monthly_salary = 45000
        case _:
            print("Invalid job position")
            exit()

    Amil_weekly_salary = Amil_monthly_salary / 4
    Amil_allowance = Amil_weekly_salary*0.05

    Amil_basic_salary = Amil_weekly_salary + Amil_allowance

    Amil_hourly_rate = Amil_basic_salary / 48

    Amil_absent_hours = 0
    Amil_absence_deduction = 0
    Amil_overtime_hours = 0
    Amil_overtime_rate = 0
    Amil_overtime_pay = 0

    if Amil_actual_hours < 48:
        Amil_absent_hours = 48 - Amil_actual_hours
        Amil_absence_deduction = (Amil_absent_hours * Amil_hourly_rate * 1.10)
    elif Amil_actual_hours > 48:
        Amil_overtime_hours = Amil_actual_hours - 48
        Amil_overtime_rate = Amil_overtime_hours * 1.50
        Amil_overtime_pay = (Amil_overtime_rate * Amil_overtime_rate)

    Amil_net_weekly_salary = (Amil_basic_salary - Amil_absence_deduction + Amil_overtime_pay)
    Amil_half_month_salary = Amil_weekly_salary * 2
    Amil_gross_half_month_salary = (Amil_basic_salary * 2)

    Amil_half_month_absence_deduction = (Amil_absence_deduction * 2)

    Amil_half_month_overtime_pay = (Amil_overtime_pay * 2)
    Amil_net_half_month_salary = (Amil_gross_half_month_salary - Amil_half_month_absence_deduction + Amil_half_month_overtime_pay)

    print("-----Payroll-----")
    print(f"Employee's name: {Amil_employee}\n"
          f"Job position: {Amil_position}\n"
          f"Actual Hours worked: {Amil_actual_hours:,.2f}\n"
          f"**************************\n"
          f"Monthly Salary: ${Amil_monthly_salary:,.2f}\n"
          f"Gross Basic Salary: ${Amil_basic_salary:,.2f}\n"
          f"Net weekly salary: ${Amil_net_weekly_salary:,.2f}\n"
          f"Hourly Rate: {Amil_hourly_rate:,.2f}\n"
          f"Absent: {Amil_absent_hours}\n"
          f"Absence deduction: {Amil_absence_deduction}\n")

    again = input("Do you want to enter again? (Y/N): " )

    if again.lower() != "y":
        print("Program ended.")
        break







