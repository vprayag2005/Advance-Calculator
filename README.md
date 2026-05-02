# Advance Calculator (Python)

An interactive, menu-driven **advanced calculator** built in Python that goes beyond basic arithmetic and includes common math + finance utilities (roots, factorial, powers, logarithms, sine, simple/compound interest). The project is designed to be **easy to run, easy to extend, and backed by automated tests**.

**Repository:** https://github.com/vprayag2005/Advance-Calculator

---

## Why this project (recruiter-friendly highlights)

- **Clean, modular design:** core logic is encapsulated in a `Calculator` class.
- **Algorithmic implementations (not just `math` wrappers):**
  - Square root via **Heron’s method**
  - N-th root via **Newton–Raphson**
  - Sine via **Maclaurin series** approximation
  - Log base `a` of `b` using repeated scaling/division (digit approximation)
- **Interactive CLI application:** simple menu system for user-driven execution.
- **Stateful workflow:** supports continuing calculations using the **previous result**.
- **Tested with PyTest-style tests:** includes a `test_calculator.py` suite covering major operations.

---

## Features

### Basic operations
- Addition
- Subtraction
- Multiplication
- Division (handles divide-by-zero gracefully)

### Advanced math operations
- **Square root** (Heron’s method)
- **Factorial**
- **Power** (supports negative exponents)
- **N-th root** (Newton–Raphson)
- **Log base a of b** (approximation)
- **Sine (degrees)** (Maclaurin series)

### Finance utilities
- **Simple Interest**
- **Compound Interest**

---

## Tech stack

- **Language:** Python 3
- **Type:** Command-line (CLI) program
- **Testing:** `pytest`-style unit tests (`test_calculator.py`)

---

## Project structure

- `calculator.py` — main implementation (`Calculator` class + CLI loop)
- `test_calculator.py` — unit tests
- `README.md` — project documentation

---

## Getting started

### Prerequisites
- Python 3.x installed

### Run the calculator

```bash
python calculator.py
```

You will see a menu like:

- 1 Addition
- 2 Subtraction
- 3 Multiplication
- 4 Division
- 5 Square Root
- ...
- 13 Exit

---

## Running tests

If you have `pytest` installed:

```bash
pytest
```

(Alternatively, you can run the test file directly, but `pytest` is recommended.)

---

## Example usage

- Compute `sqrt(49)` → `7`
- Compute compound interest with `(principal=3000, rate=0.1, time=2, periods=2)`
- Compute `sin(90°)` → approximately `1.0`

---

## Notes & limitations

- This is a **learning-focused** project emphasizing algorithmic implementation and CLI flow.
- Some functions return approximations based on configured iteration/precision.

---

## Next improvements (good to mention in interviews)

- Add input validation for all numeric inputs (handle non-numeric user input gracefully)
- Improve exponent handling in `find_power` for non-integer exponents
- Expand trigonometric functions (cos, tan) and add radians support
- Add CI workflow (GitHub Actions) to run tests on every push
- Package as an installable CLI (`pipx` / `argparse` command interface)

---

## License

Add a license if you plan to share/redistribute this project.
