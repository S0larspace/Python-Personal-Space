'''
Aim of this script is to filter spam and potential phishes from an email inbox, plans to be automated eventually.
'''
import os

# Good practice to establish absolute or dynamic paths
# Get directory of script
# __file__ refers to this script itself
script_dir = os.path.dirname(os.path.abspath(__file__))

# Directory of the sample email source text file
sampEmail_dir = os.path.join(script_dir, "sample_email_source.txt")

email_info = {
    "from": None,
    "subject": None,
    "date": None
}

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
    "won't last forever"
}  # Consider moving this into a separate text file to avoid lengthy code as this list grows

with open(sampEmail_dir, encoding="utf-8", errors="ignore") as f:
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

# Output to terminal to test parsing logic
print("Email details as follows:\nDate: {}\nFrom: {}\nSubject: {}".format(
    email_info["date"], email_info["from"], email_info["subject"]))
