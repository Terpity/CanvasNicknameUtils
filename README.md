# Canvas Nickname Utils - by Terpity

## Hey!
Hey! I'm [Terpity](https://github.com/Terpity), and this is my Python CLI utility for changing Canvas course nicknames.  

I developed this after I couldn't find a setting for it in the Canvas UI. Maybe I was just blind, or stupid, or both, but here we are.  

It's pretty basic, and covers all of the available features for interacting with nicknames through the API.

## Requirements
### Python packages
The utility requires the [requests](https://pypi.org/project/requests/) package to be installed. If you're using PIP, open a terminal in the same folder as app.py (or navigate there) and simply run  

    pip install -r requirements.txt

and the required package should be installed.
The program also requires { sys } and { json } but these should be installed by default.

### API key
The utility does require you to input an API key from your Canvas settings.
On desktop, the steps for me were as follows:
1. On the side panel, open the Account tab and click on the 'Settings' link.
2. Scroll down to the 'Approved integrations' section. Click on the '+ New access token' button
3. Type in 'Changing course nicknames' or something to that effect as the purpose, and select an expiration close to the current date (This is optional, but is best practice)
4. Once the access token details are visible, copy the string of characters from the 'Token' heading. Paste this code into Notepad or a similar text editor.

The program will then ask you for this token as an input.
The program <b>does not save this</b> across uses, so if you plan on changing multiple nicknames, keep the API key saved somewhere else to refer back to.


### Canvas Link
You will also need the link to your institutions Canvas page.  
As an example, the one for Flinders University is "https://canvas.flinders.edu.au/" (As of mid-2024).  

If you go to Flinders or Adelaide Uni, the links are already preloaded by default, simply choose your applicable option.  

If you go to another institution, please copy the link to Canvas and paste it when the program asks you to.  
Make sure to INCLUDE the forward slash at the end, or else the program will not be able to fulfill the request properly.

## Disclaimer
The program <b>does not</b> save any information.   
The program <b>does not</b> send any information outside of <b>your network and Canvas</b>.  
<b>I do not collect any information</b> when you run the program.

Feel free to verify this yourself, the code is openly available on my Github at https://github.com/Terpity/CanvasNicknameUtils
