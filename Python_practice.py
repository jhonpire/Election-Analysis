# print("Hello World")

# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# print("Hello World")
# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[3] != 'Jefferson':
#     print(counties[2])

counties = ["Arapahoe","Denver","Jefferson"]
#Logical Operators
# if "El Paso" in counties:
#     print ("El Paso is in the list of counties.")
# else:
#     print("El Paso is not in the list of counties.")

#Combined Membership and Logical Operators uring "and"
# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")

#Combined Membership and Logical Operators uring "or"
# if "Arapahoe" in counties or "El Paso" in counties:
#     print("Arapahoe or El Paso is in the list of counties.")
# else:
#     print("Arapahoe and El Paso are not in the list of counties.")

#Combined Membership and Logical Operators uring "Not"
# if "Arapahoe" in counties and "El Paso" not in counties:
#    print("Only Arapahoe is in the list of counties.")
# else:
#     print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

#For loop practice
# for county in counties:
#     print(county)

# Using range function
# for num in range(5):
#     print(num)

#Using range function grabbing the length of the list
# for i in range(len(counties)):
#     print(counties[i])

counties_tuples = ("Arapahoe","Denver","Jefferson")

# for i in range(len(counties_tuples)):

#       print(counties_tuples[i])

#Declaring a Dictionary with the counties and their registered voters
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#Iterate Through a Dictionary
# for county in counties_dict:
#     print(county)

#Iterate Through Keys
# for county in counties_dict.keys():
#     print(county)

# Get the Velues from a Dictionary
# for voters in counties_dict.values():
#     print(voters)

# for county in counties_dict:
#     print(counties_dict[county])

# for county in counties_dict:
#     print(counties_dict.get(county))

#Obtain Key and values in Dictionary
# for key, value in counties_dict.items():
#     print(key, value)

# for county, voters in counties_dict.items():
#     print(county, voters)

#SKILL DRILL
# for county, voters in counties_dict.items():
#     print (county,"county has", voters, "voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

# for i in len(voting_data):
#       print(voting_data[i])

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

#Retrieving the registered voters of each county
# for county_dict in voting_data:
#      print(county_dict['registered_voters'])

#To print only the county names from the List of Dictionaries
# for county_dict in voting_data:
#     print(county_dict['county'])

#Code previous to reformatting with F-String
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

#Reformatted code implementing F-Strings
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# #Using for loops with dictionaries printing both keys and values
# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")

# Implementing F-Strings to simplify printing information from dictionaries
# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

#Multiline F-Strings
# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# print(message_to_candidate)

#SKILL DRILL 2
for county, voters in counties_dict.items():
    print (f'{county} county has {voters:,} registered voters')

    