# Friday-Project-7
This repo hosts an application that allows a user to sign up and sign in using a database to store their information. Please start by running the signupFile.py successfully through to recieve the prompt "Sign Up successful!" Then run the signinFile.py using the same email and password to recieve the prompt "Login In Successful."

## SignUpInfo.db
This file hosts the database which saves a user's email and password once the entries meet all the parameters of the signupFile.py. 

## signupFile.py
This file is used as a sign up application. When ran, a window will pop up prompting the user to enter an email, password, and re-enter password.
The passwords must match and the email must include "@" and "." to ensure there is a domain listed. Otherwise, the application will prompt the
user " Invalid email format. Please enter a valid email" or " Passwords do not match. Please try again." In additon, this window is configured to save successful entries to the SignUpInfo.db when the defined parameters are met. 

This window was created using a mixture of defined functions, link to the database, entry boxes, labels, window title, and a button.

## loginFile.py
This file is used as a sign in application. This file prompts the user to enter their email and password. It then checks the SignUpInfo.db to ensure
the user has signed up. If the user is in the database, it will prompt "Sign In Successful" in the color green. Otherwise, it will prompt "Email or 
Password Incorrect" in the color red. 

This window was created using a link to the database file, defined functions, entry boxes, labels, window title, and a button. 