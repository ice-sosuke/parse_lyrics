import MeCab
import unidic

unidic_path = unidic.DICDIR
print(unidic_path)
# yomi = MeCab.Tagger("-r /usr/local/lib/mecab/dic/unidic/dicrc -d /usr/local/lib/mecab/dic/unidic -Oyomi")
#yomi = MeCab.Tagger("-r C:/Users/icela/enshu/Lib/site-packages/unidic/dicdir/dicrc -d C:/Users/icela/enshu/Lib/site-packages/unidic/dicdir -Oyomi")
yomi = MeCab.Tagger("-r C:/Users/icela/enshu/Lib/site-packages/unidic/dicdir/dicrc -d C:/Users/icela/enshu/Lib/site-packages/unidic/dicdir -Oaccent")

ret = yomi.parse("研究").split()
#ret = yomi.parse("大好き").split()

print(ret)
