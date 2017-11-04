import string
import random
import time

'''managing highscores'''


def leaderboard_management(player_name, filex):
    with open(filex, "r") as lb:
        names = []
        score = []
        f = lb.readline()
        while f != "":
            temp = f[:-1]
            temp = temp.split("\t")
            names.append(temp[0])
            score.append(temp[1])
            f = lb.readline()
        lb.close()
    for i in range(len(score)):
        for j in range(len(score) - 1):
            if (int(score[j]) < int(score[j + 1])):
                score[j], score[j + 1] = score[j + 1], score[j]
                names[j], names[j + 1] = names[j + 1], names[j]

    print("\n--------------------------LEADERBOARD--------------------------------\n")
    print("RANK \t" + "NAME" + " " * 21 + "SCORE")
    for e in range(len(score)):
        f = 25 - len(names[e])
        print(str(e + 1) + ". \t" + names[e] + " " * f + score[e])
    last = input("\nDO YOU WANT TO PLAY AGAIN (Y/N) : ").upper()
    if last == "Y":
        lang_option(player_name)
    else:
        print("THANKS FOR PLAYING OUR QUIZ\n")
        star = input("please give feedback/rating : ")
        with open("rating.txt", "a+") as r:
            r.write(player_name + "\t" + star + "\n")
        r.close()


'''recording score of player'''


def highscore(player_name, filename, score):
    filex = filename[0]
    filex += "leaderboard.txt"
    with open(filex, "a+") as lb:
        lb.write(player_name + "\t" + str(score) + "\n")
        lb.close()
    leaderboard_management(player_name, filex)


'''scoring message'''


class scoring:
    def cor_msg(self, no):
        msg = {1: "may be ur lucky", 2: "alright nice!", 3: "did someone call streak?",
               4: "you are on fire!!", 5: "looks like u r a pro!"}
        print("\n" + msg[no] + "\n")

    def incor_msg(self, no):
        msg = {1: "oops!", 2: "bad luck!", 3: "wrong wrong wrong...",
               4: "concentrate!", 5: "better luck next time!"}
        print("\n" + msg[no] + "\n")


'''FACT OF NUMBER'''


def num_fact(score):
    fp = open("m.txt", "r")
    x = fp.readline()
    sc_ore = str(score)

    while(x != ""):
        t = x.split()
        if t[0] == sc_ore:
            print("********************************************\n")
            print(x)
            print("********************************************\n")
            break
        x = fp.readline()
    fp.close()


''''scoring animation'''


def final_score(player_name, filename, score):
    possibleCharacters = string.digits

    target = str(score)
    attemptThis = ''.join(random.choice(possibleCharacters)
                          for i in range(len(target)))
    attemptNext = ''

    completed = False

    while completed == False:
        print("SCORE ..." + attemptThis + " ...")
        attemptNext = ''
        completed = True
        for i in range(len(target)):
            if attemptThis[i] != target[i]:
                completed = False
                attemptNext += random.choice(possibleCharacters)
            else:
                attemptNext += target[i]
        attemptThis = attemptNext
        time.sleep(0.1)

    print("\n" + player_name + " YOUR SCORE IS " + str(target) + " POINTS!\n")
    print(player_name + " DO YOU KNOW ???\n")
    num_fact(target)
    time.sleep(2)
    highscore(player_name, filename, score)


x = scoring()


def bringpro(player_name, file, score):
    key = file[0]
    key = key + ".txt"
    if file[0] == "P":
        ans = {1: 'D', 2: 'A', 3: 'B', 4: 'A', 5: 'D'}
    elif file[0] == "C":
        ans = {1: 'D', 2: 'C', 3: 'B', 4: 'B', 5: 'A'}
    else:
        ans = {1: 'C', 2: 'C', 3: 'A', 4: 'D', 5: 'B'}
    with open(key, "r") as pro:
        i = 1
        correct = incorrect = 0
        line = pro.readline()
        print("----------- THIS IS GOING TO BE TOUGH ------------\n")
        time.sleep(1)
        while line != '':
            while line != '$end\n':
                print(line)
                line = pro.readline()
            start_t = time.time()
            omr = input("option : ").upper()
            t_taken = time.time() - start_t
            t_taken = round(t_taken)
            if omr == ans[i]:
                print("correct!")
                correct += 1
                x.cor_msg(correct)
                score += (20 - (t_taken) / 2)
            else:
                print("incorrect!")
                incorrect += 1
                x.incor_msg(incorrect)
            i += 1
            time.sleep(0.8)
            line = pro.readline()
            print("----------------------")
        pro.close()
        final_score(player_name, file, int(score))


def _quiz(player_name, filename, ans):
    print("\n THIS QUIZ CONTAINS 5 MODERATE LEVEL QUESTIONS \n EACH QUESTION HAS MAX 20 MARKS \n TIME PENALTY WILL BE CHARGED \n")
    time.sleep(1)
    with open(filename, "r") as p:
        i = 1
        correct = incorrect = xxx = 0
        line = p.readline()
        print("----------------------")
        while line != '':
            time.sleep(2)
            while line != '$end\n':
                print(line)
                line = p.readline()
            start_t = time.time()
            omr = input("option : ").upper()
            t_taken = time.time() - start_t
            t_taken = round(t_taken)
            if omr == ans[i]:
                print("correct!")
                correct += 1
                x.cor_msg(correct)
                xxx += (20 - (t_taken) / 2)
            else:
                print("incorrect!")
                incorrect += 1
                x.incor_msg(incorrect)
            i += 1
            line = p.readline()
            print("----------------------")
        p.close()
        # print(int(xxx))
        time.sleep(1)
        if correct >= 4:
            print("\n*** SEEMS YOU'VE GOT THE SKILL, proceed to pro level ***\n")
            print(" Y - YEAH, BRING 'EM ON!!")
            print(" N - NO, IT'S ENOUGH FOR ME!!\n")
            PRIO = input(" Y / N : ").upper()
            if (PRIO == 'Y'):
                bringpro(player_name, filename, int(xxx))
            else:
                final_score(player_name, filename, int(xxx))
        else:
            final_score(player_name, filename, int(xxx))


