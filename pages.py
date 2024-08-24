from database import DatabaseManager

#DatabaseManager manages database related queries/actions
class PageManager: 
    def __init__(self, notion_client, database_id):
        #Create Notion client and set the database ID
        self.notion = notion_client
        self.database_id = database_id
    def send_mail(self): 
        sender = input("Sender: ")
        recipient = input("Recipient: ")
        message = input("Message: ")
        self.create_page_in_database(message,recipient,sender)

    def create_page_in_database(self, message, recipient, sender):
        #Create page data to create a new page in the database
        page_data = {
            "parent": { 
                "type": "database_id",
                "database_id": self.database_id
            },
            "properties": {
                "Message": {
                    "title": [
                        {
                            "text": {
                                "content": message
                            }
                        }
                    ]
                },
                "Recipient": {
                    "rich_text": [
                        {
                            "text": {
                                "content": recipient
                            }
                        }
                    ]
                },
                "Sender": {
                    "rich_text": [
                        {
                            "text": {
                                "content": sender
                            }
                        }
                    ]
                }
            }
        }

        #Create the page
        response = self.notion.pages.create(**page_data)

        #Handle response
        if response:
            print("Message sent!")

    def delete_message(self, page_id):
        #Archive msg and move the page to trash, can't actually delete 
        #according to docs
        response = self.notion.pages.update(**{
            "page_id": page_id,
            "archived": True,
            "in_trash": True,
        })

        if response:
            print("Successfully deleted message.")

    def delete(self):
        #Show messages for a recipient and let them select which to delete
        #number is associated with the page to delete
        recipient = input("user: ")
        database_manager = DatabaseManager(self.notion,self.database_id)
        number_to_messages_map = database_manager.list_recipient_messages(recipient)

        if len(number_to_messages_map) < 1:
            print("No messages to delete.")
            return

        print("Messages you have to delete:\n")
        for num in number_to_messages_map:
            sender = number_to_messages_map[num][0]
            msg = number_to_messages_map[num][1]
            page_id = number_to_messages_map[num][2]
            print(f"Message #{num} \nfrom: {sender} \nmessage: {msg}\n")

        msg_number = int(input("Select message number to delete: "))
        self.delete_message(number_to_messages_map[msg_number][2])