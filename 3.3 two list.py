pack = []
decode = []
bad_packs = 0

packs_amt = int(input('Кількість пакетів'))
for i_pack_num in range(packs_amt):
    print ('\n Пакет номер',i_pack_num+1)
    for i_bit in range(4):
        print (i_bit+1, 'біт', end=' ')
        num = int(input())
        pack.append(num)
    if pack.count(-1) <= 1:
        decode.extend(pack)
    else:
        print ('Багато помилок в пакеті')
        bad_packs += 1
    pack = []

    print  ('\n Отримані повідомлення', decode)
    print ('\n Кількість помилок в повідомленнях', decode.count(-1))
    print('\n Кількість втрачених пакетів', bad_packs)
