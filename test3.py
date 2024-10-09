f = open('Res_MeCab_Yomi.txt', 'r', encoding='UTF-8')
lines = f.readlines()
f.close()

f = open('Res_MeCab_Yomi_gived.txt', 'r', encoding='UTF-8')
lines_gived = f.readlines()
f.close()


count = 0
fo = open('Dif_MeCab_Yomi.txt', 'w', encoding='UTF-8')
for i in range(len(lines)):
    if lines[i] != lines_gived[i]:
        print(i, lines[i])
        fo.write(lines[i] + lines_gived[i] + "\n")
        count += 1
fo.close()

if count == 0:
    print("clear")
else:
    print(count)