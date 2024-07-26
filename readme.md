# 🔐 Strong Password Checker

## Overview

Welcome to the **Strong Password Checker** project! This tool is designed to assess the strength of passwords based on predefined criteria. It uses **PLY (Python Lex-Yacc)** to lex and parse passwords, ensuring they meet the necessary requirements to be considered strong.

## ✨ Features

- **Password Validation**: Checks if a password meets the criteria for strength.
- **Criteria**:
  - At least 13 characters long.
  - Contains at least one uppercase letter.
  - Contains at least one lowercase letter.
  - Contains at least one digit.
  - Contains at least one special character.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- PLY library

You can install PLY using pip, but I provided a `requirements.txt` file:

```sh
pip install ply
```

### Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/Darleanow/LexerParserPasswordPython
   cd LexerParserPasswordPython
   ```

2. **Ensure you have PLY installed**:

   ```sh
   pip install -r requirements.txt
   ```

3. **Run the application**:

   ```sh
   python parser.py
   ```

## 🛠️ Usage

Once the application is running, you will be prompted to enter a password. The tool will then evaluate the password and determine if it is strong based on the predefined criteria.

### Example

```sh
Enter a password to check (enter 'exit' to quit): MyStrongPPPAAAA!!@ssw0rd!
Strong password

Enter a password to check (enter 'exit' to quit): weakpass
Weak password
```

## 📂 Project Structure

- **lexer.py**: Contains the lexer definitions to identify parts of the password.
- **parser.py**: Contains the parser logic that uses the lexer to check password strength.

## 📧 Contact

Made By Enzo, Damien, Mohammed
If you have any questions or suggestions, please feel free to reach out.
