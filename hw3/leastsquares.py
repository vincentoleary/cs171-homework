# Vincent O'Leary (vjo25)
# Assignment 3 for CS 171-064
# Linear Regression Generator

# import used libraries
import sys
import csv
import math

# Print a welcome statement
print('Welcome to Linear Regression Generator')

# Ask for a new file name and save it a var
input_file_name=input('Enter File Name Containing Data: ')

# Try to open the file, or fail gracefully if any errors
try:
    csv_data_import = {}

    with open(input_file_name,'r') as csvfile:
        csv_file_import = csv.reader(csvfile, delimiter=',')

        first_row = True

        for row in csv_file_import:
            if first_row:
                # Assign the var titles from first row before saving data
                x_axis_title = row[0]
                y_axis_title = row[1]

                # Now skip the first row with column names and then save data
                first_row = False
                continue

            x_axis_value = row[0]
            y_axis_value = row[1]

            # Assign the corrct type to each var
            x_axis_value = int(x_axis_value)
            y_axis_value = float(y_axis_value)

            # Create a dictionary of values x,y
            csv_data_import[x_axis_value] = y_axis_value

# Exit program if file does not exist, but do it gracefully
except FileNotFoundError as e:
    print('Sorry, I couldn\'t find the file you wanted.\nI have to exit the program now.\nGoodbye!')
    sys.exit()
# Exit program if file has bad values, but do it gracefully
except ValueError as e:
    print('Sorry, that file has a bad or missing value.\nI have to exit the program now.\nGoodbye!')
    sys.exit()

# Calculate the average value for x and y

# n be the number of known values
number_known_values = len(csv_data_import)

# x is the ith known x-axis value
x_sum = 0
for x in csv_data_import.keys():
    x_sum = x_sum + x

# x_a is the average of all x-values
x_average = int(x_sum/number_known_values)

# y is the ith known y-axis value
y_sum = 0
for y in csv_data_import.values():
    y_sum = y_sum + y

# y_a is the average of all y-values
y_average = float(y_sum/number_known_values)

# Calculate the slope and intercept of the regression

# The slope (m) can be computed as
m_num = 0
m_den = 0
for x,y in csv_data_import.items():
    m_num = m_num + ((x - x_average)*(y - y_average))
    m_den = m_den + ((x - x_average)**2)

m_slope = m_num / m_den

# The intercept (b) can be computed from the averages as
b_intercept = y_average-(m_slope*x_average)

# Calculate the average error of the regression equation
error_sum = 0
for x,y in csv_data_import.items():
    error_sum = error_sum + (abs(y - (m_slope*x+b_intercept)))

error_ave = error_sum / number_known_values

# Calculate the standard error of the regression
error_square = 0
for x,y in csv_data_import.items():
    error_square = error_square + ((y - (m_slope*x+b_intercept))**2)

mean_std_error = (1/(number_known_values - 2)) * error_square
std_error = math.sqrt(mean_std_error)

# If file is found, print the summary statistics
print('The Linear Regression Equation is y = '+str(m_slope)+' * x + '+str(b_intercept))
print('The Average Error for Known Values is +/- '+str(error_ave))
print('The Regression Standard Error for Known Values is '+str(std_error))

# Explain how the program will work
print('I am now ready to make some predictions!')
print('To quit, type \'exit\' instead of a value.')

# Define a function to make a prediction
def prediction(x):
    return (m_slope*int(x)) + b_intercept

# Run the main program
if __name__=='__main__':
    predict_my_value=input('Enter a value: ')
    # If the user enters a value, make a prediction, otherwise print the error and try again
    while predict_my_value != 'exit':
        try:
            y_guess = prediction(predict_my_value)
            print('My prediction when the',x_axis_title,'is',predict_my_value,'is that',y_axis_title,'will be approx.',y_guess)
        except ValueError as e:
            print('That is not a value I understand, try again.')
        except TypeError as e:
            print('That is not a value I understand, try again.')
        # Continue to ask the user for a value to make a new prediction
        predict_my_value=input('Enter another value: ')
    # If the user enters 'exit' and leaves the program, exit gracefully
    print('Done already?\nGoodbye! Come back again soon.')
