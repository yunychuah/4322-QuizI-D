'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
infile = open('employee_data.csv', 'r')

csvfile = csv.reader(infile)

next(csvfile)

#create an empty dictionary
dictionary = {}

#use a loop to iterate through the csv file
#full employee name as key, new salary as value
for row in csvfile:
    name = row[1]+ ' ' +row[2]
    salary = row[5]
    dictionary = {name:salary}

    new_salary = (int(salary)*0.1)+int(salary)

    #check if the employee fits the search criteria
    if row[4] == 'CSR':
        print('Manager Name:',name,'Current Salary:',salary)
        dictionary[salary] = new_salary
       

print()
print('=========================================')
print()
for key, value in dictionary.items():
    print(f'Manager Name: {name} New Salary: {new_salary}')

#for key,value in dictionary:
    #print('Manager Name: {key} New Salary: {value}')
#iternate through the dictionary and print out the key and value as per printout
#for key, value in dictionary:
    #print(f'Manager Name: {key} New Salary: {value}')



          
        

        
    
