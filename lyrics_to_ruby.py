# (): 読み仮名 []: ルビ ^: 空白 /: 改行　%: 副改行　<: 改貢 >: タブ
import re
import os

# f = open("list_Yamaha_MIDI_20240930.txt", 'r', encoding="utf-8")
# datalist = f.readlines()
# f.close()

# print(len(datalist))

# for data in datalist:
#     div_data = data.split()
#     ID = div_data[0]
#     file = 'C:/Users/icela/Desktop/org_lyrics/'+  ID + ".txt"
#     if not os.path.exists(file):
#         continue

ret = ''
# file = "C:/vsc_enshu/parse_lyrics/A0AGBi5Ac0.txt"
file = "C:/vsc_enshu/parse_lyrics/b0vDjryGdE.txt"
with open(file, 'r', encoding='utf-8') as F:
    for line in F:
        line_list = line.split()
        # print("file", file)
        if len(line_list) < 2:
            continue
        #ret += line_list[1]
        line_lyrics = line_list[1]

        if '[' in line_lyrics:
            print("[あるよ")
            print(line_lyrics)
            matches = re.findall(r'\[.*', line_lyrics)
            print("line_lyrics", matches)
            line_lyrics = re.sub(r'\[', '', matches[0])
            print(line_lyrics)

        if ']' in line_lyrics:
            print("]あるよ")
            print(line_lyrics)
            matches = re.findall(r'.*?\]', line_lyrics)
            print("line_lyrics", matches)
            line_lyrics = re.sub(r'\]', '', matches[0])
            print(line_lyrics)

        ret += line_lyrics

# org_lyrics_path = "C:/Users/icela/Desktop/org_lyrics"
# lyrics_file_name = "C:/Users/icela/vsc_enshu/parse_lyrics/b0vDjryGdE.txt" 

ret = ret.replace('<イントロ','')
ret = ret.replace('<INTRODUCTION','')
ret = ret.replace('<間奏','')
ret = ret.replace('<エンド','')
ret = ret.replace('<エンディング','')
ret = ret.replace('<ENDING','')

#ret = re.sub(r'\[.*?\]', '', ret)
ret = re.sub(r'\（.*?\）', '', ret)

ret = ret.replace('/','\n')
ret = ret.replace('<','\n')
ret = ret.replace('^','　')

# ret.replace('>','')
# print(ret)  

#os.chdir("C:/Users/icela/vsc_enshu/parse_lyrics/plain_text")
os.chdir("C:/vsc_enshu/parse_lyrics/ruby_text")

# output = "A0AGBi5Ac0" + "_ruby.txt"
output = "b0vDjryGdE" + "_ruby.txt"
with open(output, 'w', encoding='utf-8') as f:
    f.write(ret+'\n')
#os.chdir("C:/Users/icela/vsc_enshu/parse_lyrics/plain_text")
os.chdir("C:/vsc_enshu/parse_lyrics")