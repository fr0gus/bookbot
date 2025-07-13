def count_words(string: str) -> int:
    word_list = string.split()
    return len(word_list)

def count_letters(string: str):
    alphabet = {chr(i):0 for i in range(ord('a'), ord('z') + 1)}

    for letter in string:
        if letter.lower() in alphabet:
            alphabet[letter.lower()] += 1
            
    return alphabet

def sort_on(items):
    return items["num"]

def letter_list(count_dict):
    letters = [{"char": letter, "num": count} for letter, count in count_dict.items()] 
    letters.sort(reverse=True, key=sort_on)

    return letters
