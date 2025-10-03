```markdown
# Python Calculator

A small, command-line Python calculator script for basic arithmetic and a circle-area calculation. This repository contains a single script, `calculator.py`, that runs in the terminal and provides an interactive prompt to perform addition, subtraction, multiplication, division and compute the area of a circle.

## Features

- Interactive command-line menu
- Addition, subtraction, multiplication, division
- Area of a circle calculation (A = π r²)
- Input validation and helpful error messages

## Requirements

- Python 3.7 or newer

This project has no external dependencies — it uses only the Python standard library.

## Install / Get started

1. Clone or download this repository.
2. Open a terminal (PowerShell, CMD, Bash) and change into the project directory:

```powershell
cd path\to\Python-Calaculator
```

3. Run the calculator script:

```powershell
python calculator.py
```

On systems with multiple Python versions you may need to use `python3` instead of `python`.

## Usage

When you run `calculator.py` you'll see a numbered menu. Enter the number of the operation you want (1–6), then follow the prompts:

Menu options:

1. Add
2. Subtract
3. Multiply
4. Divide
5. Area of Circle
6. Exit

Examples:

- To add two numbers, choose `1` then enter the first and second numbers at the prompts.
- To compute a circle area, choose `5` and enter the radius (a number). The script uses a default π value of 3.1415 and prints the computed area.

Notes on input:

- The program validates numeric input and menu choices. If you enter a non-numeric value where a number is expected, the program asks again.
- Division by zero is detected and handled with a friendly message — the operation is not performed.

Advanced usage (importing):

You can also import the `cal` function from `calculator.py` into another script and call it directly with a custom π value:

```python
from calculator import cal
import math

# call with a more precise pi
cal(pi=math.pi)
```

## Development

This is a tiny one-file project. If you want to extend it:

- Add unit tests for the arithmetic and area calculations.
- Extract calculation logic into separate functions to improve testability.
- Replace the interactive prompt with a CLI argument interface (argparse) if you prefer non-interactive use.

## Contributing

Contributions are welcome. Please open an issue for discussion or submit a pull request with a clear description of changes.

## License

This project includes a `LICENSE` file. By default the repository provides licensing information; please review `LICENSE` for details.

## Contact

If you have questions or suggestions, open an issue in this repository.

## Known issues / Notes

- π is a default parameter in the script (`pi=3.1415`). For more accurate results import `math` and call `cal(pi=math.pi)` when using the function programmatically.
- There are no automated tests included yet.

---

Small, self-contained, and easy to read — perfect as a learning example or quick utility.
