#print('hello world')
import calendar

def generate_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    print("  S  M  T  W  T  F  S")
    for week in cal:
        for day in week:
            if day == 0:
                print(" may   ", end="")
            else:
                print(f"{day:2} ", end="")
        print()

if __name__ == "__main__":
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    generate_calendar(year, month)
