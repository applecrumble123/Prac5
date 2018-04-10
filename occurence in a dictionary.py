text = str(input("Enter a sentence: "))
text = text.split()
my_dict = {word : text.count(word) for word in text}
for word, value in my_dict.items():
    print("{:<10} : {:>5}".format(word, value))
