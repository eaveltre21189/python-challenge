# python-challenge

Created script to read two csv files, analyze the data, and generate a report of the analysis as a new file:

PyBank:

    * Imported and read the source data file
    * Calculated the total number of months (rows) in the data set
    * Calcluated the total amount of profits or losses over the entire period
    * Calculated the change in profits/losses for each month (prior month's profit/loss - current month's profit loss)
    * Then, from the above, calculated the average monthly change in profits/losses over the entire period
    * Identified the month with the greatest profit and the month with the greatest loss, with their respective amounts
    * Printed a report of the data analysis to the terminal and as a new TXT file

PyPoll:

    * Imported and read the source data file
    * Calculated the total number of votes cast (total number of ballots)
    * Created a list of all possible candidates from the population
    * For each candidate, calculated the total number of votes, and percent of total votes
    * Based on individual candidate data, determine the winner of the election
    * Printed a report of the election results to the terminal and as a new TXT file