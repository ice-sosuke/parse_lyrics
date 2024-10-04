# (): 読み仮名 []: ルビ ^: 空白 /: 改行　%: 副改行　<: 改貢 >: タブ
import re,os

f = open("list_Yamaha_MIDI_20240930.txt", 'r', encoding="utf-8")
datalist = f.readlines()
f.close()

print(len(datalist))

unique_chars = set()

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
            pattern = r'[^A-Za-z\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]'
            result = re.findall(pattern, ret)
            unique_chars.update(set(result))  # 文字列をセットにして統合

unique_chars_list = sorted(unique_chars)
# print(unique_chars_list)

with open('unique_chars_list.txt', 'w', encoding='utf-8') as f:
    for str in unique_chars_list:
        f.write(str+'\n')

# class parse_lyrics:
#     def __init__(self):
#         self.midi_list_path = "C:/Users/icela/vsc_enshu/parse_lyrics/list_Yamaha_MIDI_20240930.txt"
#         self.org_lyrics_path = "C:/Users/icela/Desktop/org_lyrics"
#         # self.lyrics = []
#         self.lyrics = ""
#         self.lyrics_list = [[]]

#     def load_data(self):
#         f = open(self.midi_list_path, 'r', encoding="utf-8_sig")
#         datalist = f.readlines()
#         f.close()
#         for data in datalist:
#             div_data = data.split()
#             file = div_data[0]
#             file = file + ".txt"
#             self.lyrics.append(file)

#             path = self.org_lyrics_path + '/' + file
#             #print(path)
#             with open(path) as F:
#                  for line in F:
#                     line_list = line.split()
#                     #self.lyrics.append(line_list[1])
#                     self.lyrics += (line_list[1])

#             self.lyrics_list.append(self.lyrics)

#         print(self.lyrics_list)
#         return self.lyrics_list
    
#     def plaintext(self):
#         with open("C:/Users/icela/vsc_enshu/parse_lyrics/b0vDjryGdE.txt") as F:
#             for line in F:
#                 line_list = line.split()
#                 print(line_list[1])
#                 self.lyrics += (line_list[1])

        
#         print(self.lyrics)
#         # for i in range(self.lyrics):
#         #     if i == "<":
#         #         pass

#     plaintext()
    

