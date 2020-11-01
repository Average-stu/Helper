from nltk.chat.util import Chat, reflections
from Login import login
from account_details import G_password, G_username,Insta_password,Insta_username
from time import sleep

# Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?", ]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you \nWhat do you need ?", ]
    ],
    [
        r"(.*) your name ?",
        ["I am Helper , Just here to chat with you and solve your Problems .", ]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind that", ]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that", "Alright, great !", ]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there", ]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse", ]

    ],
    [
        r"(.*)created(.*)",
        ["Aman created me for his Cyber-security journey ", "top secret ;)", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Not sure about Location ,But he is Indian', ]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2", "In %2 there is a 50% chance of rain", ]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ", ]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Football", ]
    ],
    [
        r"who (.*) (moviestar|actor|actress)?",
        ["Zendaya"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear, Would be adding more feature']
    ],
]

my_dummy_reflections= {
    "go"     : "gone",
    "hello"    : "hey there"
}

#default message at the start of chat
print("Hi, I'm Helper and I am here to help \nPlease type lowercase English language to start a conversation. Type quit to leave and Get back to business xd")

#Create Chat Bot
chat = Chat(pairs, reflections ,)

#Start conversation
chat.converse()
print("Let get to work \nShall we xd")
sleep(2)
print("Setting up Your enviroment")
sleep(2)
get = login(G_username,G_password,Insta_username,Insta_password)
get.G_login()
get.Insta_login()
