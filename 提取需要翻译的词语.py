import os
import re
import chardet

out_file = "需要翻译的词语.txt"

source_dir = "."



def get_encoding(file):
    with open(file,'rb') as f:
        tmp = chardet.detect(f.read())
        return tmp['encoding']

word_match = set()
for root, dirs, files in os.walk(source_dir):
    for file in files:
        filename, ex = os.path.splitext(file)

        if ex == ".cpp":
            file_path = os.path.join(root, file)
            print(file_path)
            with open(file_path, "r", encoding=get_encoding(file_path)) as f:
                data = f.read()
        #tr("Error operation")
                tr = re.findall(r"tr\(\".*?\"\)", data)

                for match in tr:
                    match_temp = match[4:-2]
                    word_match.add(match_temp)
        
with open(out_file, "w") as  f_word:
    for word in word_match:
        f_word.write(word)
        f_word.write("\n")



word_match = set()
for root, dirs, files in os.walk(source_dir):
    for file in files:
        filename, ex = os.path.splitext(file)
        if ex == ".ui":
            file_path = os.path.join(root, file)
            print(file_path)
            with open(file_path, "r", encoding=get_encoding(file_path)) as f:
                data = f.read()
            # <string>ISO:</string>
                tr = re.findall(r"<string>.*?</string>", data)

                for match in tr:
                    print(match)
                    match_temp = match[8:-9]
                    word_match.add(match_temp)


with open(out_file, "a") as  f_word:
    for word in word_match:
        f_word.write(word)
        f_word.write("\n")
