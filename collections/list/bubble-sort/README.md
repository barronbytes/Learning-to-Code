# Problem Statement

A teacher wants to automate how they organize their student exam scores after grading. They decide to implement a function **top_scores(scores, n)** that accepts a list of unsorted assignment *scores* and an integer *n* as inputs and returns the top *n* scores in descending order. The teacher intends to reward the top performing students.

## Challenge Constraints

The data respresents an unsorted list. You must organize the list in desending order. You must solve this problem without using any built-in sorting functions.

- Each score is between 0 and 100
- Do not create a new list to store values
- Handle edge cases, such as an empty list as input
- Use the **Bubble Sort Algorithm** to solve

## Future Improvements

This project has a small scope. The current solution creates a function **top_scores(scores)** that does not yet implement the variable **n** as desired. With this in mind, the current solution returns a list of descending scores. To fully solve this problem the function should be updated:

- The function should be escaped if an empty list is provided as input
- The function should handle user errors, such as providing an *n* value greater than the *scores* list length
- The function should determine a way to randomize the value of *n* and values for *scores*

The problem scope is small. Additional features/complexities could be added in the future:

- Front-end: implement web application
- Back-end: login authentication/authorization, data validation
- Data: store data into a database, use visualization tools, provide further details (e.g. student names, class block)
- Client: ask teacher what rewards they would like to give to students (e.g. 1st place, 2nd place, 3rd place, etc.)
