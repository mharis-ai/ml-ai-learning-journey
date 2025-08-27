score=input("Enter Your Score: ")
try:
    score=float(score)
    if score<0.0 or score >1.0:
        print("Error: Score is out of range. Please enter a value between 0.0 and 1.0.")
    elif score>=0.9:
        print("Grade: A")
    elif score>=0.8:
        print("Grade: B")
    elif score>=0.7:
        print("Grade: C")
    elif score>=0.6:
        print("Grade: D")
    else:
        print("Grade: F")
except:
    print("Error: Invalid input. Please enter a numeric value.")