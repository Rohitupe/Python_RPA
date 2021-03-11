# count = 0
#
# with open('cardnumber.txt', 'a') as f:
#     f.writelines(f"{count}\n")

number, points, email = 23231454, 20, 'rohit@gmail.com'

from csv import DictWriter

with open("H&M.csv", 'a', newline='') as csvF:
    csv_writer = DictWriter(csvF, fieldnames=["Loyalty card number", "Points balance", "Email Id"])
    if csvF.tell() == 0:
        csv_writer.writeheader()
    csv_writer.writerow({
        "Loyalty card number" : number,
        "Points balance" : points,
        "Email Id" : email
    })

