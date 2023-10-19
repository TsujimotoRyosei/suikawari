import random
import sys

print('プレイヤーの名前を入力してください')
player_nm = str(input())
print('1:easy 2:normal 3:hard')
print('モードを選択してください')
mode = str(input())
print('モンスターが現れた')

if mode == '1':
    player_mp = int(random.randrange(50,81)) #プレイヤーのMP
    player_hp = int(random.randrange(50,101)) #プレイヤーのHP
    monster_hp = int(random.randrange(50,101))#モンスターのHP
    while(monster_hp > 0):
        player_at = int(random.randrange(10,16))  #プレイヤーの攻撃
        player_mt = int(random.randrange(20,31))  #プレイヤーの魔法攻撃
        player_rc = int(random.randrange(25,41))  #プレイヤーの回復
        monster_ch = str(random.randrange(0,2))   #モンスターの選択
        monster_at = int(random.randrange(20,26))  #モンスターの攻撃
        print(str(player_nm) + 'のHP:' + str(player_hp) + ' ' + str(player_nm) + 'のMP:' + str(player_mp))
        print('モンスターのHPは' + str(monster_hp))
        print('1:剣で攻撃 2:魔法で攻撃(MP20) 3:回復 4:逃げる')
        player_ch = input()
        if player_ch == '1':   #剣で攻撃を選んだ場合
            monster_hp -= player_at
            print(str(player_nm) + 'は剣で攻撃をした')
            print('モンスターに' + str(player_at) + 'ダメージ与えた')
            if monster_hp > 0:  #モンスターが倒れなかった場合
                player_hp -= monster_at
                print('モンスターが攻撃してきた')
                print(str(player_nm) + 'は' + str(monster_at) + 'ダメージ受けた')
                if player_hp <= 0:  #プレイヤーが倒れた場合
                    print(str(player_nm) + 'は倒れた')
                    sys.exit(0)
        elif player_ch == '2':  #魔法で攻撃を選んだ場合
            if player_mp > 20:
                monster_hp -= player_mt
                player_mp -= 20
                print(str(player_nm) + 'は魔法で攻撃をした')
                print('モンスターに' + str(player_mt) + 'ダメージを与えた')
                if monster_hp > 0:  #モンスターが倒れなかった場合
                    player_hp -= monster_at
                    print('モンスターが攻撃してきた')
                    print(str(player_nm) + 'は' + str(monster_at) + 'ダメージ受けた')
                    if player_hp <= 0: #プレイヤーが倒れた場合
                        print(str(player_nm) + 'は倒れた')
                        sys.exit(0)
            else:
                print('魔法を使うことができない')
        elif player_ch == '3':  #回復を選んだ場合
            player_hp += player_rc
            player_mp += player_rc
            player_hp -= monster_at
            print(str(player_nm) + 'は' + 'HPとMPが' + str(player_rc) + '回復した')
            print('モンスターが攻撃してきた')
            print(str(player_nm) + 'は' + str(monster_at) + 'ダメージ受けた')
        elif player_ch == '4':  #逃げるを選んだ場合
            print(str(player_nm) + 'は逃げた')
            if monster_ch == '0': #逃げることに成功した場合
                print('モンスターから逃げることに成功した')
                sys.exit(0)
            elif monster_ch == '1': #逃げることに失敗した場合
                print('しかしモンスターから逃げることができなかった')
        else: #1~4以外の文字を入力した場合
            print('1~4の数字を入力してください')
    print('モンスターを倒した')

