# Meeting Deconflictor
Deconflict meetings over a day.

## Prompt:

The Exercise

The supplied "times" data file contains a list of start/end times for
a series of meetings scheduled during one day. Write a program that
reads this file and displays a report of meetings that conflict with one
another. You may use any programming language you prefer. Concentrate
on writing simple, expressive, tested code that shows how you like
to understand the problem, write tests to describe the problem, and
write code to make the tests pass and solve the problem. An hour
or two should be sufficient. During your on-site interview, you'll
walk us through your solution. If time allows, we may propose a small
extension of the requirements that we'll code together in pair-programming
style. Have fun!


## Usage

python -m meeting_deconflictor.deconflict FILENAME

Example:
>python -m meeting_deconflictor.deconflict /Users/kfeldhus/code/meeting_deconflictor/tests/data/times


## Development

### Testing

> pytest
