# Genshin Database 
This is a project that was done for my midterm project in Cloud and Database Systems (CS178) at Drake University.  

## Navigating the files
* WIP

## The Goal
* Create a new IAM user, Cloud9 EC2 instance, and an RDS instance in AWS
* Create a flask website that runs out of the EC2 instance. I also created an elastic IP, so that the IP wouldn't change for creating buttons that led to other pages.
* Create an SQL database that is linked to the RDS instance and have it connected to the website in some way
* Create a dynamoDB table and also have it connected to the website in some sort of way

## What I Made
* I decided that I would make a database of sorts based on my favorite video game, Genshin Impact. I tend to like to make things that have a genshin theme because it's more fun for me.  
* SQL Aspect: I created a page that would output a table full of different character info and reccomended builds that pulled data from my SQL schema. This can be found on my Database page.
* DynamoDB Aspect: I also wanted to have a place where users could make an account that can store a list of all the weapons and characters they have acquired. I made it so that they can create a user and add/remove characters and weapons from their profiles. The "Locker" is a place where they can see all of the weapons and characters that are on their list.

## Goals for the future 
* I would like to add a filtering system for the Database page and allow users to add more characters to the table.
* I would also like to somehow link the two databases. My thoughts are allowing them to filter "Owned Characters" on the database table and it only output the characters that match the characters on their list. Another thought was to display a reccomended build for every character that the person owns in the Locker.
* I also think it could be fun to have it liked with their actual genshin account somehow. That would probably utilize Hoyoverse in some way, but I'm not entirely sure how I would do it. 
