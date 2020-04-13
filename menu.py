# menu classes
import os
import ast


class Message:

    def __init__(self):
        print("Create message[C]")
        print("Inbox[I]")
        print("Drafts[D]")
        print("Outbox[O]")
        print("Sent[S]")
        print("Exit[e-x]")
        command = input("Enter your command")

    def create_message(self):
        print("At any point in the begining of an input, enter 'e-x' to\
        exit")

        to = input("Enter contact name or id\n")
        if to == 'e-x':
            self.__init__()

        message = input("Enter your message\n")
        if message == 'e-x':
            self.__init__()

        command = input("Enter 'send' to send, 'save' to save to drafts\
        'back' to go back")

        if command == "back":
            self.__init__()
        
        id = 0
        if command == "send":
            # pick up id

            # This is for the contact to keep being prompted as long as they
            # keep making a mistake unless they opt to exit
            cond = True
            while cond:
                if isinstance(to, str):
                    # check for name in contacts.txt
                    # There is to be a file for contacts
                    # check for name in file and get the id
                    # if name in contacts; get id
                        cond = False
                    else:
                        print("Name is not in contact list. Enter the proper\
                        name of enter id")
                        to = input("Enter contact name or id\n")
                elif isinstance(to, int):
                    id = to
                    cond = False
                else:
                    print("Contact entry not valid. Please enter contact again")
                    to = input("Enter contact name or id\n")

            # got to the inbox of id
            """Check if the id is on the server. The server is where all ID's
            are saved as a table key and the value is the objective instance of the 
            mobile phone instantiated with the id
            """
            # add message to inbox and create notification
            # once sending is done, return to self.__init__

        if command == 'save':
            main_path = os.getcwd()
            draft = 'db\\drafts.txt'
            draft_file = os.join(main_path, draft)
            if not os.path.exists(draft_file):
                table = {}
                table[to] = message
                with open(draft_file, 'w') as f:
                    f.write(str(table))
            else:
                with open(draft_file, 'r') as f:
                    table = ast.literal_eval(f.read())
                table[to] = message
                with open(draft_file, 'w') as f:
                    f.write(str(table))
            os.chdir(main_path)
            self.__init__()
            # save to drafts file
            # need to work on repeated savings to same name or id
        
        # An idea is to create unique ids for each phone so messages 
        # can be sent between local phones

        