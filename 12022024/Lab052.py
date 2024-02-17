#using switch case to take browser from user

browser = input("Enter browser name \n")

match browser:
    case "chrome":
        print("Chrome is selected")
    case "firefox":
        print("firefox is seleted")
    case _:
        print("No Browser selected")