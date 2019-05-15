#    Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------

#import csv file
import csv 
inputfile ="C:\\Users\\Karla Salome\\Desktop\\COLNYC201904DATA3\\homework\\03-Python\\Instructions\\PyPoll\\Resources\\election_data.csv"
#create an output text file
outputfile = "C:\\Users\\Karla Salome\\Desktop\\COLNYC201904DATA3\\homework\\03-Python\\Instructions\\PyPoll\\Resources\\election_output_data.txt"
# Create list for the csv file
polls = []
#create two dictionaries, candidate names and total number of voters per candidate
dict_polls = {}
dict_summary = {}
# Open file and assign to csvfile a name
with open(inputfile, newline='') as csvfile:
   # read
   # split the data on commas
   # assign to pollreader string variable
   # all in the same loop
   pollreader = csv.reader(csvfile, delimiter=',')
   # Skip header row one time
   next(pollreader)
   text_file = open(outputfile, "w")
   # print to text file
   text_file.write("Election Results")
   # Convert pollreader string to list
   for line in pollreader:
       polls.append(line)
   # print to text file
   text_file.write("\nTotal Votes: " + str(len(polls)))
   # print to to terminal
   print("Total Votes: " + str(len(polls)))
   # Output to text file
   text_file.write("\n-------------------------")
   # print to Terminal
   print("-------------------------")
   # Convert polls list into dictionary for counting and grouping candidate names 
   for line in polls:
       name_key = line[2]
       if name_key not in dict_polls:
           # insert name_key into dictionary Summary and initialize to 0
           dict_polls[name_key] = 0
       # count the name key inside dictionary
       dict_polls[name_key] += 1
# Print to Terminal
   print("\nKarla Salome Pratts\n \n-ELECTION RESULTS-")
   # print to text file
   text_file.write("\n-------------------------")
   # Print to Terminal
   print("-------------------------")
   # Compute the percentages of each name key of dict_polls and insert into dict_summary with 'len' to return number of items inside polls
   total_polls = len(polls)
   for name in dict_polls:
       dict_summary[name] = round((dict_polls[name] / total_polls) * 100)
       # print to text file
       text_file.write("\n" + str(name) + ": " + str(dict_summary[name]) + "% " + "(" + str(dict_polls[name]) + ")")
       # Print to Terminal
       print(str(name) + ": " + str(dict_summary[name]) + "% " + "(" + str(dict_polls[name]) + ")")

   # highest value
   highest = 0
   # Find larget value of the key/value pair inside dictionary and place the key name inside winner
   for name in dict_summary:
       if highest < dict_summary[name]:
           highest = dict_summary[name]
           winner = name

   # print to text file
   text_file.write("\n-------------------------")
   # Print to Terminal
   print("-------------------------")
   # print to text file
   text_file.write("\nWinner: " + winner)
   # Print to Terminal
   print("Winner: " + winner)
   # print to text file
   text_file.write("\n-------------------------")
   # Print to Terminal
   print("-------------------------")

# Close text file
text_file.close()
