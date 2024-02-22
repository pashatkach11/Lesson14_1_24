def correct_sentence(text):
    if text[-1] != ".":
        text = text + "."
    result = text.capitalize()
    return result

print(correct_sentence("greetings, friends."))