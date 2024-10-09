import os,sys
import re
import MeCab

# (): 読み仮名 []: ルビ ^: 空白 /: 改行 %: 副改行 <: 改貢 >: タブ

f = open('Res_PlainTextInPhrases.txt', 'r', encoding='UTF-8')
lines = f.readlines()
f.close()
lines = [l.replace("\n", "") for l in lines]

yomi = MeCab.Tagger("-r C:/Users/icela/enshu/Lib/site-packages/unidic/dicdir/dicrc -d C:/Users/icela/enshu/Lib/site-packages/unidic/dicdir -Oaccent")
fo = open('Res_MeCab_Yomi.txt', 'w', encoding='UTF-8')
for i in range(len(lines)):
    ret = yomi.parse(lines[i]).split()
    fo.write('\t'.join(ret)+'\n')
fo.close()