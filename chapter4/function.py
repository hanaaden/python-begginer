Defining a function in Python involves two main steps: defining the function and specifying the arguments it takes.

To define a function, you use the def keyword followed by the name of the function and parentheses (). If the function takes any arguments, they are included within the parentheses. The code block for the function is then indented after the colon.

To call a function in Python, you simply type the name of the function followed by parentheses (). If the function takes any arguments, they are included within the parentheses.


Let's say you want to write a function that takes in a list of integers and returns a new list with all the even numbers in the original list. Here's how you could define and call this function:
```python

def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print(even_numbers)

```

In this example, we define a function called get_even_numbers that takes one argument called numbers. The function then creates an empty list called even_numbers and loops through each number in the numbers list.

If the number is even, it is added to the even_numbers list using the append method. Finally, the function returns the even_numbers list.

To call this function, we first create a list of numbers called numbers with the values [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. We then call the get_even_numbers function with the numbers list as an argument and assign the returned value to a new list called even_numbers.

Finally, we print out the even_numbers list to the console.

When you run this code, it will output the following to the console:

[2, 4, 6, 8, 10]