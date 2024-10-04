# (): 読み仮名 []: ルビ ^: 空白 /: 改行　%: 副改行　<: 改貢 >: タブ
import re
import os

#f = open("list_Yamaha_MIDI_20240930.txt", 'r', encoding="utf-8")
f = open("only_b0vDjryGdE.txt", 'r', encoding="utf-8")
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

    output = "C:/vsc_enshu/parse_lyrics/check_tick_ruby_text/" + ID + "_check.txt"
    f = open(output, 'w', encoding='utf-8')
    with open(file, 'r', encoding='utf-8') as F:
        for line in F:
            line_list = line.split()
            # print("file", file)
            if len(line_list) < 2:
                continue
            #ret += line_list[1]
            line_lyrics = line_list[1]

            if '[' in line_lyrics:
                #print(line_lyrics)
                matches = re.findall(r'\[.*', line_lyrics)
                #print("line_lyrics", matches)
                line_lyrics = re.sub(r'\[', '', matches[0])
                #print(line_lyrics)

            if ']' in line_lyrics:
                #print(line_lyrics)
                matches = re.findall(r'.*?\]', line_lyrics)
                #print("line_lyrics", matches)
                line_lyrics = re.sub(r'\]', '', matches[0])
                #print(line_lyrics)

            #ret += line_lyrics
            
            f.write(line_list[0] + '\t' + line_lyrics + '\n')
    
    f.close()