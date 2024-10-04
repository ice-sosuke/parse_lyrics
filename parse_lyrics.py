# (): 読み仮名 []: ルビ ^: 空白 /: 改行　%: 副改行　<: 改貢 >: タブ
import re
lyrics_file_name = "C:/Users/icela/vsc_enshu/parse_lyrics/b0vDjryGdE.txt" 
ret = ''
with open(lyrics_file_name, 'r', encoding='utf-8') as F:
    for line in F:
        line_list = line.split()
        ret += line_list[1]
            # print(line_list[1])
            # self.lyrics += (line_list[1])
        
        # print(self.lyrics)
        # for i in range(self.lyrics):
        #     if i == "<":
        #         pass

# plaintext()
ret = ret.replace('<間奏','')
ret = ret.replace('<エンド','')


ret = ret.replace('/','\n')
ret = ret.replace('<','\n')
ret = ret.replace('^','　')

ret = re.sub(r'\[.*?\]', '', ret)

# ret.replace('>','')
# print(ret)  

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(ret+'\n')

