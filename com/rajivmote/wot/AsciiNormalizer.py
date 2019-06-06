class AsciiNormalizer:

    def to_ascii(s):
        all_ascii = False
        while not all_ascii:
            try:
                s.encode('ascii')
                all_ascii = True
            except UnicodeEncodeError as err:
                non_ascii = s[err.start:err.end]
                if non_ascii == '\u2019':
                    s = s.replace(non_ascii, "'")
                elif non_ascii == '\xa0':
                    s = s.replace(non_ascii, '...')
                else:
                    s = s.replace(non_ascii, ' ')
        return s
