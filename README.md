### python-package
### Hexlet tests and linter status:
[![Actions Status](https://github.com/SashaPodorozhnyak/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/SashaPodorozhnyak/devops-engineer-from-scratch-project-49/actions)[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=SashaPodorozhnyak_devops-engineer-from-scratch-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=SashaPodorozhnyak_devops-engineer-from-scratch-project-49)[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=SashaPodorozhnyak_devops-engineer-from-scratch-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=SashaPodorozhnyak_devops-engineer-from-scratch-project-49)[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=SashaPodorozhnyak_devops-engineer-from-scratch-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=SashaPodorozhnyak_devops-engineer-from-scratch-project-49)[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=SashaPodorozhnyak_devops-engineer-from-scratch-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=SashaPodorozhnyak_devops-engineer-from-scratch-project-49)[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=SashaPodorozhnyak_devops-engineer-from-scratch-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=SashaPodorozhnyak_devops-engineer-from-scratch-project-49)[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=SashaPodorozhnyak_devops-engineer-from-scratch-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=SashaPodorozhnyak_devops-engineer-from-scratch-project-49)[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=SashaPodorozhnyak_devops-engineer-from-scratch-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=SashaPodorozhnyak_devops-engineer-from-scratch-project-49)[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=SashaPodorozhnyak_devops-engineer-from-scratch-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=SashaPodorozhnyak_devops-engineer-from-scratch-project-49)[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=SashaPodorozhnyak_devops-engineer-from-scratch-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=SashaPodorozhnyak_devops-engineer-from-scratch-project-49)[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=SashaPodorozhnyak_devops-engineer-from-scratch-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=SashaPodorozhnyak_devops-engineer-from-scratch-project-49)

# Brain Games 🧠🎮

A collection of five console-based math games to train your brain. Each game offers a series of three questions that require correct answers.

## 🎯 Project Description

**Brain Games** is a collection of simple yet engaging math games launched from the command line. All games follow a unified format: greeting, three questions with increasing difficulty, and a final result.

### Core Principles:
- **Input**: via standard input (`stdin`)
- **Output**: via standard output (`stdout`)
- **Interface**: fully console-based, interactive
- **Logic**: each game has its own unique rules and mathematical challenges

## 🎮 Available Games

### 1. **Brain Even** (`brain-even`)
Determine if a number is even.

**Rules:**
- The program shows a random number
- The player must answer `yes` if the number is even, or `no` if it's odd
- Example: number 15 → answer `no`

### 2. **Brain Calc** (`brain-calc`)
Solve a mathematical expression.

**Rules:**
- The program shows a random arithmetic expression
- Supported operations: addition (`+`), subtraction (`-`), multiplication (`*`)
- The player must calculate and enter the correct result
- Example: `5 + 3` → answer `8`

### 3. **Brain GCD** (`brain-gcd`)
Find the greatest common divisor of two numbers.

**Rules:**
- The program shows two random numbers
- The player must find and enter their greatest common divisor (GCD)
- Example: numbers 25 and 50 → answer `25`

### 4. **Brain Progression** (`brain-progression`)
Find the missing number in an arithmetic progression.

**Rules:**
- The program shows an arithmetic progression with one missing number
- The player must determine and enter the missing number
- Example: `5 7 9 .. 13 15` → answer `11`

### 5. **Brain Prime** (`brain-prime`)
Determine if a number is prime.

**Rules:**
- The program shows a random number
- The player must answer `yes` if the number is prime, or `no` if it's composite
- Example: number 7 → answer `yes`


### Links

This project was built using these tools:

| Tool  |  Description                                          
|-------|---------------------------------------------------------|

| [uv](https://docs.astral.sh/uv/)            | "An extremely fast Python package and project manager, written in Rust" |

| [ruff](https://docs.astral.sh/ruff/)        | "An extremely fast Python linter and code formatter, written in Rust" |

### setup

```bash
#Clone the repository
git clone https://github.com/SashaPodorozhnyak/devops-engineer-from-scratch-project-49.git

# setup package
cd brain-games
make install

# start gaming
make brain-game
```


### examples
Examples of games can be viewed at the links below.
But you can run the asciinems yourself in the terminal, which are located in the demo directory:

brain-even
https://asciinema.org/a/YeIdAD58T1XxuMGQJs875JyCg

brain-calc
https://asciinema.org/a/FWChTJOR0UMZ9wJTTyv33elEm

brain-gcd
https://asciinema.org/a/zMAPQyLrn9TphXqHWc39uSyXM

brain-progression
https://asciinema.org/a/sNNJr3uoJJfVpGK0pYVxqi0z3

brain-prime
https://asciinema.org/a/ddP4mKravtdScsryBrlmJ3jKA

OR in terminal
```bash
#example brain-even
bash
$ brain-even
Welcome to the Brain Games!
May I have your name? Alice
Hello, Alice!
Answer "yes" if the number is even, otherwise answer "no".
Question: 15
Your answer: no
Correct!
Question: 24
Your answer: yes
Correct!
Question: 9
Your answer: no
Correct!
Congratulations, Alice!
```
This repository was created as part of a project for learning on the Hexlet platform.
