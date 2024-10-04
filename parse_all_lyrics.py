# (): 読み仮名 []: ルビ ^: 空白 /: 改行　%: 副改行　<: 改貢 >: タブ
import re
import os

f = open("list_Yamaha_MIDI_20240930.txt", 'r', encoding="utf-8")
datalist = f.readlines()
f.close()

print(len(datalist))

for data in datalist:
    div_data = data.split()
    ID = div_data[0]
    file = 'C:/Users/icela/Desktop/org_lyrics/'+  ID + ".txt"
    if not os.path.exists(file):
        continue
    ret = ''
    with open(file, 'r', encoding='utf-8') as F:
        for line in F:
            line_list = line.split()
            # print("file", file)
            if len(line_list) < 2:
                continue
            ret += line_list[1]

    # org_lyrics_path = "C:/Users/icela/Desktop/org_lyrics"
    # lyrics_file_name = "C:/Users/icela/vsc_enshu/parse_lyrics/b0vDjryGdE.txt" 
    
    ret = ret.replace('<イントロ','')
    ret = ret.replace('<INTRODUCTION','')
    ret = ret.replace('<間奏','')
    ret = ret.replace('<エンド','')
    ret = ret.replace('<エンディング','')
    ret = ret.replace('<ENDING','')



    ret = ret.replace('/','\n')
    ret = ret.replace('<','\n')
    ret = ret.replace('^','　')

    ret = re.sub(r'\[.*?\]', '', ret)

    # ret.replace('>','')
    # print(ret)  

    #os.chdir("C:/Users/icela/vsc_enshu/parse_lyrics/plain_text")
    os.chdir("C:/vsc_enshu/parse_lyrics/plain_text")

    output = ID + "_plain.txt"
    with open(output, 'w', encoding='utf-8') as f:
        f.write(ret+'\n')
    #os.chdir("C:/Users/icela/vsc_enshu/parse_lyrics/plain_text")
    os.chdir("C:/vsc_enshu/parse_lyrics")