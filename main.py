import random
import time


def nub(x):
    nr = 0
    if x == 'rock':
        nr = 1
    elif x == 'paper':
        nr = 2
    elif x == 'scissors':
        nr = 3
    else:
        print("")
    return nr


def stg(y):
    if y == 1:
        sq = "rock"
    elif y == 2:
        sq = "paper"
    elif y == 3:
        sq = "scissors"
    else:
        print("error in stg module!!")

    return sq


time.sleep(2)
print('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
''')
time.sleep(2)
print('''
█░░░█ █▀▀ █░░ █▀▀ █▀▀█ █▀▄▀█ █▀▀
█▄█▄█ █▀▀ █░░ █░░ █░░█ █░▀░█ █▀▀
░▀░▀░ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░░░▀ ▀▀▀
''')
time.sleep(1)
print('''
▀▀█▀▀ █▀▀█
░░█░░ █░░█
░░▀░░ ▀▀▀▀
\n\n''')
time.sleep(2)
print('''
█▀▀█ █▀▀█ █▀▀ █░█
█▄▄▀ █░░█ █░░ █▀▄
▀░▀▀ ▀▀▀▀ ▀▀▀ ▀░▀
''')
time.sleep(0.5)
print('''
█▀▀█ █▀▀█ █▀▀█ █▀▀ █▀▀█
█░░█ █▄▄█ █░░█ █▀▀ █▄▄▀
█▀▀▀ ▀░░▀ █▀▀▀ ▀▀▀ ▀░▀▀
''')
time.sleep(0.5)
print('''
█▀▀ █▀▀ ░▀░ █▀▀ █▀▀ █▀▀█ █▀▀█ █▀▀
▀▀█ █░░ ▀█▀ ▀▀█ ▀▀█ █░░█ █▄▄▀ ▀▀█
▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░▀▀ ▀▀▀
''')
time.sleep(0.5)
print('''
█▀▀▀ █▀▀█ █▀▄▀█ █▀▀
█░▀█ █▄▄█ █░▀░█ █▀▀
▀▀▀▀ ▀░░▀ ▀░░░▀ ▀▀▀
\n\n\n''')
time.sleep(2)
print('''

                                                    █▀▀▄ █░░█   █▀▀ █░░█ █░░█ █▀▀▄ █░░█ █▀▀█ █▀▄▀█
                                                    █▀▀▄ █▄▄█   ▀▀█ █▀▀█ █░░█ █▀▀▄ █▀▀█ █▄▄█ █░▀░█
                                                    ▀▀▀░ ▄▄▄█   ▀▀▀ ▀░░▀ ░▀▀▀ ▀▀▀░ ▀░░▀ ▀░░▀ ▀░░░▀

\n\n\n''')
time.sleep(5)
print('''
┏━━━┓
┃┏━┓┃
┃┗━━┓
┗━━┓┃
┃┗━┛┃
┗━━━┛
''', end="")
print('''
▀▀█▀▀
░░█░░
░░▀░░
''', end="")
print('''
┏━━┓
┃┏┓┃
┃┏┓┃
┗┛┗┛
''', end="")
print('''
┏━━━┓
┃┏━┓┃
┃┗━┛┃
┃┏┓┏┛
┃┃┃┗┓
┗┛┗━┛
''', end="")
print('''
▀▀█▀▀
░░█░░
░░▀░░
''', end="")
time.sleep(4)
while True:
    ci = random.randint(1, 3)
    print("\n\t\t\t(¯`◕‿◕´¯)  . . 𝒫ℛℰ𝒮𝒮 ._E_N_T_E_R_. 𝒯𝒪 . 𝒫ℒ𝒜𝒴 . .  (¯`◕‿◕´¯) \n")
    entre = input("\n")
    print("\t\t\t ıllıllı 🇷‌🇴‌🇨‌🇰‌ ıllıllı\n\n")
    time.sleep(1)
    print("\t\t\t ıllıllı 🇵‌🇦‌🇵‌🇪‌🇷‌ ıllıllı \n\n")
    time.sleep(1)
    print("\t\t\t ıllıllı 🇸‌🇨‌🇮‌🇸‌🇸‌🇴‌🇷‌🇸‌ ıllıllı \n\n")
    time.sleep(1)
    print('''
    \n\n\n\t\t\t
    ▁ ▂ ▄ ▅ ▆ ▇ █ 𝐄𝐍𝐓𝐄𝐑 𝐘𝐎𝐔𝐑 𝐂𝐇𝐎𝐈𝐂𝐄 █ ▇ ▆ ▅ ▄ ▂ ▁
    ''')
    pi = input("\n\t-->")
    piN = nub(pi)
    ciS = stg(ci)
    print(f"\n\n\t\t\t you:{pi} ;; computer:{ciS} \n\n\n ")
    time.sleep(3.5)
    pwin = False
    if piN == 1 and ci == 2:
        pwin == False
        print("\t\t\tyou choosed rock and.. computer choosed paper; \n\t\t\t you got coverd by paper")
        print("\n\n\t\t\t 【｡_｡】 𝙔𝙊𝙐 𝙇𝙊𝙎𝙏!!! 【｡_｡】")
    elif piN == 2 and ci == 1:
        pwin == True
        print(
            "\t\t\tyou choosed paper and.. computer choosed rock; \n\t\t\t you coverd rock ")
        print("\n\n\t\t\t ░▒▓█►─═ 𝕐𝕆𝕌 𝕎𝕆ℕ!!! ═─◄█▓▒░")
    elif piN == 2 and ci == 3:
        pwin == False
        print("\t\t\tyou choosed paper and.. computer choosed scissiors; \n\t\t\t computer cut you down")
        print("\n\n\t\t\t 【｡_｡】 𝙔𝙊𝙐 𝙇𝙊𝙎𝙏!!! 【｡_｡】")
    elif piN == 3 and ci == 2:
        pwin == True
        print("\t\t\tyou choosed scissors and.. computer choosed paper; \n\t\t\t you tore down computer")
        print("\n\n\t\t\t ░▒▓█►─═ 𝕐𝕆𝕌 𝕎𝕆ℕ!!! ═─◄█▓▒░")
    elif piN == 3 and ci == 1:
        pwin == False
        print("\t\t\tyou choosed scissors and.. computer choosed rock; \n\t\t\t you got crushed by rock")
        print("\n\n\t\t\t 【｡_｡】 𝙔𝙊𝙐 𝙇𝙊𝙎𝙏!!! 【｡_｡】")
    elif piN == 1 and ci == 3:
        pwin == True
        print("\t\t\tyou choosed rock and.. computer choosed scissors; \n\t\t\t you crushed the rock")
        print("\n\n\t\t\t ░▒▓█►─═ 𝕐𝕆𝕌 𝕎𝕆ℕ!!! ═─◄█▓▒░")
    elif piN == ci:
        print("\n\n\t\t\t 💙💜💛🧡 </>  𝘛𝘐𝘌!?!  **𝘺𝘰𝘶 𝘣𝘰𝘵𝘩 𝘩𝘢𝘷𝘦 𝘴𝘢𝘮𝘦 𝘮𝘪𝘯𝘥𝘴𝘦𝘵** 🧡💛💜💙")
    else:
        print(
            f"(¯´•._.• ᴇɴᴛᴇʀ ʀᴏᴄᴋ ᴘᴀᴘᴇʀ ᴏʀ sᴄɪssᴏʀs <> ***ɴᴏᴛʜɪɴɢ ᴇʟsᴇ ʟɪᴋᴇ {pi} : ) •._.•´¯)")
    time.sleep(6.5)
    print('''\n\n\n\t\t\t
    ▀▄▀▄▀▄ ＬＥＴＳ ＰＬＡＹ ＡＧＡＩＮ!! ▄▀▄▀▄▀
    \n''')
    time.sleep(2)
