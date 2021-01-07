import os
import re
import chardet

in_file = "PanoduxDemo/panoclient_zh.ts"

word_file = "需要翻译的词语.txt"
word_replace_file = "翻译词语_每行对齐.txt"

def get_encoding(file):
    with open(file,'rb') as f:
        tmp = chardet.detect(f.read())
        return tmp['encoding']

with open(in_file, "r", encoding=get_encoding(in_file)) as f:
    data = f.read()
    print(data)
    
    # tr = re.findall(r"<source>.*?</translation>", data)
    tr = re.findall(r"<source>[\s\S]*?</translation>", data)

    # print(tr)
    # for match in tr:
    #     print(match)
    #     print("*********")


if 1:
    word_match = dict()
    with open(word_file, "r", encoding=get_encoding(word_file)) as  f_word:
        with open(word_replace_file, "r", encoding=get_encoding(word_replace_file)) as  f_word_replace:
            word_lines = f_word.readlines()
            for word in word_lines:
                #print(str(word, get_encoding(file_path)))
                # print(word)
                if len(word) > 0:
                    word_replace = f_word_replace.readline()#.decode()
                    word_match[word_replace[:-1]] = word[:-1]

    with open(in_file, "r+", encoding=get_encoding(in_file)) as f:
        data = f.read()

        for word in word_match:

            # <source>search</source>
            # <translation type="unfinished"></translation>

            # <source>搜索连接</source>
            # <translatorcomment>搜索连接中文</translatorcomment>
            # <translation>搜索连接</translation>
            # src = "<source>" + word + "</source>"# + "<translation type=\"unfinished\"></translation>"
            # dst = "<source>" + word + "</source>" + "\n" + "<translatorcomment>" + word_match[word] + "</translatorcomment>" + "\n" + "<translation>" + word + "</translation>"
            # data = data.replace(src, dst)


            old_str = "<source>" + word + "</source>" + "[\s\S]*?</translation>"
            new_str = "<source>" + word + "</source>" + "\n\t\t" + "<translatorcomment>" + word + "</translatorcomment>" + "\n\t\t" + "<translation>" + word_match[word] + "</translation>"

            print("old_str:", old_str)
            print("new_str:", new_str)

            data = re.sub(old_str, new_str, data)
        
        f.seek(0)
        f.truncate()
        f.write(data)

