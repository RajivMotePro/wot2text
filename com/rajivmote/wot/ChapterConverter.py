import sys
import xml.etree.ElementTree

from com.rajivmote.wot.AsciiNormalizer import AsciiNormalizer

class ChapterConverter:

    def convert_chapter(self, chapter_filename):
        content = ""
        with open(chapter_filename, "r") as in_file:
            content = in_file.read()
        content = ''.join(xml.etree.ElementTree.fromstring(content).itertext())
        content = AsciiNormalizer.to_ascii(content)
        return content

def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        cc = ChapterConverter()
        print(cc.convert_chapter(file_name))
    else:
        print("No filename specified")

if __name__ == "__main__":
    main()

