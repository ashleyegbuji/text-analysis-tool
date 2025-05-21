from random_username.generate import generate_username
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
wordLemmatizer = WordNetLemmatizer()
import re

# Welcome User
def welcomeUser():
    print("\nWelcome to the text analysis tool, I will mine and analyze a body of text from a file you gave me!")

# Get Username
def getUsername():

    maxAttempts = 3
    attempts = 0

  
    while attempts < maxAttempts:

      # Print message prompting user to input their name
      inputPrompt = ""
      if attempts == 0:
          inputPrompt = "\nTo begin, please enter your username:\n"
   
      else:  
        inputPrompt = "\nPlease try again:\n"
      usernameFromInput = input(inputPrompt)

      # Validate Username
      if len(usernameFromInput) < 5 or not usernameFromInput.isidentifier():
          print("Username must be at least 5 characters long, alphanumeric only (a-z/A-Z/0-9), and underscore only, no spaces and cannot start with a number!")
      else:    
          return usernameFromInput

      attempts =+ 1
      
    print("\nExhausted all " + str(maxAttempts) + " attempts, assigning username instead...")
    return generate_username()[0]   


# Greet the user
def greetUser(name):
    print("Hello, " + name)

# Get text from file
def getArticleText():
    f = open("files/article.txt", "r")
    rawText = f.read()
    f.close()
    return rawText.replace("\n", " ").replace("\r", "") 
    
# Extract sentences    
def tokenizeSentences(rawText):
    return sent_tokenize(rawText)    

# Extract Words from list of Sentences
def tokenizeWords(Sentences):
    words = []
    for sentence in sentences:
        words.extend(word_tokenize(sentence))
    return words
def extractKeySentences(sentences):
    matchedSentences = []
    for sentence in sentences:
        # If sentence matches desired pattern, add to matchedSentences
        if re.search(searchPattern, sentence.lower()):
           matchedSentences.append(sentence)
    return matchedSentences       

# Get the average words per sentence, excluding punctuation
def getWordsPerSentence(sentences):
    totalWords = 0
    for sentence in sentences:
        totalWords += len(sentence.split(" "))
    return totalWords / numSentences

# Filter raw tokenized words list to only include
# valid english words
def cleanseWordList(words):
	cleansedWords = []
	invalidWordPattern = "[^a-zA-Z-+]"
	for word in words:
		cleansedWord = word.replace(".", "").lower()
		if (not re.search(invalidWordPattern, cleansedWord)) and len(word) > 1:
			cleansedWords.append(wordLemmatizer.lemmatize(cleansedWord))
	return cleansedWords

# Get User details
welcomeUser()
username = getUsername()  
greetUser(username)     

# Extract and tokenize text 
articleTextRaw = getArticleText()
articleSentences = tokenizeSentences(articleTextRaw)
articleWords = tokenizeWords(articleSentences)

# Get Sentence Analytics
stockSearchPattern = "[0-9]|[%$€£]|thousand|million|billion|trillion|profit|loss"
keySentences = extractKeySentences(articleSentences, stockSearchPattern)
wordsPerSentence = getWordsPerSentence(articleSentences)

# Get Word Analytics
articleWordsCleansed = cleanseWordList(articleWords)

# Print for testing
print("GOT:")
print(articleWordsCleansed)