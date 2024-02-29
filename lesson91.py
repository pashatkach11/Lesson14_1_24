list_word = ['i', 'was', 'three', 'near']
text_str = "Hi! When I was One I had just begun When I was Two I was nearly new"


def popular_words(text, words):
    dict_count = {}
    text1 = ""
    text1 = text.lower()
    for i in words:
       dict_count.update({i: text1.count(" "+i+" ")})
    return dict_count

print(popular_words(text_str, list_word))

print("Ok")