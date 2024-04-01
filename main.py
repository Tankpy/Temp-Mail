import requests
import random
import string
import time

def generate_random_string(length=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_temp_email():
    username = generate_random_string()
    domain = "1secmail.com"
    email_address = f"{username}@{domain}"
    print(f"Generated temporary email address: {email_address}")
    return username, domain

def check_inbox(username, domain):
    api_url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch emails.")
        return []

def get_email_content(username, domain, mail_id):
    api_url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain}&id={mail_id}"
    response = requests.get(api_url)
    if response.status_code == 200:
        email_content = response.json()
        return email_content
    else:
        print("Failed to fetch email content.")
        return {}

def monitor_email(username, domain, duration_minutes=10, check_interval_seconds=30):
    print("Monitoring email for new messages...")
    seen_emails = set()  # Keep track of seen email IDs
    start_time = time.time()
    end_time = start_time + duration_minutes * 60

    while time.time() < end_time:
        inbox = check_inbox(username, domain)
        if inbox:
            new_emails = [email for email in inbox if email['id'] not in seen_emails]
            if new_emails:
                print(f"Received {len(new_emails)} new email(s):")
                for email in new_emails:
                    email_content = get_email_content(username, domain, email['id'])
                    print(f"From: {email['from']}")
                    print(f"Subject: {email['subject']}")
                    print(f"Content: {email_content.get('textBody', 'No content available.')}")
                    seen_emails.add(email['id'])  # Mark as seen
            else:
                print("No new emails.")
        else:
            print("No emails in the inbox.")

        time.sleep(check_interval_seconds)
        print("Checking again...")

    print("The monitoring period has ended.")

def main():
    while True:
        username, domain = generate_temp_email()
        monitor_email(username, domain)
        choice = input("Do you want to generate another temporary email? (y/n): ").strip().lower()
        if choice != 'y':
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()