'''calling quiz language'''


def question(player_name, lang):
    x = random.randrange(3)
    if lang == "1":
        filename = "Pquiz" + str(x) + ".txt"
        ans0 = {1: 'B', 2: 'C', 3: 'A', 4: 'C', 5: 'C'}
        ans1 = {1: 'C', 2: 'B', 3: 'A', 4: 'B', 5: 'C'}
        ans2 = {1: 'D', 2: 'B', 3: 'B', 4: 'D', 5: 'A'}
        if x == 0:
            _quiz(player_name, filename, ans0)
        elif x == 1:
            _quiz(player_name, filename, ans1)
        else:
            _quiz(player_name, filename, ans2)

    elif lang == "2":
        filename = "Cquiz.txt"
        ans = {1: "D", 2: "A", 3: "A", 4: "A", 5: "A"}
        _quiz(player_name, filename, ans)

    elif lang == "3":
        y = random.randrange(2)
        filename = "Hquiz" + str(y) + ".txt"
        ans0 = {1: 'B', 2: 'B', 3: 'A', 4: 'D', 5: 'A'}
        ans1 = {1: 'C', 2: 'A', 3: 'A', 4: 'C', 5: 'A'}
        if y == 0:
            _quiz(player_name, filename, ans0)
        else:
            _quiz(player_name, filename, ans1)

    else:
        print("####BOMB HAS BEEN PLANTED#### \n ####!!! PLEASE CALL DEVELOPERS !!!####")


'''input player name'''


def lang_option(player_name):

    choice = "N"
    per = 0
    while choice == "N":
        flag = 1
        print("\n  -----------HELLO " + player_name +
              " CHOOSE A LANGUAGE U WANNA QUIZ IN ------\n")
        print(" 1) >>>PYTHON \n\n 2) { C } \n\n 3) <> HTML/CSS </>")
        language = input("\noption no.: ")
        if language == "1" or language == "a" or language == "A" or language == "python" or language == "PYTHON":
            option = "PYTHON"
            language = "1"
        elif language == "2" or language == "B" or language == "b" or language == "c" or language == "C":
            option = "C"
            language = "2"
        elif language == "3" or language == "html" or language == "HTML":
            option = "HTML/CSS"
            language = "3"
        else:
            if per == 3:
                print("SORRY! WE CAN'T UNDERSTAND YOU!")
                return
            print("\n ***--PLEASE BE COOL--***\n PLEASE ENTER 1/2/3 or a/b/c")
            flag = 0
        if flag == 0:
            choice = "N"
        else:
            print("\n" + player_name + " YOU HAVE SELECTED " + option)
            choice = input("CONTINUE( Y / N ): ").upper()
        per += 1
    question(player_name, language)


'''start page'''


def start():
    one = [
        "    ******   ", "    *     *    ", "    *******    ", "    ******  "
    ]
    two = [
        "    *    *   ", "    *     *    ", "       *       ", "        *   "
    ]
    three = [
        "    *    *   ", "    *     *    ", "       *       ", "       *    "
    ]
    four = [
        "    *    *   ", "    *     *    ", "       *       ", "      *     "
    ]
    five = [
        "    ****\\\\ ", "      *******    ", "    *******    ", "    *******  "
    ]
    print("\n")
    for x in one:
        print(x, end=" ")
    print("    ||")
    for x in two:
        print(x, end=" ")
    print("    ||")
    for x in three:
        print(x, end=" ")
    print("    ||")
    for x in four:
        print(x, end=" ")
    print("    ||")
    for x in five:
        print(x, end=" ")
    print("   ||")
    print(" " * 17 + "DEVELOPED BY: SHOBHIT MALARYA && SHIVAM SINGH YADAV")
    print("\n" * 2)
    time.sleep(0.5)
    player_name = input("YOUR NAME: ")
    # easter egg
    if player_name == "VALAR MORGHULIS":
        print("# easter egg #")
        with open("VALARMORGHULIS.txt", "r") as sp1:
            uu = sp1.read()
            print(uu)
            sp1.close()
        return
    if player_name == "TYLER DURDEN":
        print("# easter egg #")
        with open("TYLERDURDEN.txt", "r") as sp2:
            uu = sp2.read()
            print(uu)
            sp2.close()
        return
    if player_name == "SHOBHIT" or player_name == "SHIVAM":
        print("\n!!! SPOILER ALERT!!!\n")
        print(" ))*developers*(( ! name==cs ! ")
        return
    # easter egg
    lang_option(player_name)


'''HERE HERE WOOOOOOOOOHOOOOOOOOOOOOOOO'''


def main():
    start()


if __name__ == "__main__":
    main()
