""" A program to reverse words in a given paragraph """

import glob
import os

PATH = "./examples/"
paragraphs = []
reverse_word_paragraphs = []


def get_reverse_word_paragraph(paragraph):
    """ Returns a paragraph by reveresing the words in the given text"""
    reverse_word_paragraph = ""
    list_of_lines = paragraph.split(".")
    for line in list_of_lines:
        if not line.strip() == "":
            list_of_words = line.split()
            for word in list_of_words:
                reverse_word_paragraph += word[::-1] + " "
            reverse_word_paragraph = reverse_word_paragraph.strip() + ". "
    return reverse_word_paragraph

for file_name in glob.glob(os.path.join(PATH, "*.txt")):
    paragraph_file = open(file_name, 'r')

    paragraph = paragraph_file.read()
    paragraphs.append(paragraph)
    reverse_word_paragraphs.append(get_reverse_word_paragraph(paragraph))

    paragraph_file.close()


for index in range(len(paragraphs)):
    print("Example", index+1)
    print("\nParagraph:\n", paragraphs[index])
    print("\nReverse Paragraph:\n", reverse_word_paragraphs[index])
    print("\n")
