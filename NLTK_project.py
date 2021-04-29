import nltk, re, pprint
from nltk import word_tokenize
from collections import Counter
from nltk import punkt
#nltk.download('punkt')
#hoi



with open('little_engine.txt', 'r') as fic:
    content = fic.read().replace('\n', ' ')
sentences = list(map(str.strip, content.split(".")))

#text = engine.read()
punc = '''!()-[]}{;:'"\<>./?@#$%^&*_~'''

for sentence in sentences:
    for word in sentence:
        for ele in word:
            if ele in punc:
                word = word.replace(ele,"")
print(sentences)


print(len(sentences))

list_lengths = []
for sentence in sentences:
    words = sentence.split(' ')
    length = 0
    for word in words:
        length += 1
    list_lengths.append(length)

total = 0
for length in list_lengths:
    total += length

average_length = total/ len(sentences)
print(average_length)



#for ele in text:
    #if ele in punc:
        #text = text.replace(ele,"")


#sentences = nltk.tokenize.sent_tokenize(word)  
#print(sentences[0:10])    

#tokens = word_tokenize(text)

# print(tokens)

# words = [w.lower() for w in tokens]

# s_words = (sorted(words))

# def lexical_diversity(text):
#     return len(set(text))/ len(text)

# Counter = Counter(s_words)

# most_occur = Counter.most_common(15)

#print(most_occur)


#vocab = sorted(set(words))
