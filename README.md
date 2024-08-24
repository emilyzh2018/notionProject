## Description of the program and additional improvements(s) you selected.
The program is a simple command line interface program that utilizes python's 
argparse library for subparsers for the send,read and delete command. The program
allows for sending an email/msg from a specified sender to a specified recipient,
reading messages received from a specified recipient, and also deleting messages
received from a specified recipient. The notion-sdk-py is used to interact with 
the notion API: https://github.com/ramnes/notion-sdk-py . The database

## Description about how to install and run the program.
1. (Optional) Create and activate virtual environment
    `python -m venv .venv`
    Confirm .venv/ has been created
    `source .venv/bin/activate`
1. Install the necessary packages
    `pip install -r requirements.txt`
2. Create your notion integration key and database ID. Create a new database using
    table template, and connect that to a new integration. Retrieve the database ID through
    the URL for your database. Refer to these docs for more info: 
    https://developers.notion.com/docs/create-a-notion-integration#getting-started 
    https://developers.notion.com/docs/create-a-notion-integration#give-your-integration-page-permissions 
    
    ### You should store your notion integration token and database id in a seperate .env file for example, do not expose directly. 

    `NOTION_KEY=notion_integration_token`
    `DATABASE_ID=notion_database_id` 

3. run command `python3 notionProject.py` in terminal. 
    There are send, delete and read commands you can add after, for ex. `python3 notionProject.py send`. 
    Run `python3 notionProject.py -h` to see the help message.
    The send command allows a user to send a message/email to a specified receipient,
    and from a specified sender. The read command allows user to read messages sent
    to a specified user. The delete command allows user to delete messages send to a
    specified user. 

 
## List of references to sources you relied on (e.g. StackOverflow post about Node CLI applications, API docs, any open-source libraries).
https://www.geeksforgeeks.org/command-line-interface-programming-python/
https://docs.python.org/3/library/argparse.html 
https://docs.python.org/3/library/argparse.html#dest 
https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_subparsers 
https://github.com/ramnes/notion-sdk-py/blob/main/README.md?plain=1 
https://github.com/ramnes/notion-sdk-py 
https://developers.notion.com/docs/working-with-databases#adding-pages-to-a-database
https://developers.notion.com/reference/post-page 
https://developers.notion.com/reference/post-database-query-filter
https://developers.notion.com/reference/post-database-query
https://developers.notion.com/docs/create-a-notion-integration#give-your-integration-page-permissions 
https://developers.notion.com/docs/create-a-notion-integration#getting-started
https://developers.notion.com/docs/working-with-page-content 
https://developers.notion.com/docs/working-with-databases 
https://ramnes.github.io/notion-sdk-py/reference/api_endpoints/ 


## What are some future improvements you might make to this program or its code? What were some of the product or technical choices you made and why?
I would like to add unit tests for each method created to test multiple different edge cases/inputs.
Right now none of the methods in any classes are being tested, meaning there is 
a lack of code coverage and checking all branches' behaviors. 

Some design decisions I made include making classes such as a class for 
handling page related methods, a class for database related methods, etc. This 
makes the overall design more modular, readable and re usable in other classes/code. 

Another choice I made was using a dictionary/hashmap for mapping 
a number to each list containing the sender name, message, and page id. 
This allows for the user to select a number associated with the message they 
want deleted, and the page id to be easily accessible in o(1) time (hashmap 
look up) and passed into the other deletion method. 

I also decided to use subparsers in the argparser.ArgumentParser, and added a
parser for each subcommand (send,read, delete). 
