#coding: utf-8

import os
import re
import chardet


in_file = "需要翻译的词语.txt"
in_file_english = "翻译词语_每行对齐.txt"

source_dir = "."

def get_encoding(file):
    with open(file,'rb') as f:
        tmp = chardet.detect(f.read())
        code = tmp['encoding']
        print(code)
        return code

word_match = dict()


with open(in_file, "r") as  f_word:
    with open(in_file_english, "r", encoding=get_encoding(in_file_english)) as  f_word_replace:
        word_lines = f_word.readlines()
        for word in word_lines:
            #print(str(word, get_encoding(file_path)))
            # print(word)
            word_replace = f_word_replace.readline()#.decode()
            word_match[word[:-1]] = word_replace[:-1]

# for word in word_match:
#     print(word)
#     print(word_match[word])
#     print("-------")



for root, dirs, files in os.walk(source_dir):
    for file in files:
        filename, ex = os.path.splitext(file)
        if ex == ".cpp" or ex == ".ui":
            file_path = os.path.join(root, file)
            print(file_path)
            with open(file_path, "r+", encoding=get_encoding(file_path)) as f:
                data = f.read()
                # print(data)
                print("*******************************")
                for word in word_match:
                    # word_temp = word.decode(get_encoding(file_path)).encode('utf-8')
                    if data.find(word) != -1:
                        # cpp
                        old = "tr(\"" + word + "\")"
                        new = "tr(\"" + word_match[word] + "\")"
                        data = data.replace(old, new)
                        print(old, new)
                        # ui
                        old = "<string>" + word + "</string>"
                        new = "<string>" + word_match[word] + "</string>"
                        data = data.replace(old, new)
                        print(old, new)
                # print(data)
                f.seek(0)
                f.truncate()
                f.write(data)
                # exit(0)
            # exit(0)