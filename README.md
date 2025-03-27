# Indoor-Triathlon-Scoring
Rescores the indoor triathlons using standard deviations rather than their equation\
I partook in the OSU indoor triathlon I am under the impression that they multiply each distance by a selected number to even out the distances and then those roughly equalized numbers are added together for a final score\
I figured that putting the distances on the day onto a normal distribution and using standard deviations to quantify the quality of a performance would produce a more equitable result across events. this ensures that the winner is the best performer on average relative to the performances of each athlete that competed in the event and eliminates error in converting swim distance to an "equivalent" run distance or similar errors between converting event distances.
I used pandas to read in the excel sheet as a dataframe, manipulated the data with numpy and sent the output to a separate Output.xlsx file.
