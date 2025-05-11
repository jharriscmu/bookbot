def count_words(text):
    words = text.split()
    return len(words)
def count_characters(text):
    char_counts ={}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
def sort_character_counts(char_counts):
    sorted_chars = []
    for char, count in char_counts.items():
        if char.isalpha():
            sorted_chars.append({"char": char, "num": count})
    sorted_chars.sort(key=lambda item: item["num"], reverse=True)
    return sorted_chars
    