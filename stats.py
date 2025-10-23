def get_word_count(text):
    return len(text.split())

def sort_character_counts(char_counts):
    sorted_char_counts = []
    for char in char_counts:
        if char.isalpha():
            sorted_char_counts.append({'char': char, 'num': char_counts[char]})

    sorted_char_counts.sort(reverse=True, key=lambda item: item['num'])

    return sorted_char_counts

def get_character_count(text):
    char_count = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1
    
    return sort_character_counts(char_count)