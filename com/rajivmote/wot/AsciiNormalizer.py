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
                    s = s.replace(non_ascii, '')
                elif non_ascii == '\u2014':
                    s = s.replace(non_ascii, '--')
                elif non_ascii == '\u201c':
                    s = s.replace(non_ascii, '"')
                elif non_ascii == '\u201d':
                    s = s.replace(non_ascii, '"')
                elif non_ascii == '\u2026':
                    s = s.replace(non_ascii, '...')
                elif non_ascii == '\u2018':
                    s = s.replace(non_ascii, "'")
                elif non_ascii == '\u2013':
                    s = s.replace(non_ascii, '-')
                elif non_ascii == '\xe7':
                    s = s.replace(non_ascii, 'c')
                else:
                    print("NON-ASCII:", non_ascii, err)
                    s = s.replace(non_ascii, ' ')
        return s
