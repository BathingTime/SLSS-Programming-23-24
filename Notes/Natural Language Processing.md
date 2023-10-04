---
tags:
  - notes
  - nlp
  - y2023
  - programming-level-1-2
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
## Naming

What you can do:
1. Name them with letters, numbers, and underscores.
2. Names **should** start with a lowercase letter.
What you **cannot** do:
1. You **cannot** name them with spaces or symbols.
2. You **cannot** name them with certain names that are reserved.
	• e.g. `if`, `elif`, `else`, `and`, `or`, `not`

Good names are something like this:

```python
fave_food
date_of_birth
student_number
```

Bad names are like this:

```python
Favourite_food
a
num
aa
aaa
```
# Design

The design process is the steps that we take when we create a solution to a problem.

There are four steps in our design process:
## 1. Design our algorithm in English (or any human language).
An *algorithm* is a sequence of steps to solve a problem.
In this class, before we start ANY programming, we write our steps in English.
## 2. Translate our algorithm from English to Python.
We will translate our algorithm into "proper" Python.
## 3. Test our Python algorithm.
Check if it works *syntactically*. In other words, we check to see if it BREAKS.
Check if it works *semantically*.