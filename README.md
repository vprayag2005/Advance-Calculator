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

