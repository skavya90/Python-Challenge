import csv
import os

#path to csv file
csvpath = os.path.join('C:\\','users','skavy','Desktop','Bootcamp','Python-Challenge','PyPoll','election_data.csv')

voters = []
dict_election = {}

#Using csv module, open and read the file 
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    
    #Reads header row first
    header = next(csvreader)
    # Checks the rows as list in csvfile and remove duplicates
    election_data = list(csv.reader(csvfile, delimiter=','))
    
    #Loops through every row of csv file
    for row in election_data:
        
        voters.append(int(row[0]))
        candidate_name = (row[2])
        #Conditional for verifying candidate name in the row with items in dictionary
        if candidate_name in dict_election:
            dict_election[candidate_name] = dict_election[candidate_name] +1
        else:
            dict_election[candidate_name] = 1
            
           
print("Election Results")
print("----------------------------------")
print(f"Total Votes: {len(voters)}")  
print("----------------------------------") 

#Exporting text file            
output_file = os.path.join("Pypoll.txt")
# Writes output to text file
w = open('Pypoll.txt','w')
w.write("Election Results")
w.write("\n----------------------------------")
w.write(f"\nTotal Votes: {len(voters)}")  
w.write("\n----------------------------------")

#Loops through dictionary items  calculates percentage of votes for each candidate
for keys,values in dict_election.items():
    #calculates percentage of votes for each candidate
    vote_percent = ((values / len(voters)) * 100)
    print(f"{keys}: ({round(vote_percent, 2)}%) {values}")           
    w.write(f"\n{keys}: ({round(vote_percent, 2)}%) {values}")
print("----------------------------------") 
w.write("\n----------------------------------")
#Gets the key in dictionary with maximum number of votes
maximum = max(dict_election, key=dict_election.get)
print(f"Winner: {maximum}")
print("----------------------------------")

w.write(f"\nWinner: {maximum}") 
w.write("\n----------------------------------")

w.close()


    
        
        
    