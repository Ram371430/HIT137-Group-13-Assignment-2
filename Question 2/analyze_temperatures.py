import os
import pandas as pd

# Define the path to the folder containing the CSV files
temperatures_folder = "temperatures"

# Initialize data structures for calculations
monthly_totals = {month: 0 for month in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]}
monthly_counts = {month: 0 for month in monthly_totals}
station_ranges = {}
station_averages = {}

# Process each CSV file in the folder
for filename in os.listdir(temperatures_folder):
    if filename.endswith(".csv"):
        filepath = os.path.join(temperatures_folder, filename)
        data = pd.read_csv(filepath)

        # Update totals and counts for monthly averages
        for month in monthly_totals.keys():
            monthly_totals[month] += data[month].sum()
            monthly_counts[month] += data[month].count()

        # Calculate temperature range for each station
        for _, row in data.iterrows():
            station_name = row["STATION_NAME"]
            monthly_temps = row[["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]]
            temp_range = monthly_temps.max() - monthly_temps.min()

            if station_name not in station_ranges:
                station_ranges[station_name] = temp_range
            else:
                station_ranges[station_name] = max(station_ranges[station_name], temp_range)

            # Calculate average temperature per station
            if station_name not in station_averages:
                station_averages[station_name] = []
            station_averages[station_name].extend(monthly_temps.dropna().tolist())

# Calculate the average temperature for each month
monthly_averages = {month: monthly_totals[month] / monthly_counts[month] for month in monthly_totals}

# Save monthly averages to a file
with open("average_temp.txt", "w") as file:
    file.write("Average Temperatures for Each Month:\n")
    for month, avg_temp in monthly_averages.items():
        file.write(f"{month}: {avg_temp:.2f}\n")

# Find the station(s) with the largest temperature range
max_range = max(station_ranges.values())
largest_range_stations = [station for station, temp_range in station_ranges.items() if temp_range == max_range]

with open("largest_temp_range_station.txt", "w") as file:
    file.write("Station(s) with the Largest Temperature Range:\n")
    for station in largest_range_stations:
        file.write(f"{station}\n")

# Find the warmest and coolest station(s)
station_avg_temps = {station: sum(temps) / len(temps) for station, temps in station_averages.items()}
max_avg_temp = max(station_avg_temps.values())
min_avg_temp = min(station_avg_temps.values())

warmest_stations = [station for station, avg_temp in station_avg_temps.items() if avg_temp == max_avg_temp]
coolest_stations = [station for station, avg_temp in station_avg_temps.items() if avg_temp == min_avg_temp]

with open("warmest_and_coolest_station.txt", "w") as file:
    file.write("Warmest Station(s):\n")
    for station in warmest_stations:
        file.write(f"{station}\n")
    file.write("\nCoolest Station(s):\n")
    for station in coolest_stations:
        file.write(f"{station}\n")

print("Analysis complete. Results saved to files.")
