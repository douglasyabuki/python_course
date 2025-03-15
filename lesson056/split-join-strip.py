"""
split and join with list and str
split - splits a string (into a list)
join - joins a list into a string
"""
phrase = '   Look at this   , what an interesting thing          '
raw_phrase_list = phrase.split(',')

cleaned_phrase_list = []
for i, phrase in enumerate(raw_phrase_list):
    cleaned_phrase_list.append(raw_phrase_list[i].strip())  # Removes leading/trailing spaces

# print(raw_phrase_list)
# print(cleaned_phrase_list)

joined_phrases = ', '.join(cleaned_phrase_list)
print(joined_phrases)
