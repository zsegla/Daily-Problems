# https://leetcode.com/problems/word-frequency/



# Read from the file words.txt and output the word frequency list to stdout.
# cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -rn | awk '{print $2 " " $1}'


cat words.txt | tr -s ' ' '\n' | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -nr | awk '{print $2, $1}'
