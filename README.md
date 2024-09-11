# Web-brute


Web Brute is a Python script that performs a brute force attack against a web application's login form. It tests multiple username and password combinations to identify valid credentials. The tool allows users to specify a "needle" text to detect a successful login response.

## Features

- Supports both username lists and files
- Custom wordlist input for passwords
- Allows user-defined success indicator text ("needle")
- Efficient multi-threaded HTTP requests using `requests.Session`

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/web-brute-forcer.git
    cd web-brute-forcer
    ```

2. **Install Required Libraries:**

    ```bash
    pip install requests tqdm
    ```

## Usage

```bash
python web_brute.py <target> [--usernames <usernames>] [--usernames_file <usernames_file>] <password_file> --needle <needle>
```
