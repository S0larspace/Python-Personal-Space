'''
Aim of this script is to filter spam and potential phishes from an email inbox, plans to be automated eventually.
'''
import os

email_info = {
    "from": None,
    "subject": None,
    "date": None
}
with open("Python Refresher\Python Projects\Email Inbox Filter\sample_email_source.txt", encoding="utf-8", errors="ignore") as f:
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

print("CWD: ", os.getcwd())
print("Files in CWD: ", os.listdir())
# print("Email details as follows:\nDate: {}\nFrom: {}\nSubject: {}".format(
#   email_info["date"], email_info["from"], email_info["subject"]))
