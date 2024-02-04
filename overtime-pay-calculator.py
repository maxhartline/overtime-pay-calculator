def main():

    #User input 
    pay_rate = float(input("Enter your pay rate per hour: $"))
    hours_worked = float(input("Enter the number of hours worked: "))

    #Calculate pay
    pay = pay_rate * hours_worked

    #Calculate and output total pay if hours under 40
    if hours_worked < 40:   
        print(f"Your total pay is ${pay:.2f}")

    #Calculate and output total pay if hours over 40
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        overtime_total_pay = pay + overtime_pay
        print(f"Your total pay is ${overtime_total_pay:.2f}")

if __name__ == "__main__":
    main()  