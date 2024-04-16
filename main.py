def main(path_to_file: str) -> str:
    with open(path_to_file) as f:
        contents = f.read()
        return contents


def wordcount(contents: str):
    words = contents.split()
    return len(words)


def count_letters(contents: str) -> list:
    # Generate a list of lowercase ASCII characters
    ascii_lowercase = [chr(i) for i in range(ord('a'), ord('z') + 1)]

    # Initialize a dictionary with lowercase ASCII characters as keys
    ascii_dict = {char: 0 for char in ascii_lowercase}

    for i in contents:
        char = i.lower()
        if char in ascii_dict.keys():
            ascii_dict[char] += 1

    chars = []
    for key, value in ascii_dict.items():
        new_dict = {"char": key, "val": value}
        chars.append(new_dict)

    # print(chars)

    def sort_on(ascii_dict):
        return ascii_dict['val']

    chars.sort(reverse=True, key=sort_on)

    return chars

    # get a list of lower ascii letters
    # initiate a dictionary
    # update the dictionary while traversing over the contents


def report(contents: str) -> str:
    wc = wordcount(contents)
    chars_list = count_letters(contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wc} words found in the document")
    print("")

    for i in chars_list:
        print(f"The {i['char']} character was found {i['val']} times")

    print("--- End report ---")


if __name__ == "__main__":
    contents = main('books/frankenstein.txt')
    report(contents)
