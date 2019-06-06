
import os
import sys
import zipfile

from com.rajivmote.wot.EbookBrowser import EbookBrowser
from com.rajivmote.wot.ChapterConverter import ChapterConverter

class WotConverter:

    def convert_wot(self, wot_epub, temp_dir, out_dir):
        #Unzip ebook to temp directory
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        with zipfile.ZipFile(wot_epub, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        #Read table of contents
        toc_file_name = os.path.join(temp_dir, "nav.xhtml")
        eb = EbookBrowser()
        books = eb.browse_ebook(toc_file_name)
        #Iterate over chapters and convert them into the output directory
        cc = ChapterConverter()
        for book in books:
            chapters = book.get('chapters')
            for chapter in chapters:
                in_chapter_filename = chapter.get('file').partition('#')[0]

                chapter_text = cc.convert_chapter(in_chapter_filename)
                out_chapter_filename = "WoT-Book{:02d}Chapter{:02d}.txt".format(book.get('number'), chapter.get('number'))
                out_chapter_filename = os.path.join(out_dir, out_chapter_filename)
                with open(out_chapter_filename, 'w') as chapter_file:
                    chapter_file.write(chapter_text + '\n')

def main():
    if len(sys.argv) > 3:
        wot_epub = sys.argv[1]
        temp_dir = sys.argv[2]
        out_dir = sys.argv[3]
        wc = WotConverter()
        wc.convert_wot(wot_epub, temp_dir, out_dir)
    else:
        print("Usage: <wot_epub> <temp_dir> <out_dir>")

if __name__ == "__main__":
    main()
