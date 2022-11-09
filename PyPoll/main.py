import os
import csv

# Specify path for csv file
csv_path=os.path.join("Resources","election_data.csv")

# Open and read csv skipping the header row
with open(csv_path,"r") as csv_file:
    
    election_data=csv.reader(csv_file,delimiter=",")

    next(election_data)

# Read through each row of data and create a list for Candidates

    Candidates=[]

    for row in election_data:

        Candidates.append(row[2])

# Print the total votes by obtaining length of list

    print("Election Results")

    print("------------------------------------")

    print("Total Votes: " +str(len(Candidates)))

    print("------------------------------------")

# Identify all unique candidate names and store in an alphabetically sorted list
    candidate_names = list(set(Candidates))
    candidate_names_sorted=sorted(candidate_names)

# Create lists for each candidate by sorting through all the names

    candidate_1=[]
    candidate_2=[]
    candidate_3=[]
    for candidate in Candidates:
        if candidate == candidate_names_sorted[0]:
            candidate_1.append(Candidates)
        
        elif candidate == candidate_names_sorted[1]:
            candidate_2.append(Candidates)

        elif candidate==candidate_names_sorted[2]:
            candidate_3.append(Candidates)

# Obtain number of votes for each candidate

    candidate_1_votes=len(candidate_1)
    candidate_2_votes=len(candidate_2)
    candidate_3_votes=len(candidate_3)

# Calculate % of votes for each candidate

    percentage_1=round((candidate_1_votes/len(Candidates))*100,3)
    percentage_2=round((candidate_2_votes/len(Candidates))*100,3)
    percentage_3=round((candidate_3_votes/len(Candidates))*100,3)

# Pring number of votes and percenatge of votes for each candidate

    print(candidate_names_sorted[0]+": "+str(percentage_1)+"% "+"(" +str(len(candidate_1))+")")
    print(candidate_names_sorted[1]+": "+str(percentage_2)+"% "+"(" +str(len(candidate_2))+")")
    print(candidate_names_sorted[2]+": "+str(percentage_3)+"% "+"(" +str(len(candidate_3))+")")
    print("------------------------------------")

# Find the winner

    percentages=[percentage_1,percentage_2,percentage_3]

    winner_percentage= max(percentages)

    if winner_percentage==percentage_1:
        print("Winner: "+candidate_names_sorted[0])
        print("------------------------------------")

    elif winner_percentage==percentage_2:
        print("Winner: "+candidate_names_sorted[1])
        print("------------------------------------")
        
    elif winner_percentage==percentage_2:
        print("Winner: "+candidate_names_sorted[2])
        print("------------------------------------")

# Export to a text file

output_path = os.path.join("Analysis","Analysis.txt")
with open(output_path,"w") as txt_file:

    print("Election Results", file=txt_file)

    print("------------------------------------", file=txt_file)

    print("Total Votes: " +str(len(Candidates)), file=txt_file)

    print("------------------------------------",file=txt_file)

    print(candidate_names_sorted[0]+": "+str(percentage_1)+"% "+"(" +str(len(candidate_1))+")", file=txt_file)
    print(candidate_names_sorted[1]+": "+str(percentage_2)+"% "+"(" +str(len(candidate_2))+")", file=txt_file)
    print(candidate_names_sorted[2]+": "+str(percentage_3)+"% "+"(" +str(len(candidate_3))+")",file=txt_file)
    print("------------------------------------",file=txt_file)

    print("Winner: "+candidate_names_sorted[1], file=txt_file)
    print("------------------------------------", file=txt_file)


    