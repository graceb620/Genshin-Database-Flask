"""
DynamoCode.py
@author Grace Bero

Desc: This is the page that includes all functions related to the DynamoDB
"""
import boto3
from boto3.dynamodb.conditions import Key

TABLE_NAME = "Genshin-Users"

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)


'''
printList(list)

@param list, a list that will be converted into the desired format
@return html, a string that will be used on an html page

Used to format a list into the desired format
'''
def printList(list): 
    html = "" #empty string holder
    for item in list: #loops through list
        html += item + "<br>" #adds every item in desired format
    return html #retuns the desired formatted string list 

'''
get_users()

@return ListUsers, a string of Usernames to be used on an html page

Used to READ and display a list of usernames from the database
'''
def get_users():
    ListUsers = "" #empty string holder
    response = table.scan() #gets all items in the database
    for user in response["Items"]: #runs through all the items in the database 
        ListUsers += user["Username"] + "<br>" #adds every item in the list in desired format
    return ListUsers #returns the usernames in desired format

'''
get_user_data(username)

@param username, a string associated with a users Username
@return weapons, a list of a users weapons or blank if there is an error
@return characters, a list of a users characters or an error message

Used to get a list of a users weapons and characters from the database
'''

def get_user_data(username):
    
    try: #all expeced outcomes
        response = table.get_item(Key={'Username': username}) #gets all the usernames in database
        if 'Item' in response: #checks to ensure the username exists in the db
            user = response.get('Item') #Gets the specific User info requested
            
            weaponList = user["Weapons"] #gets the weapon list from the desired user
            weapons = printList(weaponList) #weapon list in the desired format
        
            charList = user["Characters"] #gets the character list from the desired user
            characters = printList(charList) #character list in desired format
        else: #if username not in db
            #used this format due to how the output is displayed on the html
            characters = "User may not exist, please try again"
            weapons = ""
            
        return weapons, characters #returns the lists
        
    except Exception as e:
        characters = f"Something went wrong, please try again. ERROR: {str(e)}"
        weapons = ""
        return weapons, characters #error message

    
'''
create_user(username, weapons, characters):

@param username, a string for the users desired username
@param weapons, a list of weapons that the user has
@param characters, a list of characters that the user has
@return message, a string tells the user if they were successful or not

Used to CREATE a user in the database
'''
def create_user(username, weapons, characters):
    message = "" #empty string holder
    try: #all expected outcomes
        response = table.get_item(Key={'Username': username}) #gets list of all usernames in db
        if 'Item' in response: #checks if the username is already taken 
            message = f"username, {username}, is already taken, please try something else" #error message if username is already taken 
        else: #if the username is not taken
            table.put_item( #putting the new user into the db
                Item={
                    'Username': username,
                    'Weapons': weapons,
                    'Characters': characters
                })
            message = "You have successfully created a user" #success message
    except Exception as e:
        message = f"Something went wrong, please try again. ERROR: {str(e)}"
        
    return message #output message

'''
delete_user(username)

@param username, the username of the user that would like to be deleted
@return message, a string that tells the user if they were successful or not 

Used to DELETE a user from the database
'''
def delete_user(username):
    message = "" #empty list holder
    try: #all expected outcomes 
        response = table.get_item(Key={'Username': username}) #gets list of all usernames in db
        if 'Item' in response: #checks if the username is in the database
            table.delete_item(Key={'Username': username}) #deletes the user
            message = f"{username} successfully deleted!" #success message
        else: #if the username is not in the db
            message = f"User, {username}, does not exist, please try again" #error message
    except Exception as e: #unexpected error occurs
        message = f"ERROR: {str(e)}" 
        
    return message #output message

'''
add_item(username, category, item)

@param username, a string for the users username 
@param category, the name of the variable to be accessed
@param item, the item to be added to the list
@return message, a string to tell the user if it was successful or not

Used to add an item to a list variable from the database
'''

def add_item(username, category, item):
    message = "" #empty string holder
    try: #expected outcomes
        response = table.get_item(Key={'Username': username}) #gets a list of usernames in the db
        if 'Item' in response: #checks in username is in the db
            if item in response.get('Item', {}).get(category, []): #checks if item is already in list
                message = f"{item} already in {category} list"
            else: #if not in list
                table.update_item( #updates the item list
                    Key={'Username': username}, #using the key 'Username'
                    UpdateExpression = f"SET {category} = list_append({category}, :i)", #adds the item to the chosen category list
                        ExpressionAttributeValues = { ':i' : [item]}) #the item to be added
                message = f"{item} added to {category} list successfully" #success message
        else: #if the username does not exist
            message = f"User, {username}, does not exist, please try again" #error message
    except Exception as e: #unexpected error occurs
        message = f"ERROR: {str(e)}"
        
    return message #output message

'''
index_item(List, item)

@param List, the list to be run through
@param item, the item to be searched for 
@return count, the index of the item 

Used to find the index of an item in a list
'''

def index_item(List, item):
    try:
        count = -1 #-1 because indexes start at 0
        for i in List: #loop through list 
            count += 1 #add 1 to the count 
            if i == item: #condition for loop to stop 
                return count #stops loop and returns the count
    except Exception as e: #if something goes wrong
        print(f"ERROR: {str(e)}") #print error to the console

'''
delete_item(username, category, item)

@param username, a string for the users username 
@param category, the name of the variable to be accessed
@param item, the item to be deleted from the list
@return message, a string to tell the user if it was successful or not

Used to remove an item from a list variable from the database
'''
def delete_item(username, category, item):
    message = "" #Output message to be displayed
    try: #all expected outcomes
        response = table.get_item(Key={'Username': username}) #get a list of the usernames in the database
        
        if 'Item' in response: #check to make sure that the usename is in the database
            if item in response.get('Item', {}).get(category, []): #checks to make sure that the item is not in the category list already
                index = index_item(response['Item'][category], item) #gets the index of the item in the list
                table.update_item( #updating the item
                    Key={'Username': username}, #using the key 'Username'
                        UpdateExpression = f"REMOVE {category}[{index}]") #removing the item
                message = f"{item} removed from {category} list successfully" #success message
            else: #if the item is not in the list
                message = f"{item} does not exist in {category} list" #failure message
        else: #is the username doe not exist
            message = f"User, {username}, does not exist, please try again" #failure message 
    except Exception as e: #unexpected error occurs
        message = f"ERROR: {str(e)}"
    
    return message #returns the message
