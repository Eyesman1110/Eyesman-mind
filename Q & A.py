

QA={'1.what is your name?:':{1:['AEye','Amanda','America']},
    '2.How old are you?:':{2:['20~25','25~30','30~35']},
    '3.what do you do?:': {3: ['lawyer', 'engineer', 'alternative military service ']}
    }






def Question_answer(Question, option, Answer):
    print(Question)
    op=list(option.values())[0]
    for select,each_option in enumerate(op,start=1):
        print(select,').',each_option)
    while True:
        input_A = input('select the answer')
        if [int(input_A)] == list(Answer.keys()):
            print('nice choose')
            break
        else:
            print('WTF')
for i,v in QA.items():
    Question_answer(i,v,v)
