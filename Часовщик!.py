from datetime import datetime

a = int(input("Enter numbers: "))

s = datetime.fromtimestamp(a).strftime('%d %A %H:%M:%S')

print("Converted numbers to seconds: " + str(s))
