def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(book_path):
    return len(get_book_text(book_path).split())

def get_num_chars(book_path):
    chars = {}
    lower_book = get_book_text(book_path).lower()
    for i in lower_book:
        if i not in chars:
            chars[i] = 1
        else:
            chars[i] += 1
    return chars

def sort_dict(book_path):
    def sort_on(items):
        return items["num"]
    ordered = []
    formatted = []
    chars = get_num_chars(book_path)
    for key in chars:
        if key.isalpha():
            ordered.append({"char": key, "num": chars[key]})
    ordered.sort(reverse=True, key=sort_on)
    for item in ordered:
        formatted.append(f'{item["char"]}: {item["num"]}')
    return formatted 
