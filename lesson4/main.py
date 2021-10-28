from const import QUIZ_DCT
score = 0
for e in QUIZ_DCT.keys():
    for k in QUIZ_DCT[e].keys():
        print('Категория: {}'.format(e))
        i = 0
        for j in QUIZ_DCT[e][k].keys():
            if i == 0 or i == 1:
                print("{}: {}".format(j, QUIZ_DCT[e][k][j]))
                i+=1
            if i == 2:
                x = input('Введите ваш вариант ответа: ')
                if x == QUIZ_DCT[e][k]['Правильный ответ']:
                    print('Супер!')
                    score += 1
                    break
                else:
                    print('Фу. Неправильно')
                    break
print(score)
