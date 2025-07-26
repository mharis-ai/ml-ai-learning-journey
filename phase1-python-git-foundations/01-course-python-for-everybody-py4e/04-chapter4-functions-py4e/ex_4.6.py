hours=input("Enter Hours: ")
rate=input("Rate Per Hour: " )
hours=float(hours)
rate=float(rate)
def computepay():
    if hours>40:
        rp = 40*rate
        op=(hours-40)*(rate*1.5)
        pay=op+rp
    else:
        pay = hours*rate
    return pay
print("Pay",computepay())
