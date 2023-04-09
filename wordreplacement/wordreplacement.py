def replace_word():
    str = "hi guys, i am Martin, and hi hi hi hi"
    word_to_replace = input("Enter the word to replace: ")
    new_word = input("Enter the new word: ")
    print(str.replace(word_to_replace, new_word))
    
replace_word()