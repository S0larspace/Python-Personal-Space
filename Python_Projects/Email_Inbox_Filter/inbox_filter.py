'''
Aim of this script is to filter spam from an email inbox, plans to be automated eventually.

Currently only implementing text parsing to filter
'''
import os
from email.header import decode_header

# Good practice to establish absolute or dynamic paths
# Get directory of script
# __file__ refers to this script itself
script_dir = os.path.dirname(os.path.abspath(__file__))

# Directory of the sample email folder
EMAIL_DIR = os.path.join(script_dir, "emails")

# Set default values to unknown if any of the headers are missing from the txt file
# Missing headers will generate None values which would create an error if not handled.

spam_phrases = {
    "free gift",
    "don't miss",
    "limited time offer",
    "great deal",
    "insane discounts",
    "instantly",
    "keep your little ones engaged",
    "free membership",
    "100%% guaranteed",
    "100%% satisfaction",
    "Time is running out",
    "won't last forever",
    "newsletter",
    "free"
}  # Consider moving this into a separate text file to avoid lengthy code as this list grows


# Function to decode MIME encoded headers
def decode_mime_header(value):
    if not value:
        return value

    # returns a list of tuples of the header split into different parts and the encoding of each part
    decoded_parts = decode_header(value)
    decoded_string = ""

    for part, encoding in decoded_parts:
        if isinstance(part, bytes):  # Case 1: the part is in bytes and have to be decoded
            decoded_string += part.decode(encoding or 'utf-8', errors='ignore')
        else:   # Case 2: the part is already a string
            decoded_string += part

    return decoded_string


# Main processing loop to go through each email file in the directory
for filename in os.listdir(EMAIL_DIR):

    email_info = {
        "from": "Unknown sender",
        "subject": "No subject",
        "date": "Unknown date"
    }

    if not filename.endswith(".txt"):
        continue  # Skip non-txt files

    file_path = os.path.join(EMAIL_DIR, filename)

    with open(file_path, encoding="utf-8", errors="ignore") as f:
        # C:\Users\Admin\Documents\Career\GitHub Repositories\Python-Personal-Space\Python Projects\Email Inbox Filter\sample_email_source.txt

        for line in f:
            # Remove any trailing and leading whitespaces for each line
            line = line.strip()

            # Email Sources are split into headers and body sections separated by a blank line as the boundary
            if line == "":
                break  # Ends loop if parsing has passed the header section

            if line.startswith("From:"):
                email_info["from"] = line[len("From:"):].strip()
                # len("From:") returns 5 which is also the index of the start of the interested data
            elif line.startswith("Subject:"):
                email_info["subject"] = line[len("Subject:"):].strip()
            elif line.startswith("Date:"):
                email_info["date"] = line[len("Date:"):].strip()

            # Combine info from sender and subject into a single string for spam phrase checking
            text_to_check = (
                (email_info["subject"] or "") + " " + (email_info["from"]) or "").lower()

            # function to detect spam
            is_spam = any(phrase in text_to_check for phrase in spam_phrases)

            result = "SPAM" if is_spam else "CLEAN"

        # Output result of each email to console
        print("-" * 40)
        print("File: {}".format(filename))
        print("From: {}".format(email_info["from"]))
        print("Subject: {}".format(email_info["subject"]))
        print("Date: {}".format(email_info["date"]))
        print("Result: {}".format(result))