elif mode == '2':
    player_mp = int(random.randrange(60,91)) #プレイヤーのMP
    player_hp = int(random.randrange(70,101)) #プレイヤーのHP
    monster_hp = int(random.randrange(50,151))#モンスターのHP
    while(monster_hp > 0):
        player_at = int(random.randrange(10,16))  #プレイヤーの攻撃
        player_mt = int(random.randrange(20,31))  #プレイヤーの魔法攻撃
        player_rc = int(random.randrange(25,41))  #プレイヤーの回復
        monster_ch = str(random.randrange(0,2))   #モンスターの選択
        monster_at = int(random.randrange(20,26))  #モンスターの攻撃
        print(str(player_nm) + 'のHP:' + str(player_hp) + ' ' + str(player_nm) + 'のMP:' + str(player_mp))
        print('モンスターのHPは' + str(monster_hp))
        print('1:剣で攻撃 2:魔法で攻撃(MP20) 3:回復 4:逃げる')
        player_ch = input()
        if player_ch == '1':   #剣で攻撃を選んだ場合
            monster_hp -= player_at
            print(str(player_nm) + 'は剣で攻撃をした')
            print('モンスターに' + str(player_at) + 'ダメージ与えた')
            if monster_hp > 0:  #モンスターが倒れなかった場合
                player_hp -= monster_at
                print('モンスターが攻撃してきた')
                print(str(player_nm) + 'は' + str(monster_at) + 'ダメージ受けた')
                if player_hp <= 0:  #プレイヤーが倒れた場合
                    print(str(player_nm) + 'は倒れた')
                    sys.exit(0)
        elif player_ch == '2':  #魔法で攻撃を選んだ場合
            if player_mp > 20:
                monster_hp -= player_mt
                player_mp -= 20
                print(str(player_nm) + 'は魔法で攻撃をした')
                print('モンスターに' + str(player_mt) + 'ダメージを与えた')
                if monster_hp > 0:  #モンスターが倒れなかった場合
                    player_hp -= monster_at
                    print('モンスターが攻撃してきた')
                    print(str(player_nm) + 'は' + str(monster_at) + 'ダメージ受けた')
                    if player_hp <= 0: #プレイヤーが倒れた場合
                        print(str(player_nm) + 'は倒れた')
                        sys.exit(0)
            else:
                print('魔法を使うことができない')
        elif player_ch == '3':  #回復を選んだ場合
            player_hp += player_rc
            player_mp += player_rc
            player_hp -= monster_at
            print(str(player_nm) + 'は' + 'HPとMPが' + str(player_rc) + '回復した')
            print('モンスターが攻撃してきた')
            print(str(player_nm) + 'は' + str(monster_at) + 'ダメージ受けた')
        elif player_ch == '4':  #逃げるを選んだ場合
            print(str(player_nm) + 'は逃げた')
            if monster_ch == '0': #逃げることに成功した場合
                print('モンスターから逃げることに成功した')
                sys.exit(0)
            elif monster_ch == '1': #逃げることに失敗した場合
                print('しかしモンスターから逃げることができなかった')
        else: #1~4以外の文字を入力した場合
            print('1~4の数字を入力してください')
    print('モンスターを倒した')

elif mode == '3':
    player_mp = int(random.randrange(70,101)) #プレイヤーのMP
    player_hp = int(random.randrange(70,151)) #プレイヤーのHP
    monster_hp = int(random.randrange(80,201))#モンスターのHP
    while(monster_hp > 0):
        player_at = int(random.randrange(10,16))  #プレイヤーの攻撃
        player_mt = int(random.randrange(20,31))  #プレイヤーの魔法攻撃
        player_rc = int(random.randrange(25,41))  #プレイヤーの回復
        monster_ch = str(random.randrange(0,2))   #モンスターの選択
        monster_at = int(random.randrange(20,26))  #モンスターの攻撃
        print(str(player_nm) + 'のHP:' + str(player_hp) + ' ' + str(player_nm) + 'のMP:' + str(player_mp))
        print('モンスターのHPは' + str(monster_hp))
        print('1:剣で攻撃 2:魔法で攻撃(MP20) 3:回復 4:逃げる')
        player_ch = input()
        if player_ch == '1':   #剣で攻撃を選んだ場合
            monster_hp -= player_at
            print(str(player_nm) + 'は剣で攻撃をした')
            print('モンスターに' + str(player_at) + 'ダメージ与えた')
            if monster_hp > 0:  #モンスターが倒れなかった場合
                player_hp -= monster_at
                print('モンスターが攻撃してきた')
                print(str(player_nm) + 'は' + str(monster_at) + 'ダメージ受けた')
                if player_hp <= 0:  #プレイヤーが倒れた場合
                    print(str(player_nm) + 'は倒れた')
                    sys.exit(0)
        elif player_ch == '2':  #魔法で攻撃を選んだ場合
            if player_mp > 20:
                monster_hp -= player_mt
                player_mp -= 20
                print(str(player_nm) + 'は魔法で攻撃をした')
                print('モンスターに' + str(player_mt) + 'ダメージを与えた')
                if monster_hp > 0:  #モンスターが倒れなかった場合
                    player_hp -= monster_at
                    print('モンスターが攻撃してきた')
                    print(str(player_nm) + 'は' + str(monster_at) + 'ダメージ受けた')
                    if player_hp <= 0: #プレイヤーが倒れた場合
                        print(str(player_nm) + 'は倒れた')
                        sys.exit(0)
            else:
                print('魔法を使うことができない')
        elif player_ch == '3':  #回復を選んだ場合
            player_hp += player_rc
            player_mp += player_rc
            player_hp -= monster_at
            print(str(player_nm) + 'は' + 'HPとMPが' + str(player_rc) + '回復した')
            print('モンスターが攻撃してきた')
            print(str(player_nm) + 'は' + str(monster_at) + 'ダメージ受けた')
        elif player_ch == '4':  #逃げるを選んだ場合
            print(str(player_nm) + 'は逃げた')
            if monster_ch == '0': #逃げることに成功した場合
                print('モンスターから逃げることに成功した')
                sys.exit(0)
            elif monster_ch == '1': #逃げることに失敗した場合
                print('しかしモンスターから逃げることができなかった')
        else: #1~4以外の文字を入力した場合
            print('1~4の数字を入力してください')
    print('モンスターを倒した')
else:
    print('1〜3の数字を入力してください')