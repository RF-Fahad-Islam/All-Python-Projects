import os

def wordFinder(word, filename):
    fileContent = True
    with open(filename, 'r') as f:
        # while fileContent:
        fileContent = f.read().lower()
        if word in fileContent:
            return True
        else:
            return False

files = os.listdir()
# print(files)
word = input("Enter a word that you want to find on this directory : ")
founded_files = 0
for item in files:
    if item.endswith('.txt'):
        print(f"\nDetecting {word} in {item}...")
        present = wordFinder(word.lower(), item)
        if present:
            print(f"*******hidden {word} found in {item}")
            founded_files += 1
        else:
            print(f"{word} is not found in {item}")
            
print("\n******Word Finder Summary******")
print(f"{word} found in total {founded_files} file(s)")
        
        
    