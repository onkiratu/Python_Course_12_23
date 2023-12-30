# meal.py

def convert(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours + minutes / 60

def main():
    time_input = input("Enter the time (24-hour format as #:## or ##:##): ")
    time = convert(time_input)

    # Define meal times
    breakfast_start, breakfast_end = 7, 8   # 7:00 - 8:00
    lunch_start, lunch_end = 12, 13         # 12:00 - 13:00
    dinner_start, dinner_end = 18, 19       # 18:00 - 19:00

    if breakfast_start <= time <= breakfast_end:
        print("It's breakfast time.")
    elif lunch_start <= time <= lunch_end:
        print("It's lunch time.")
    elif dinner_start <= time <= dinner_end:
        print("It's dinner time.")

if __name__ == "__main__":
    main()
