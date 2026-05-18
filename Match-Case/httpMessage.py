# Program to display HTTP status messages using match-case

status_code = int(input("Enter HTTP status code: "))

match status_code:

    case 200:
        print("200 OK - Request Successful")

    case 404:
        print("404 Not Found - Page does not exist")

    case 500:
        print("500 Internal Server Error")

    case _:
        print("Unknown HTTP Status Code")