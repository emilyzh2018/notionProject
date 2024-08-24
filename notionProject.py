import os
from dotenv import load_dotenv
from notion_client import Client
import argparse 
from pages import PageManager
from database import DatabaseManager
#load .env variables
load_dotenv() 
#create a notion client and get database id to use
notion = Client(auth=os.environ["NOTION_KEY"])
database_id = os.environ["DATABASE_ID"]

def main():
    #Pass in notion client and database id
    page_manager = PageManager(notion,database_id)
    database_manager = DatabaseManager(notion,database_id)

    #Create argument parser
    parser = argparse.ArgumentParser(description="Notion CLI")

    #Subparser for subcommands
    subparsers = parser.add_subparsers(dest="command")
    #send command
    send_parser = subparsers.add_parser('send', help="Send mail to a user.")
    send_parser.set_defaults(func=page_manager.send_mail)

    #read command
    read_parser = subparsers.add_parser('read', help="Check a user's mail.")
    read_parser.set_defaults(func=database_manager.read_mail)
    #delete command
    read_parser = subparsers.add_parser('delete', help="Delete a user's mail.")
    read_parser.set_defaults(func=page_manager.delete)
    
    args = parser.parse_args()
    if args.command is None:
        print("Welcome to NotionMail!\nPlease select an option:\n"
                    "  - send: Send mail to a user.\n"
                    "  - read: Check a user's mail.\n"
                    "  - delete: Delete a user's mail.\n")
    else:
        args.func()


if __name__ == "__main__":
    main()
