myDict = {
    "programming": "the process of writing computer programs",
    'accidial': "dial someone's number on phone accidentally", 
    'bitcoin': 'an online payment system that does not require an intermediary',
    'conlang': 'an invented language intended for human communication'
}
print(f"Choose from this words :\n{list(myDict.keys())}\n")
user = input("Enter the word you want to know meaning : ")
print(f"The meaning of {user} is :\n\"{myDict.get(user)}\"")