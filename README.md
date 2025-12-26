# 🔐 Password Generator & Strength Analyzer

This project is a Python-based tool designed to generate cryptographically secure passwords and analyze their strength using industry-standard algorithms.

It was developed to practice **modularization**, **external API integration**, and **secure coding practices** in Python, following the learning path of "Curso em Vídeo".

## 🚀 Features

* **Secure Generation:** Uses the `secrets` module for cryptographically strong random numbers, making it suitable for managing secrets such as passwords and account authentication.
* **Advanced Analysis:** Implements the `zxcvbn` library (developed by Dropbox) to estimate password strength based on entropy and common patterns.
* **Visual Feedback:** Provides a clear safety level from 0 (Too Weak) to 4 (Super Strong) with color-coded terminal output.
* **Smart Tips:** Offers specific suggestions on how to improve the provided or generated password.
* **Robust Error Handling:** Includes `try/except` blocks to manage invalid user inputs and ensure a smooth experience.

## 🛠️ Technologies Used

* **Python 3**
* **`zxcvbn` Library:** For realistic password strength estimation.
* **`secrets` Module:** For generating tokens and secure passwords.
* **`string` Module:** To handle ASCII characters, digits, and punctuation.

## 📦 Installation

1. **Clone the repository:**
```bash
git https://github.com/Florianomiguel/secure-password-generator

```


2. **Navigate to the project folder:**
```bash
cd password-generator

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```



## 🎮 How to Use

Run the main script to start the interactive CLI:

```bash
python main.py

```

You will be prompted to either:

1. **Generate a new password:** Specify the desired length and get a secure string immediately.
2. **Check a current password:** Type any password to see its safety level and improvement tips.

## 🛤️ Future Roadmap

* [ ] Build a web interface using **Streamlit** to make the tool accessible via browser.
* [ ] Add an option to export generated passwords to a local encrypted file.
* [ ] Implement a graphical "Strength Meter" bar.

---
