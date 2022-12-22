import random
import matplotlib.pyplot as plt
import pandas as pd

def double_dip(q,ans_list):
    print(q)
    for i in range(4):
        print(f'{i+1}. {ans_list[i]}')
    a=int(input('Enter your first choice: '))
    a-=1
    if ans_list[a] == ans_list[4]:
        # print(f'You won ₹{amt}')
        return True
    else:
        a=int(input('Enter your second choice: '))
        a-=1
        if ans_list[a] == ans_list[4]:
            # print(f'You won ₹{amt}')
            return True
        else:
            return False

def fifty(q,ans_list):
    print(q)
    rem1 = ''
    rem2 = ''
    while True:
        i = random.randint(0,3)
        rem1 = ans_list[i]
        # print(rem1)
        if rem1 != ans_list[4]:
            break
    ans_list.remove(rem1)
    while True:
        i = random.randint(0,2)
        rem2 = ans_list[i]
        # print
        if rem2 != ans_list[3]:
            break
    ans_list.remove(rem2)
    print('Your new options are:')
    for i in range(2):
        print(f'{i+1}. {ans_list[i]}')
    a=int(input('Enter your choice: '))
    a-=1
    if ans_list[a] == ans_list[2]: return True
    else: return False

def audience_poll(q,ans_list):
    prob = {}
    # ans_perc = 100
    
    perc = random.uniform(60.00,80.00)
    perc= round(perc,2)
    prob[ans_list[4]] = perc
    ans_perc = 100-perc
    # print(ans_perc)
    for i in ans_list:
        if i != ans_list[4]:
            perc = random.uniform(0.00,ans_perc)
            perc = round(perc,2)
            prob[i] = perc
            ans_perc = ans_perc-perc
            # print(ans_perc)
    x = [1,2,3,4]
    y=[]
    for i in range(4):
        x1 = x[i] - 1
        y.append(prob[ans_list[x1]])
    

    # s = pd.Series()
    # s.plot.bar(figsize=(20, 10))
    plt.bar(x,y)
    # plt.plot(x,y)
    plt.xlabel('Options')
    plt.ylabel('%')
    plt.title("Audience Poll")
    plt.show()
    print(q)

    for i in range(4):
        print(f'{i+1}. {ans_list[i]}')

    a=int(input('Enter your choice: '))
    a-=1
    if ans_list[a] == ans_list[4]: return True
    else: return False





ques = [
    {
        'Who is the king of jungle?': ['lion','tiger','elephant','leopard', 'lion'],
        'What is the capital of India?' : ['New Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'New Delhi']
    },
    {
        'Who is the king of jungle?': ['lion','tiger','elephant','leopard', 'lion'],
        'What is the capital of India?' : ['New Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'New Delhi']
    },
    {
        'Who is the king of jungle?': ['lion','tiger','elephant','leopard', 'lion'],
        'What is the capital of India?' : ['New Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'New Delhi']
    },
    {
        'Who is the king of jungle?': ['lion','tiger','elephant','leopard', 'lion'],
        'What is the capital of India?' : ['New Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'New Delhi']
    },
    {
        'Who is the king of jungle?': ['lion','tiger','elephant','leopard', 'lion'],
        'What is the capital of India?' : ['New Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'New Delhi']
    },
    {
        'Who is the king of jungle?': ['lion','tiger','elephant','leopard', 'lion'],
        'What is the capital of India?' : ['New Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'New Delhi']
    },
    {
        'Who is the king of jungle?': ['lion','tiger','elephant','leopard', 'lion'],
        'What is the capital of India?' : ['New Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'New Delhi']
    },
    {
        'Who is the king of jungle?': ['lion','tiger','elephant','leopard', 'lion'],
        'What is the capital of India?' : ['New Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'New Delhi']
    },
    {
        'Who is the king of jungle?': ['lion','tiger','elephant','leopard', 'lion'],
        'What is the capital of India?' : ['New Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'New Delhi']
    },
    {
        'Who is the king of jungle?': ['lion','tiger','elephant','leopard', 'lion'],
        'What is the capital of India?' : ['New Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'New Delhi']
    },
    {
        'Who is the king of jungle?': ['lion','tiger','elephant','leopard', 'lion'],
        'What is the capital of India?' : ['New Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'New Delhi']
    },
    {
        'Who is the king of jungle?': ['lion','tiger','elephant','leopard', 'lion'],
        'What is the capital of India?' : ['New Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'New Delhi']
    },

]
amount = [1000,5000,10000,50000,160000,320000,640000,1250000,2500000,5000000,10000000,50000000]
# game_over = False

used = []
# available = [1,2,3]

for i in range(len(amount)):
    print(f'Playing for ₹{amount[i]}')
    j = random.randint(0,1)
    questions = ques[i]
    # print(questions)
    q1 = list(questions.keys())
    q = q1[j]
    ans = questions[q][4]
    # print(ans)
    print(q)
    for op in range(4):
        print(f'{op+1}. {questions[q][op]}')
    a = int(input('Would you like to take lifeline, if yes, press 9\n\Choose any option:  or you can quit by pressing 8 \t\t'))
    if a==8:
        quit = input('Are you sure you want to quit(y/n)')
        if quit=='y':
            print(f'Congratulations you won {amount[i-1]}')
            # game_over=True
            break
        else:
            print('Lets go on!!')
            i-=1
    elif a==9:
        if len(used) !=3:
            print('Available lifelines:')
            if 1 not in used:
                print('Audience Poll (input 1)')
            if 2 not in used:
                print('50-50 (input 2)')
            if 3 not in used:
                print('Double Dip (input 3)')
            lifeline = int(input())

            if lifeline == 1 and lifeline not in used:
                print('You Choose 50-50')
                result = audience_poll(q,questions[q])
                used.append(1)
            
            elif lifeline == 2 and lifeline not in used:
                print('You Choose 50-50')
                result = fifty(q,questions[q])
                used.append(2)
            
            elif lifeline == 3 and lifeline not in used:
                print('You Choose Double Dip')
                result = double_dip(q,questions[q])
                used.append(3)
                # available.remove()
            # print(result)
            else:
                print('Incorrect Input')
                i-=1
            if result:
                print(f'You won ₹{amount[i]}')
                print()
                print()
                print()
                print()
                print()
            else:
                in_10k = amount.index(10000)
                in_320k = amount.index(320000)
                if i < in_10k:
                    print("Sorry! You didn't win anything")
                elif i >= in_10k and i < in_320k:
                    print(f'You won ₹10000!')
                else:
                    print('Congratulations! You won ₹320000')
                break
        else:
            print('No lifelines available')
            i-=1            
    else:
        a-=1
        if ques[i][q][a] == ans:
            print('Correct Answer!')
            print(f'You won ₹{amount[i]}')
            print()
            print()
            print()
            print()
            print()

        else:
            in_10k = amount.index(10000)
            in_320k = amount.index(320000)
            if i < in_10k:
                print("Sorry! You didn't win anything")
            elif i >= in_10k and i < in_320k:
                print(f'You won ₹10000!')
            else:
                print('Congratulations! You won ₹320000')
            break
            # game_over = True