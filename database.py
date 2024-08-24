#DatabaseManager manages database related queries/actions
class DatabaseManager:
    def __init__(self, notion_client, database_id):
        # Initialize Notion client and set the database ID
        self.notion = notion_client
        self.database_id = database_id

    #list each msg for specified recipient
    def list_recipient_messages(self, recipient):
        response = self.notion.databases.query(**{
            "database_id": self.database_id,
            "filter": {
                "property": "Recipient",
                "rich_text": {
                    "contains": recipient,
                },
            },
        })
        results = response["results"]
        num_msgs = len(results)
        page_ids = [x['id'] for x in results]

        messages = [x['properties']['Message']['title'][0]['text']['content'] for x in results]
        senders = [x['properties']['Sender']['rich_text'][0]['text']['content'] for x in results]
        sender_and_message_list = list(zip(senders, messages, page_ids))
        number_to_msg_mapping = {}
        for i in range(len(sender_and_message_list)):
            number_to_msg_mapping[i+1] = sender_and_message_list[i]

        return number_to_msg_mapping
    def read_recipient_messages(self,recipient):
        response = self.notion.databases.query(**{
            "database_id": self.database_id,
            "filter": {
                "property": "Recipient",
                "rich_text": {
                    "contains": recipient,
                },
            },
        })
        results = response["results"]
        num_msgs = len(results)
    
        messages = [x['properties']['Message']['title'][0]['text']['content'] for x in results]
        senders = [x['properties']['Sender']['rich_text'][0]['text']['content'] for x in results]
        sender_and_message_list = list(zip(senders, messages))
        return sender_and_message_list
        
    def read_mail(self):
        recipient = input("User: ")
        message_and_sender_list = self.read_recipient_messages(recipient)
        print(f"\nMessages ({len(message_and_sender_list)}):")
        for item in message_and_sender_list:
            sender,message = item[0],item[1]
            print(f"\nfrom: {sender}")
            print(f"{message}\n")