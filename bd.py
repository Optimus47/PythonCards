from datetime import datetime 

bday = "20/11"

# print birthday date
print("Your next bd is on",datetime.strptime(f"{bday}/{datetime.today().year}", "%d/%m/%Y").strftime("%d/%m/%Y"))
# print day of the week
print("Your bd is on",datetime.strptime(f"{bday}/{datetime.today().year}", "%d/%m/%Y").strftime("%A"))
# print days left for birthday
today = datetime.today()
bday = datetime.strptime(f"{bday}/{datetime.today().year}", "%d/%m/%Y")
#if bday < today:
#    bday = datetime.strptime(f"{bday.day}/{bday.month}/{datetime.today().year + 1}", "%d/%m/%Y")
days_left = (bday - today).days
print("Days left for your bd",days_left)
# print today date  
print("today",datetime.today())

