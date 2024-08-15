def word_count(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    return word_count


def char_counter(text):
    chars = [0] * 26
    for char in text:
        if char.isalpha():
            chars[ord(char.lower()) - ord('a')] += 1
    chars_dict = {}
    for i in range(26):
        chars_dict[chr(i + ord('a'))] = chars[i]
    sorted_chars_dict = dict(sorted(chars_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_chars_dict


def print_report(file_path, text):
    print(f'--- Begin report of {file_path} ---')
    print(f'The book contains {word_count(text)} words.\n\n')
    for char, count in char_counter(text).items():
        print(f'the \'{char}\' character was found {count} times.')
    print('--- End report ---')


def main():
    file_path = 'books/frankenstein.txt'
    with open(file_path) as f:
        text = f.read()
        print_report(file_path, text)


if __name__ == '__main__':
    main()