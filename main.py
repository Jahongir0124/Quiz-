import random

variants = ['A', 'B', 'C', 'D']
select_answer = []
score = 0
quiz = [
    {'question': "12 + 34",
     'answers': [46, 45, 34, 56],
     'correct': 46
     },
     {'question': "11 + 37",
     'answers': [48, 45, 34, 56],
     'correct': 48
     }
]


for i in range(len(quiz)):
    print(f"{i+1}.", quiz[i]['question'], "?")
    random.shuffle(quiz[i]['answers'])
    for j in range(len(variants)):
        print(f"{variants[j]}.{quiz[i]['answers'][j]}")

    answer = input("Select the option: ")
    try:
        index_answer = variants.index(answer.upper())
        select = quiz[i]['answers'][index_answer]
        correct_answer = quiz[i]['correct']
        if select == correct_answer:
            score += 1
        else:
            pass
    except Exception as e:
        print("Invalid input")
        break
print("Your result: ", score)  


