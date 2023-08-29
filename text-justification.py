# https://leetcode.com/problems/text-justification/



class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line_chars = 0          # number of chars on current line
        line_words = []         # list of words on current line
        justified = []          # output, list of justified strings

        for word in words:

            if line_chars + len(line_words) + len(word) <= maxWidth: 
                line_words.append(word)
                line_chars += len(word)

            else:                                   # word cannot be added to current line
                gaps = len(line_words) - 1          # nb gaps between words
                spaces = maxWidth - line_chars      # nb of spaces to make line maxWidth
                line = [line_words[0]]              # list of words and spaces
                if gaps == 0:                       # pad end if single word
                    line.append(" " * spaces)

                for line_word in line_words[1:]:    # distribute spaces between other words
                    space = spaces//gaps
                    if spaces % gaps != 0:          # round up if uneven division of spaces
                        space += 1
                    line.append(" " * space)        # add space
                    spaces -= space                 # reduce remaining spaces and gaps
                    gaps -= 1
                    line.append(line_word)

                justified.append("".join(line))

                line_words = [word]                 # add word to next line.
                line_chars = len(word)

        final_line = " ".join(line_words)           # pad final line with spaces
        final_line += " " * (maxWidth - len(final_line))
        justified.append(final_line)

        return justified
