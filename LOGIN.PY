
#start
 #Importing Modules
try:
	import os, telegram, time, sys, logging
	from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
	from telegram.ext.dispatcher import run_async
	from functools import wraps
	from pprint import pprint
except ImportError as e:
	print("Problem: ",e)
	exit()

#Bot Data (Please insert bot token here!)
namebot = 'Login Test'
verbot  = 'v1' #<== You can change this version with your real bot version
tokenbot= '697365031:AAE6PpZ-u4tBq6xt3nI1hv2CGmZxdMgL3HM' #<-- Put your bot token here!

#polling setup
try:
	updater= Updater(tokenbot)
except ValueError as e:
	print("Please insert your tokenbot!")
	exit()

#handling command
dispatcher = updater.dispatcher

#logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#####################################################################################################################
#DATA
#####################################################################################################################

#Temporary Data (I will use mysql soon!)
users_data = {}
vip_developer = 293125876
users = {}
status = ""
 
def displayMenu():
    status = input("Are you registered user? y/n? Press q to quit")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
 
def newUser():
    createLogin = input("Create login name: ")
 
    if createLogin in users:
        print("\nLogin name already exist!\n")
    else:
        createPassw = input("Create password: ")
        users[createLogin] = createPassw
        print("\nUser created\n")
 
def oldUser():
    login = input("Enter login name: ")
    passw = input("Enter password: ")
 
    if login in users and users[login] == passw:
        print("\nLogin successful!\n")
    else:
        print("\nUser doesn't exist or wrong password!\n")
 
while status != "q":
    displayMenu()
   
#end
