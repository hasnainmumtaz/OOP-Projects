# OOP Projects

## Football.ipynb
OOP makes code-writing more efficient, making it easier to scale the number of teams playing the League. Improvements that can be made:
- `teams` can be set as a class variable, and once the team is created, it can be appended to the list.
- Creating a leaderboard
- Adding more commentary lines can be achieved by defining a commentary class with class methods to get commentary for different events in the duration of the match.

## Hunting.ipynb
the class can be used here to introduce a multitude of character classes such as knights, to add more depth to a game/simulation with their distinctive mechanics and interactions. Improvements that can be made:
- Remove `status_shield` and `weapon` variables and put them under the `__init__` Dunder method so that they are unique to every Hunter object.
- Consider the damage that can be done by the other classes to each other.

## ooptictactoe.py
The highlight of this code is the use of `Box` class in `populate_grid()` to create the grid. Implementing the Tic Tac Toe GUI in this way reduced the number of lines required to achieve the same effect. Also, I got to learn how to use `customtkinter,` a library built on top of the `tkinter` library. Improvements:
- Add more comments to make it easier to collaborate
- Improve the implementation of `restart()`
