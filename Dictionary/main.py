import requests
word = input("Enter the word to get Definitions : ")
r = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
data = r.json()
# print(data)
for dicts in data:
    print(f"--------------- Word : \"{dicts.get('word')}\" ---------------")
    for item in dicts.get("phonetics"):
        print(f"{item.get('text')} => {item.get('audio')}")
    for item in dicts.get("meanings"):
        print(f"\n * Parts of speech : {item.get('partOfSpeech')}")
        for det in item.get("definitions"):
            print(f"Definition : {det.get('definition')}")
            print(f"Example : {det.get('example')}")