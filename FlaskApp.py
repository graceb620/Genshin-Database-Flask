"""
FlaskApp.py
@author Grace Bero

Desc: This is the page that runs the website
Just click Run and the ip will be up and running

IP: ip
"""

from flask import Flask
from flask import render_template
from flask import request
from DynamoCode import *
from SQLcode import *
import creds
import boto3

app = Flask(__name__)

'''
/home

The home page
'''
@app.route('/') #the desired address
def home(): #creates the home page
    return render_template('home.html') #renders using the desired html template

    
'''
/database

Allows users to READ a table of character info and reccomended builds
'''
@app.route('/database') #desired address
def allChar(): #displays the SQL database 
    rows = execute_query("""SELECT CName, Region, Weapon, Artifact, ReleaseVersion
                            FROM Characters JOIN Build USING (CName)
                            ORDER BY ReleaseVersion
                            """) #Runs the desired SQL query
    database_table_html = display_db(rows) #Puts the output into a table format
    return render_template('database.html', database_table_html=database_table_html) #renders using the html template

''' 
/locker

Allows user to READ through a list of their weapons and characters
''' 
@app.route('/locker', methods=['GET']) #The page before the user submits any input
def locker(): #creates the page
    return render_template('locker.html') ##renders using the html template
 
@app.route('/locker', methods=['POST']) #The page after the user submits the input
def lockerPost(): #creates the page
    UserWeapons = "" #empty string holder for weapons
    UserCharacters = "" #empty string holder for characters
    
    username = request.form['username'].lower() #gets the username from the input form and converts to lowercase
    UserWeapons, UserCharacters = get_user_data(username) #gets the weapons and characters lists
    
    #Renders the page using the html 
    return render_template('locker.html', UserWeapons=UserWeapons, UserCharacters=UserCharacters) #adds list to the corresponding id area on html 

'''
/locker/manage

Allows users to CREATE/DELETE a weapon or character from their Locker
'''
@app.route('/locker/manage', methods=['GET']) #before user input
def manageLocker(): #creates the page
    return render_template('manageLocker.html') #Renders using the html

@app.route('/locker/manage', methods=['POST']) #after user input
def manageLockerPost(): #creates the page
    
    username = request.form['username'].lower() #gets username from the form and converts to lowercase
    
    if 'AddCharacter' in request.form: #Add a character
        category = "Characters" #category name
        item = request.form['AddCharacter'].lower() #gets character from the form and converts to lowercase
        AddCharMsg = add_item(username, category, item) #adds the character to the users character list and outputs the outcome message
        #Renders page using html 
        return render_template('manageLocker.html', AddCharMsg=AddCharMsg) #puts outcome message in the corresponding id on html
        
    elif 'DeleteCharacter' in request.form: #Delete a character
        category = "Characters" #category name
        item = request.form['DeleteCharacter'].lower() #gets item from the form and converts to lowercase
        DelCharMsg = delete_item(username, category, item) #deletes character and outputs the outcome message
        #renders the page unsing html
        return render_template('manageLocker.html', DelCharMsg=DelCharMsg) #puts outcome message in the corresponding id in html
        
    elif 'AddWeapon' in request.form: #Add a weapon
        category = "Weapons" #Category name
        item = request.form['AddWeapon'].lower() #gets item from the form and converts to lowercase
        AddWeaponMsg = add_item(username, category, item) #Adds the weapon and outputs the outcome message
        #renders the page using the html
        return render_template('manageLocker.html', AddWeaponMsg=AddWeaponMsg) #puts the outcome message in the corresponding id in the html
        
    elif 'DeleteWeapon' in request.form: #Delete a message
        category = "Weapons" #Category name
        item = request.form['DeleteWeapon'].lower() #Gets item from the form and converts to lowercase
        DelWeaponMsg = delete_item(username, category, item) #Deletes the weapon and outputs the outcome message
        #Renders page using html
        return render_template('manageLocker.html', DelWeaponMsg=DelWeaponMsg) #puts the outcome message in the corresponding id in the html

'''
/users

Allows users to READ through the list of usernames
'''
@app.route('/users') #compiles a list of all the users in the db
def users(): #creates page
    userList = get_users() #gets a list of the users
    #Renders using the html
    return render_template('users.html', userList=userList) #puts list in the corresponding id in the html

'''
/users/manage

Allows users to CREATE/DELETE a user 
'''
@app.route('/users/manage', methods=['GET']) #before user input
def manageUser(): #creates page
    return render_template('manageUser.html') #renders using the html 

@app.route('/users/manage', methods=['POST']) #after the user input
def manageUserPost(): #creates page
    if 'AddUser' in request.form: #Add a user
        username = request.form['AddUser'].lower() #gets username from the form and converts to lowercase
        addUserMsg = create_user(username, [], []) #creates the user in the db and outputs the outcome message. Users get empty list for Characters and Weapons upon creation
        #renders using html
        return render_template('manageUser.html', addUserMsg=addUserMsg) #Outputs message in the corresponding id on html
    elif 'DelUser' in request.form: #delets a user
        username = request.form['DelUser'].lower() #gets username from the form and converts to lowercase
        DelUserMsg = delete_user(username) #deletes the user and outputs the outcome message. 
        #renders using the html
        return render_template('manageUser.html', DelUserMsg=DelUserMsg) #outputs message in the corresponding id on the html
    
'''
/about

Creates the about page
'''
@app.route('/about') #about me page
def about(): #creates page
    return render_template('about.html') #renders using the html
    
'''
Need this for it to work
'''
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=8080, debug=True)