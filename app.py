# -------------------------------------------------------
# Hi! Terpity here.
# I'm glad you're being skeptical of the program, I would be too. Props to you for being safe and checking it out.
# Man of my word, hand on heart, the only place the API key here goes is the Flinders Canvas servers

# Import statements for required plugins
import sys
import requests
import json

# The text shown when exiting the program
sysExitText = "The program will now terminate. If you're finished using the program, it is advised to go back to your Canvas 'Approved integrations' and delete the Access Key you generated, to prevent unwanted use."

# Tutorial steps
print('\n\n\n-------------------------------------------------')
print("Welcome to Terpity's course nickname utils!")
print("This program allows users to update and remove the nicknames for each of their enrolled Canvas (FLO) courses. The course nickname is only visible to you.")
print("To use this program, there are a few quick steps that need to be completed. All the code for this is self-contained and nothing is saved or leaves the program at all, except the API calls to Canvas.")
print("To proceed, first you need to get an API key from your Canvas settings.")
print("On desktop, the steps should be as follows:")
print("1. On the side panel, open the Account tab and click on the 'Settings' link.")
print("2. Scroll down to the 'Approved integrations' section. Click on the '+ New access token' button")
print("3. Type in 'Changing course nicknames' or something to that effect as the purpose, and select an expiration close to the current date (This is optional, but is best practice)")
print("4. Once the access token details are visible, copy the string of characters from the 'Token' heading. Paste this code into Notepad or a similar text editor.")
try:
    userToken = str(input("5. Paste the API token here and press Enter: "))
except:
    print('An error occured when entering the API token')
    sys.exit(sysExitText)

if userToken == "":
    print('You did not enter an API token')
    sys.exit(sysExitText)

print('\n\n------------------------------------------------------\nThe program also needs to know where to send your API request.')
print('1. You\'re a Flinders\' Uni student')
print('2. You\'re a Uni of Adelaide student')
print('3. You go to another university that uses Canvas')
try:
    userUni = str(input('Please enter the number that applies to you (1, 2, or 3): '))
    if userUni == "1" or "2" or "3":
        match userUni:
            case "1":
                api_url = "https://canvas.flinders.edu.au/api/v1"
            case "2":
                api_url = "https://myuni.adelaide.edu.au/api/v1"
            case "3":
                try:
                    print('\n\n------------------------------------------------------\nAn example of a Canvas link is "https://canvas.flinders.edu.au/"')
                    api_url = str(input("Please paste your Canvas link (INCLUDING the final forward slash): "))
                    api_url = api_url + "api/v1"
                except:
                    print('An error occured')
                    sys.exit(sysExitText)
    else:
        print('The input was invalid. Please try again')
        sys.exit(sysExitText)
except TypeError:
    print('The value entered was not a number')
    sys.exit(sysExitText)
except:
    print('An error occured')
    sys.exit(sysExitText)



# Setting constants

headers = {"Authorization": f"Bearer {userToken}"}
validCourseIDs = []

# Prints utility options
print('\n\n------------------------------------------------------\nAvailable utilities:\n')
print("1. Set a course's nickname")
print("2. Remove one course's nickname")
print('3. Remove ALL course nicknames')
print('Please enter either "1", "2", or "3" (Without the quotation marks) to select your option')

# Prompts utility selection
menuOption = str(input('Enter the number of your choice: '))
# If selection is not vaild, closes the program
if menuOption == "1" or "2":
    # Requests lists of courses from server
    response = requests.get(f"{api_url}/users/self/courses", headers=headers)
    
    # If the status code isn't "OK", closes the program
    if response.status_code != 200:
        print(f'An error has occured: status code from server: {response.status_code}')
        print('Apologies, please try again later.')
        sys.exit(sysExitText)
    # When courses are received:
    else:
        # Prints enrolled courses
        print('\n\n\n')
        print('Your enrolled courses:\n------------------------------------------------------\n')   
        responseData = json.loads(response.text)
        # Lists all enrolled courses
        for k,v in enumerate(responseData):
            print(f"{v['course_code']} --- {v['id']}")
            validCourseIDs.append(v['id'])

    # If the menu option was 1
    match menuOption:
        case "1":
            print('\n')
            print('From the courses listed above, please identify the course you wish to rename.')

            # Takes user input for the course and its new nickname
            inputCourseID = str(input("Type in the digits at the end of the course's line (after the three dashes) and press Enter: "))
            inputNewNickname = str(input("Type in the new nickname you would like to set and press Enter: "))

            # Sends the request to the server
            payload = dict(nickname=inputNewNickname)
            url = f'{api_url}/users/self/course_nicknames/{inputCourseID}'
            response = requests.put(f'{url}',data=payload,headers=headers)

            if response.status_code != 200:
                print(f'\n\n------------------------------------------------------\nAn error has occured: status code from the server: {response.status_code}')
                print('Apologies, please try again later.')
                sys.exit(sysExitText)
            else:
                print(f'\n\n------------------------------------------------------\nCourse with id {inputCourseID} has successfully had its nickname updated to {inputNewNickname}')
                sys.exit(sysExitText)

        case "2":
            print('\n')
            print('From the courses listed above, please identify which one you want to remove the nickname of.')

            inputCourseID = str(input("Type in the digits at the end of the course's line (after the three dashes) and press Enter: "))
            url = f'{api_url}/users/self/course_nicknames/{inputCourseID}'
            response = requests.delete(f'{url}',headers=headers)

            if response.status_code != 200:
                print(f'\n\n------------------------------------------------------\nAn error has occured: status code from the server: {response.status_code}')
                print('Apologies, please try again later.')
                sys.exit(sysExitText)
            else:
                print(f'\n\n------------------------------------------------------\nCourse with id {inputCourseID} has successfully had its nickname cleared.')
                sys.exit(sysExitText)

        case "3": 
            confirmation = input('\n\n------------------------------------------------------\nPlease type "y" or "n" (Without quotations) to confirm if you want to delete ALL your course nicknames: ')
            
            if confirmation == "y":
                url = f'{api_url}/users/self/course_nicknames'
                response = requests.delete(f'{url}',headers=headers)
                
                if response.status_code != 200:
                    print(f'\n\n------------------------------------------------------\nAn error has occured: status code from the server: {response.status_code}')
                    print('Apologies, please try again later.')
                    sys.exit(sysExitText)
                else:
                    print(f'\n\n------------------------------------------------------\nAll course nicknames successfully cleared.')
                    sys.exit(sysExitText)
            
            else:
                sys.exit(sysExitText)

        case _:
            print(f'The entry was invalid')
            print('Please reload the program and try again.')
            sys.exit(sysExitText)
