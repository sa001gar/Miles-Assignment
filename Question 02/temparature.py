import pandas as pd
import matplotlib.pyplot as plt
import os


file_name = 'temperature_data.csv'

# Check if the file exists
if not os.path.exists(file_name):
    print(f"Error: {file_name} not found.")

else:
    try:
        # Read the CSV
        data = pd.read_csv(file_name, usecols=['date', 'temperature']).dropna()

        # Check if the file is empty
        if data.empty:
            print(f"Error: The file {file_name} is empty.")
        else:
            # Convert the 'date' column to datetime format
            data['date'] = pd.to_datetime(data['date'])

            # Find the highest and lowest temperatures
            max_temp = data['temperature'].max()
            min_temp = data['temperature'].min()

            max_temp_date = data.loc[data['temperature'] == max_temp, 'date'].iloc[0]
            min_temp_date = data.loc[data['temperature'] == min_temp, 'date'].iloc[0]

            # Create the line plot
            plt.figure(figsize=(10, 6))
            plt.plot(data['date'], data['temperature'], marker='o', color='b', label='Temperature')

            # Annotate highest and lowest temperatures
            plt.annotate(f'{max_temp}°C on {max_temp_date.date()}', 
                         xy=(max_temp_date, max_temp), 
                         xytext=(max_temp_date, max_temp + 1), 
                         arrowprops=dict(facecolor='red', arrowstyle='->'),
                         fontsize=9, color='red')

            plt.annotate(f'{min_temp}°C on {min_temp_date.date()}', 
                         xy=(min_temp_date, min_temp), 
                         xytext=(min_temp_date, min_temp - 2), 
                         arrowprops=dict(facecolor='green', arrowstyle='->'),
                         fontsize=9, color='green')

            # Set labels and title
            plt.xlabel('Date')
            plt.ylabel('Temperature (°C)')
            plt.title('Daily Temperature Variations')
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.legend()

            # Show the plot
            plt.tight_layout()
            plt.show()

    except pd.errors.EmptyDataError:
        print(f"Error: The file {file_name} is empty or could not be parsed.")
    except Exception as e:
        print(f"An error occurred: {e}")
