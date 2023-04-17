# Knights

This project contains a Python implementation of a puzzle solver using propositional logic. The puzzle.py file contains the implementation, and it currently includes solutions for four different puzzles.

The puzzles were solved using the logic.py module, which contains a set of classes and functions that implement a propositional logic knowledge base and model-checking algorithms. These algorithms allow the program to determine whether a given set of symbols satisfies a particular knowledge base.

## Usage
To run the program, you can simply execute the puzzle.py file in your terminal or IDE. The output will show the solutions for the four puzzles that have already been implemented.

If you want to add your own puzzle, you can modify the puzzle.py file by adding a new knowledgeN variable containing your knowledge base, where N is a unique integer. Then, add a new tuple to the puzzles list, containing a string with the name of your puzzle and the corresponding knowledgeN variable. Finally, run the program again to see the solutions for your new puzzle.

## Clarifications
Please note that the puzzle.py file was given 4 different knowledge bases that were solved using propositional logic. However, if you would like to add your own puzzle, feel free to modify the file as described above.

The project files are available on GitHub, so there is no need to provide installation instructions or a link to download the project. Simply clone or download the repository to your local machine and run the puzzle.py file as described above.

Also note that the puzzle.py file contains the implementation for the four puzzles, as well as a main function that outputs the solutions for each puzzle. If you would like to use the solver in a different context, you may need to modify the code accordingly.

## Acknowledgments
This project was adapted from a puzzle book by logician Raymond Smullyan. The logic.py module was provided by Harvard's CS50 AI course whereas all puzzles in puzzle.py were solved by myself.
