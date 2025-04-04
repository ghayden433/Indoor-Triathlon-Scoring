import pandas as pd
import numpy as np

# each of the three event titles, to iterate through
events = ["Swim Distance (Yards)", "Bike Distance (Miles)", "Run Distance (Miles)"]
# read in the results excel sheet as a pandas dataframe
results = pd.read_excel('OSU INDOOR TRIATHLON 2025 RESULTS.xlsx', index_col=0)

for event in events:
    # calculate the mean and standard deviation for one event
    mean = np.mean(results[event])
    std_dev = np.std(results[event])

    # calculate standard deviations above/below the mean for each person
    temp_std_dev_results = list()
    for result in results[event]:
        temp_std_dev_results.append((result - mean) / std_dev)

    # add the standard deviations to the dataframe for each event
    results[event + " std_dev"] = temp_std_dev_results

# find the average standard deviations from the mean for each participant and store it in a column called averageStdDev
results['average_std_dev'] = (results[events[0] + " std_dev"] + results[events[1] + " std_dev"] + results[events[2] + " std_dev"]) / 3

# sort the by average standard deviations from mean, create a column for the new places aftwer rescore
results = results.sort_values(by='average_std_dev', ascending=False)
results.insert(0, 'Rescore Place', [i+1 for i in range(len(results))])

# send to an excel sheet
try:
    results.to_excel("Output.xlsx")
except:
    print("Permission Denied: Please close the excel sheet or ensure valid permission")

