# ⚠️ Requirements of assignments ⚠️
# At the top the file write you git user id ex: "@sumit-dev-01"
# 1. When you start your assignment, make sure you have to record your current work. If you on any system like windows or mac, you have start your screen recording.
# 2. Submit your work to "origin/assignments"
# 3. Submit your recording to "sumitpaul@cloudadda.net"
# 4. Follow this procedures to get a classmate note book 📒, if you successfully completed that assignment
# 5. When you start you assignment don't shift to another window, do not open any lecture file. Just answer the question, and submit your assignment to early mentioned destination.
# 6. Submit your raw recorded file, make sure that is not modified or edited...edited file not accepted 🚫
# 7. When you write your code and run that successfully, then "comment off" that code so that code would be ignored by python interpreter, when you run your next code. Because you can write multiple types of code on a single file. And saved your work securely because your code is checked by me" 


# QUESTION:-

# 1. Create a dictionary of students with their marks and write a program to calculate the average marks using a for loop.
# 2. Write a program that takes a dictionary of employee data (name and salary) and prints the names of employees with salaries greater than $50,000.
# 3. Using NumPy, create a dictionary where keys are integers from 1 to 10, and values are their squares. Print the dictionary.
# 4. Write a Python program to merge two dictionaries using the `update()` method and verify the result using a for loop.
# 5. Using Pandas, create a DataFrame from a dictionary and calculate the mean, median, and sum of a specific column.
# 6. Write a program to create a dictionary of fruits with their prices and calculate the total cost of buying 5 of each fruit using a while loop.
# 7. Using Pandas, read a CSV file containing employee data, filter out employees from a specific department, and convert the result back into a dictionary.
# 8. Write a program that takes a dictionary of students with their grades, sorts the dictionary by grades in descending order, and prints the result.
# 9. Create a NumPy array of random numbers and write a program to store their square roots in a dictionary with the original numbers as keys.
# 10. Using Pandas, create a DataFrame from a dictionary of lists, add a new column that calculates the sum of other columns, and print the updated DataFrame.
# 11. Write a program that checks if a specific key exists in a dictionary using a for loop. If it exists, print its value.
# 12. Using NumPy, create a dictionary where the keys are integers and the values are arrays of their multiples up to 10. Print the dictionary.
# 13. Create a program that takes a dictionary of product prices, increases the price of each product by 10%, and prints the updated dictionary.
# 14. Using Pandas, write a program to group a DataFrame by a specific column (e.g., department) and calculate the sum of another column (e.g., salary).
# 15. Write a program that takes a dictionary of tuples (student ID and name) as keys and their grades as values, and calculates the highest grade.
# 16. Using Pandas, read a CSV file into a DataFrame, replace all missing values with zeros, and export the updated DataFrame back to a new CSV file.
# 17. Write a Python program to count the frequency of each value in a dictionary and store the result in a new dictionary.
# 18. Using NumPy, write a program to generate an array of random numbers and store their squares and cubes in a dictionary with keys "squares" and "cubes".
# 19. Create a program that takes a dictionary of countries and their populations, filters out countries with populations greater than 1 million, and prints the result.
# 20. Using Pandas, create a DataFrame from a dictionary, apply a function to a specific column, and add a new column with the transformed data.
# 21. Write a program to find the intersection of keys from two dictionaries and store the result in a new dictionary.
# 22. Using NumPy, create a dictionary where keys are numbers from 1 to 5 and values are random arrays of 5 numbers each. Calculate the mean of each array.
# 23. Write a Python program that takes a dictionary of lists and converts it into a Pandas DataFrame.
# 24. Using Pandas, write a program to filter rows of a DataFrame where a specific column's value is greater than a threshold and convert the result into a dictionary.
# 25. Write a program to add a new key-value pair to a dictionary using both the `update()` method and direct assignment. Verify the changes.
# 26. Using NumPy, generate a random 2D array and create a dictionary where keys are row indices and values are the corresponding rows.
# 27. Write a Python program to combine two dictionaries and sum the values of keys that exist in both dictionaries.
# 28. Using Pandas, write a program to find the correlation between two columns of a DataFrame created from a dictionary.
# 29. Write a program that creates a dictionary from a list of tuples, where each tuple contains a key-value pair. Use a for loop to iterate through the list.
# 30. Using NumPy, create an array of random integers, count the occurrences of each integer, and store the results in a dictionary.
# 31. Write a Python program that takes a dictionary of lists and finds the length of the longest list using a while loop.
# 32. Using Pandas, create a DataFrame from a dictionary, calculate the row-wise sum, and store the sums in a new column.
# 33. Write a program that takes a nested dictionary and flattens it into a single dictionary with compound keys (e.g., "outer.inner").
# 34. Using NumPy, generate a dictionary where keys are unique random numbers, and values are arrays of their logarithms.
# 35. Write a Python program that filters out keys from a dictionary whose values are empty lists, strings, or None, and prints the cleaned dictionary.
# 36. Using Pandas, create a program to group a DataFrame by multiple columns and calculate aggregated statistics (e.g., mean, max).
# 37. Write a program that uses a for loop to iterate through a dictionary and prints each key-value pair on a new line.
# 38. Using NumPy, write a program to create a dictionary where keys are numbers from 1 to 10, and values are arrays of their factorials.
# 39. Create a program that converts a dictionary of tuples into a Pandas DataFrame, where the tuple elements become column values.
# 40. Using Pandas, write a program to read a CSV file, create a pivot table from the DataFrame, and export the result to a new CSV file.

# 41. Given an unstructured JSON-like dataset representing a chatbot's conversation logs, write a Python function that:
# 
# 1. Reads the unstructured data (captured from an AI's interaction).
# 2. Structures it into a more readable format (e.g., a pandas DataFrame or a SQL-compatible table).
# 3. Handles missing values and ensures that the resulting data is clean and standardized (e.g., timestamps in ISO format, consistent user-agent information).
# 4. Stores the structured data in a database or a CSV file for further analysis.
#
# The unstructured data might look something like this:
# 
# unstructured_data = [
#     {"timestamp": "2024-12-13T10:01:00", "user": "John", "message": "Hi there!"},
#     {"timestamp": "2024-12-13T10:01:30", "user": "AI", "message": "Hello! How can I assist you today?"},
#     {"timestamp": "2024-12-13T10:02:00", "user": "John", "message": "I need help with data science."},
#     {"timestamp": None, "user": "AI", "message": "Sure! What specific topic are you interested in?"}
# ]
#
# After the function execution, the structured data should be in a tabular form where each interaction (timestamp, user, message) is clearly represented and stored.
#
# Example of structured output (in CSV format or SQL database):
# 
# | Timestamp            | User  | Message                                            |
# |----------------------|-------|----------------------------------------------------|
# | 2024-12-13T10:01:00  | John  | Hi there!                                          |
# | 2024-12-13T10:01:30  | AI    | Hello! How can I assist you today?                 |
# | 2024-12-13T10:02:00  | John  | I need help with data science.                     |
# | 2024-12-13T10:02:30  | AI    | Sure! What specific topic are you interested in?   |
# 
# The final goal is to make AI conversation logs more interpretable and structured for analysis.