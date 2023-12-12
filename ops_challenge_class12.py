#!/usr/bin/python3

# Import library 
import requests

# Declare variables by asking user for website address
web_address = input("Please type in destination url (format: google.com):\n")

# Concat w/ user input
user_url = str("https://" + web_address)

# Ask user to select the HTTP method to run
choice = input("Please select an HTTP method from the following list:\n1)get\n2)post\n3)put\n4)delete\n5)head\n6)path\n7)options\n")

# Confirm that they want to send request
confirm_choice = input(f"Please confirm that you want to send a HTTP request to {user_url} by typing 'yes' or 'no': ")

# Confirmation logic
if confirm_choice != "yes":
    print("Cancelling request")
    exit()

# Logic to run things depending on user's selection
if choice == '1':
    method = requests.get
elif choice == '2':
    method = requests.post
elif choice == '3':
    method = requests.put
elif choice == '4':
    method = requests.delete
elif choice == '5':
    method == reuqests.head
elif choice == '6':
    method = requests.patch
elif choice == '7':
    method = requests.options
else:
    print("Please select a method from the list")
response = method(user_url)

# Get status codes
status_codes = {
    200: "Ok",
    201: "Created",
    202: "Accepted",
    203: "Non-Authoritative Information",
    204: "No Content",
    205: "Reset Content",
    206: "Partial Content",
    207: "Multi-Status",
    208: "Already Reported",
    226: "IM Used",
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Found",
    303: "See Other",
    304: "Not Modified",
    307: "Temporary Redirect",
    308: "Permanent Redirect",
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Timeout",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    505: "HTTP Version Not Supported",
    506: "Variant Also Negotiates",
    507: "Insufficient Storage",
    508: "Loop Detected"
}

# Print status code and message
code_message = status_codes.get(response.status_code, "Please try again later")
print(f"Response Status Code w/ Message: {response.status_code} {code_message}")

# Print header info
for header, data in response.headers.items():
    print(f"{header}: {data}")