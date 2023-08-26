# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Demonstrate examples of Exception Handling and Pickling
# Changelog (Who, When, What):
# Arlo Magpoc, 8/20/2023, Created Script
# ------------------------------------------------------------------------ #

# Exception Handling and Pickling Demonstration

import pickle  # Imports code from another code file

# Data variables
strFileName = 'EmployeeID.dat'
lstCustomer = []

print('\nWelcome to our Employee Creation Portal. Please enter information below\n')

def save_data_to_file(file_name, list_of_data):
    objFile = open(file_name, "ab")
    pickle.dump(list_of_data, objFile)
    objFile.close()

def read_data_from_file(file_name):
    file = open(file_name, "rb")
    list_of_data = pickle.load(file)
    file.close()
    return list_of_data

intId = input("Please enter your Employee Id: ") # Get Employee ID and NAME From user, then store it in a list object
strName = str(input("Please enter your name: "))
lstCustomer = [intId, strName]

try: # Starts the Try Clause
    if intId.isnumeric() == False:
        raise Exception('Please only use numbers for Employee ID.')
    if strName.isnumeric() == True:
        raise Exception('Don\'t use numbers for Employee name.')

except Exception as e: # The Exception Clause
    print("There was an error:")
    print(e, e.__doc__, type(e), sep='\n')

save_data_to_file(strFileName, lstCustomer) # Stores the list object into a binary file

# Reads  data from the file into a new list object. Displays Contents
print("Employee ID: ")
print(read_data_from_file(strFileName)[0], '\n')
print("Employee Name: ")
print(read_data_from_file(strFileName)[1])

input()