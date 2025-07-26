hours=input("Enter Hours: ")
rate=input("Enter Rate Per Hour: ")
hours=float(hours)
rate=float(rate)
if hours>40:
    rp=40*rate #regular pay
    op=(hours-40)*(rate*1.5) #overtime pay
    pay=op+rp
    print(pay)
else:
    pay=hours*rate
    print(pay)