import csv
from datetime import datetime
from matplotlib import pyplot as plt
import sys  # Importing sys for the exit path

filename = 'sitka_weather_2018_simple.csv'

# Load data from the file
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, highs, and lows
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing or invalid data for row: {row}")
            continue
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

while True:
    choice = input("Choose to display the High temp by entering H, Low temp by entering L, or to exit enter Exit: ").strip().upper()

    if choice == 'H':
        # Plot the high temperatures
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily High Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()
        print("Plot displayed. You may choose again or exit.")
    elif choice == 'L':
        # Plot the low temperatures
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue') #changed low to blue
        plt.title("Daily Low Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()
        print("Plot displayed. You may choose again or exit.")
    elif choice == 'EXIT':
        print("Now Exiting.") #exit message
        sys.exit()
    else:
        print("Invalid input. Please enter H, L, or Exit.") #error handling
