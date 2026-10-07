# Program 4 - Independent Task: Text Analyzer

sentence = input("Enter a sentence: ")      # input: I love Python
words = sentence.split()                    # ['I', 'love', 'Python']
print("Word count:", len(words))            # Output: Word count: 3
reversed_sentence = sentence[::-1]          # [::-1] -> ulta string
print("Reversed:", reversed_sentence)       # Output: Reversed: nohtyP evol I
