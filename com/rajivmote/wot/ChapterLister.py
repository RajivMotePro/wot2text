import sys
import csv
from com.rajivmote.wot.EbookBrowser import EbookBrowser

class ChapterLister:
    def list_chapters(self, toc_filename, chapters_filename):
        eb = EbookBrowser()
        books = eb.browse_ebook(toc_filename)
        header = ['book_num', 'book_title', 'chapter_num', 'chapter_title']
        with open(chapters_filename, 'w', newline='') as chapter_file:
            writer = csv.DictWriter(chapter_file, fieldnames=header)
            writer.writeheader()
            for book in books:
                book_num = book.get('number')
                book_title = book.get('title')
                chapters = book.get('chapters')
                for chapter in chapters:
                    chapter_num = chapter.get('number')
                    chapter_title = chapter.get('title')
                    row = { 'book_num': book_num, 'book_title': book_title, 'chapter_num': chapter_num, 'chapter_title': chapter_title }
                    writer.writerow(row)

def main():
    if len(sys.argv) > 2:
        toc_filename = sys.argv[1]
        chapters_filename = sys.argv[2]
        cl = ChapterLister()
        cl.list_chapters(toc_filename, chapters_filename)
    else:
        print("usage: toc_filename, chapters_filename")

if __name__ == "__main__":
    main()
