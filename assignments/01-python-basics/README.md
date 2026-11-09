# Python Beginner Assessment — Classwork

Five beginner Python exercises covering input, variables, conditionals,
operators, lists, loops, and strings. Suggested duration: 30–40 minutes.

## Submission and input/output rules

- Put one Python file per answer in `submissions/`.
- The part of the filename before the first underscore is the question ID:
  `q1_calculator.py` maps to `q1`, and `q2.py` maps to `q2`.
- Read the specified input from standard input. Do not print input prompts;
  print only the requested answer so automatic output comparison works.
- For Q4, read five integers from one line separated by spaces.
- Each changed file is evaluated separately against that question's tests.
  GitHub Actions uploads individual JSON reports and a summary for the
  questions submitted in that push.

## Q1. Basic Calculator

Read two numbers on separate lines, followed by an operator (`+`, `-`, `*`, or
`/`) on the third line. Print the result. Convert the inputs to numbers, print
`Cannot divide by zero` for division by zero, and print `Invalid operator` for
an unsupported operator.

Example input:

```text
10
5
*
```

Expected output: `50.0`

Topics: variables, user input, type casting, operators.

## Q2. Even or Odd

Read one integer and print `Even` or `Odd`.

Example input: `17`

Expected output: `Odd`

Bonus: Also determine whether the number is positive, negative, or zero. The
bonus is not included in automatic scoring.

Topics: conditionals, operators.

## Q3. Reverse a String

Read one line of text and print it in reverse. Do not use Python's built-in
`reversed()` function.

Example input: `python`

Expected output: `nohtyp`

Bonus: Check whether the input is a palindrome. The bonus is not included in
automatic scoring.

Topics: strings, loops.

## Q4. Find the Largest Number

Read five integers separated by spaces, store them in a list, and print the
largest value. Do not use `max()`.

Example input: `10 25 4 80 12`

Expected output: `80`

Topics: lists, loops, conditionals.

## Q5. Count Vowels

Read a sentence and print the number of vowels (`a`, `e`, `i`, `o`, `u`).
Count uppercase and lowercase vowels equally.

Example input: `Hello World`

Expected output: `3`

Topics: strings, loops, conditionals.

## Mentor assessment notes

- Ask the candidate to explain their approach before coding.
- Observe whether they can debug simple errors.
- Ask about edge cases after they have a working solution.
- Assess correctness, Python fundamentals, readability, and problem-solving,
  not speed alone.

## Mentor note

The repository includes example submissions to exercise the evaluator. Q1
currently fails the division-by-zero and invalid-operator cases; Q2 and Q4
contain deliberate logic errors. Q3 and Q5 are intended to pass their
configured tests. Fix or replace the seeded examples before using this
directory as a clean student answer key.
