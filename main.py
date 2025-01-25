def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = count_words(text)
    num_characters = count_characters(text)
    report = report_list(num_characters)
    report.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for r in report:
        print(f"The '{r['char']}' character was found {r['num']} times")
    print("--- End report ---")

def get_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_dict = {}
    char_list = []
    lowered_text = text.lower()
    char_list = list(lowered_text)
    for l in char_list:
        if l in char_dict:
            char_dict[l] += 1
        else:
            char_dict[l] = 1
    return char_dict

def report_list(dict):
    report = []
    for d in dict:
        list = {}
        count = dict[d]
        if d.isalpha() == True:
            list["char"] = d
            list["num"] = count
            report.append(list)
    return report

def sort_on(dict):
    return dict["num"]

main()