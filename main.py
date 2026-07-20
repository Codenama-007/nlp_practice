import nltk
from nltk.tokenize import word_tokenize , sent_tokenize # for tokenizing the sentence 
from nltk.stem import PorterStemmer # for Stemming the Sentence 
from nltk.stem import WordNetLemmatizer # for performing lemmatization
from nltk.corpus import stopwords # for removing stopwords 
import re 

nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

text = """
Hello Everyone!!

I'm playing football with my friends at https://fifa.com.
My email is student123@gmail.com.
The players were running faster than anyone!
I scored 3 goals 😀😀.
"""

# Tokenization of the sentence 
def tokenization(sentence):
    tokens = sent_tokenize(sentence)
    for token in tokens:
        print(token)
    
    return tokens


# Stemming the Sentence 
def stemming(text):
    tokens = word_tokenize(text)
    stemms = {

    }
    for token in tokens:
        stemms.update(
            {
                f'{token}' : stemmer.stem(token)
            }
        )

    return stemms

# Lemmitization
def lemmitizing(sentence):
    tokens = word_tokenize(sentence)
    lemms = {}

    for token in tokens:
        lemms.update(
            {
                f'{token}' :lemmatizer.lemmatize(token) 
            }
        )
    
    return lemms
# removing Stop Words
def stopword_removal(words):

    stop_words = set(stopwords.words("english"))

    filtered_words = []

    for word in words:

        if word.lower() not in stop_words:
            filtered_words.append(word)

    return filtered_words
# Text filtaration
def filtration(text):

    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)

    # Remove Email Addresses
    text = re.sub(r'\S+@\S+', '', text)

    # Remove Numbers
    text = re.sub(r'\d+', '', text)

    # Remove Emojis / Non-ASCII Characters
    text = re.sub(r'[^\x00-\x7F]+', '', text)

    # Remove Extra Spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()




# Testing the Tokenization 
tokens = tokenization(text.lower())
print(" Tokenization Given Below ")
print(tokens)

# Testing the Stemming
text_2 = "The players played different games while running quickly and enjoying their achievements."
stemms = stemming(text_2.lower())
print(" Stemming Given Below ")
for key , value in stemms.items():
    print(f"{key} -> {value}")


# Testing the Lemmitization
text_3 = """
The children were running towards the mice while the geese were flying.
The better players were studying harder than the others.
"""

lems = lemmitizing(text_3.lower())
print(' Lemmitization given below ')
for key , value in lems.items():
    print(f'{key} -> {value}')


# Testing stopwords removal
text_4 = """
The students are studying in the library with their teachers and friends.
"""
words = word_tokenize(text_4.lower())
word = stopword_removal(words)
print(" Removed Stop Words ")
print(word)

# Testing Filtarations 
filtered_text = filtration(text)

print("Original Text")
print(text)

print()

print("Filtered Text")
print(filtered_text)
