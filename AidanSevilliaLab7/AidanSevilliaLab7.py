class Message: # create class to call in demo function

    sender = ''
    recipient = ''
    body = ''
    line = str('')

    def __init__(self, sender, recipient): #initialize everything

        self.sender =  sender
        self.recipient = recipient
        self.body = ''

    def to_string(self): # create main function that returns results
        return '\033[1;31;0m \nTo: {}  \nFrom: {} \n \n\033[1;35;0mFor Christmas I want: \033[1;34;0m \n{}'.format(self.recipient, self.sender, self.body)

    def append_body(self, line): #create tack-on function to add 'line' to the end of 'body'

        self.body = self.body + line + '\n'


    def str_ok(self, line): #create string length checker for running in demo file

        if len(line) <= 10:
            #print("Message length acceptable.")
            return True
        else:
            #print("Message too long.")
            return False


