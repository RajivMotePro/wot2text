import os
import sys
import xml.etree.ElementTree
from com.rajivmote.wot.AsciiNormalizer import AsciiNormalizer

class EbookBrowser:
    out_dir = "./"
    chapter_dir = os.path.join(out_dir, "TEXT")

    def browse_ebook(self, toc_filename):
        books = []
        out_dir = os.path.dirname(toc_filename)
        #Read the Table of Contents file
        with open(toc_filename, "r") as toc_file:
            root = xml.etree.ElementTree.parse(toc_file).getroot()
            root = root.find('./{http://www.w3.org/1999/xhtml}body/{http://www.w3.org/1999/xhtml}nav')
            lists = root.findall('{http://www.w3.org/1999/xhtml}ol')
            book_num = 0
            for list in lists:
                items = list.findall('{http://www.w3.org/1999/xhtml}li')
                for item in items:
                    book_node = item.find('{http://www.w3.org/1999/xhtml}a')
                    book = { 'number': book_num, 'title': AsciiNormalizer.to_ascii(book_node.text), 'chapters': [] }
                    chapter_list = item.find('{http://www.w3.org/1999/xhtml}ol')
                    if (chapter_list):
                        chapter_nodes = chapter_list.findall('{http://www.w3.org/1999/xhtml}li')
                        last_chapter_num = -1
                        for chapter_node in chapter_nodes:
                            ch = chapter_node.find('{http://www.w3.org/1999/xhtml}a')
                            chapter_title = AsciiNormalizer.to_ascii(ch.text)
                            chapter_file = os.path.join(out_dir, ch.get('href'))
                            # parse out chapter number
                            ch_num_str = chapter_title.partition(' ')[0].partition('.')[0]
                            chapter_num = -1
                            if (ch_num_str == 'Prologue:'):
                                chapter_num = 0
                            elif (ch_num_str == 'Epilogue:'):
                                chapter_num = last_chapter_num + 1
                            elif (ch_num_str.isnumeric()):
                                chapter_num = int(ch_num_str)
                            if (chapter_num >= 0):
                                last_chapter_num = chapter_num
                                book.get('chapters').append({ 'number': chapter_num, 'title': chapter_title, 'file': chapter_file })
                        books.append(book)
                        book_num = book_num + 1
        return books


    def print_books(self, books):
        for book in books:
            print(book.get('number'), book.get('title'))
            try:
                book_title = book.get('title')
                book_title.encode('ascii')
            except UnicodeEncodeError as err:
                print('\t', err)
            chapters = book.get('chapters')
            for chapter in chapters:
                print('\t', chapter.get('number'), chapter.get('title'), chapter.get('file'))
                chapter_name = chapter.get('title')
                try:
                    chapter_name.encode('ascii')
                except UnicodeEncodeError as err:
                    print('\t', '\t', err, err.start, err.end)

def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        eb = EbookBrowser()
        books = eb.browse_ebook(file_name)
        eb.print_books(books)
    else:
        print("No filename specified")

if __name__ == "__main__":
    main()
