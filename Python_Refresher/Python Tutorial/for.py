students = {
    "male": ["Tom", "Anton", "Peter", "Harry"],
    "female": ["Veronica", "Chrystal", "Anabel", "Leah"]
}

for key in students.keys():  # gives back the keys "male" and "female"
    for name in students[key]:  # goes through each name in the students dictionary
        if "a" in name:
            print(name)
