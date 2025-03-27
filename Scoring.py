import pandas as pd
import numpy as np

# each of the three event titles, to iterate through
events = ["Swim Distance (Yards)", "Bike Distance (Miles)", "Run Distance (Miles)"]
# read in the results excel sheet as a pandas dataframe
results = pd.read_excel('OSU INDOOR TRIATHLON 2025 RESULTS.xlsx', index_col=0)

for event in events:
    # calculate the mean and standard deviation for one event
    mean = np.mean(results[event])
    stdDev = np.std(results[event])

    # calculate standard deviations above/below the mean for each person
    tempStdDevResults = list()
    for result in results[event]:
        tempStdDevResults.append((result - mean) / stdDev)

    # add the standard deviations to the dataframe for each event
    results[event + " StdDev"] = tempStdDevResults

# find the average standard deviations from the mean for each participant and store it in a column called averageStdDev
results['averageStdDev'] = (results[events[0] + " StdDev"] + results[events[1] + " StdDev"] + results[events[2] + " StdDev"]) / 3

# sort by average standard deviations and send to an excel sheet
results.sort_values(by='averageStdDev', ascending=False).to_excel("Output.xlsx")

