"""Goal of this program is to obtain an email address input and to slice it into the username and domain name respectively."""

# Get user email address
email = input("What is your email address?: ").strip()

# Slice out the user name
user_name = email[:email.index("@")]
# print(user_name)

# Slice out the domain name
domain_name = email[(email.index("@") + 1):]
# print(domain_name)

# Format message
output = "Your username is {} and your domain name is {}".format(
    user_name, domain_name)


# Display output message
print(output)
