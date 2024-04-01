# Temporary Email Monitor

A Python script to generate a temporary email address, monitor the inbox for new messages, and display the contents of new emails. This script uses the free temporary email service provided by 1secmail.com.

## Features

- Generates a new temporary email address.
- Monitors the inbox for a specified duration.
- Displays new email messages, including sender, subject, and content.
- Allows for frequency adjustment of inbox checks.
- Option to generate another temporary email after the monitoring period.

## Requirements

- Python 3
- `requests` library

## Installation

1. Ensure Python 3 is installed on your system.
2. Install the `requests` library

Using pip install requests

Download the main.py script from this repository.

## Usage
To run the script, navigate to the directory containing main.py and execute:

python temp_email_monitor.py

Follow the on-screen prompts to start monitoring a new temporary email address or to generate a new one after the monitoring period.

## Customization
You can customize the monitoring duration and the frequency of inbox checks by modifying the following variables at the beginning of the main.py script:

duration_minutes: Duration of the monitoring period in minutes (default is 10 minutes).
check_interval_seconds: Frequency of inbox checks in seconds (default is 30 seconds).
For example, to check the inbox every 15 seconds for 5 minutes, set:

duration_minutes = 5
check_interval_seconds = 15

## Limitations
The script uses the public API provided by 1secmail.com, which does not require authentication. Be mindful of the data you receive/send using this service, as it is accessible publicly.
Frequent requests to the service may be subject to rate limiting. Adjust check_interval_seconds accordingly.

## Disclaimer
This script is for educational purposes only. Do not use it to send or receive sensitive information. Always use responsibly and in accordance with the terms of service of the email provider (1secmail.com).

## Contributions
Contributions are welcome! If you have improvements or bug fixes, please open a pull request or issue.


This `README.md` provides a concise overview of the script and how to use it. Adjust the content as necessary to fit the specifics of your script, especially if you add features or make significant changes.

Thank you!
