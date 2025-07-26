largest = None
smallest = None
while True:
    integers = input("Enter Integers: ")
    if integers == "done":
        break
    try:
        integers = int(integers)
    except:
        print("Invalid input")
        continue
    if largest is None or integers>largest:
        largest = integers
    if smallest is None or integers<smallest:
        smallest = integers
print("Maximum is",largest)
print("Minimum is",smallest)