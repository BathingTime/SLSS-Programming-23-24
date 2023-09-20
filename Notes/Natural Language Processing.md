---
tags:
  - notes
  - nlp
  - y2023
  - programming-1-2
---
# Output

We can use a function to display text and symbols onto the screen.
We use the `print()` function to display outputs.

```python
print('Your text goes in here.')
```

> **Task:**
> 1. Open Visual Studio Code.
> 2. Make sure that it's open to your repository.
> 3. Create a new file called `Input_and_Output.py`.
## [[Headers]]

# Comments

Comments are pieces of text that are *not* interpreted by Python.
This means that the text is **ignored**.
We use the hash symbol (#) to make comments.

```python
#This is a comment.
```

> **Task:**
> • In `Input_and_Output.py`:
> 	1. Put the header.
> 	2. Write in some comments.
# Input

We cam grab information from the user using `input()`.
When we run the function, it does two things:
1. It **waits** for the user to write something or noting.
2. The user needs press **Enter/Return** to indicate that they are finished.

```python
input()

input(<prompt>)#Prints out the prompt, then waits.
```
# Variables

Variables allow us to store information for the time that our app is running.

```python
favourite_food=input("What is your favourite food: ")
```

`favourite_food` —> name of the variable
`=` —> assignment operator
`input()` —> value
## [[Strings]]