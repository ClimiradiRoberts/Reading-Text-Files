# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}



def read_file_content(filename):
    # [assignment] Add your code here 
    
    file_content = open(filename, "r")
    count = 0
    file_content.close()

    return file_content


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    text = text.translate(str.maketrans("", "", string.punctuation))

    word_count = {}
    text_to_split = text.split()

    word_count = collections.Counter(text_to_split)
    word_count = {k: v for k, v in word_count.items()}

    return word_count

    print(count_words())