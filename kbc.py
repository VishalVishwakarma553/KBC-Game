import random
import pygame
import time
from colorama import Fore, Style
pygame.mixer.init()
right_answer_sound = pygame.mixer.Sound('right_answer.wav')
wrong_answer_sound = pygame.mixer.Sound('wrong_answer.wav')
Questions  = {
    'Which god is also known as Gauri Nandan?':'A. Agni B. Indra C. Hanuman D. Ganesha',
    'What does not grow on tree according to a popular Hindi saying?': 'A. Money B. Flower C. Leaves D. Fruits',
    'Which city is known as the Pink City of India?': 'A. Banglore B. Mysore C. Jaipur D. Kochi',
    "Who wrote India's National Anthem?": 'A. Rabindranath Tagore B. Lal Bahadur Shastri C. Chetan Bhagat D. RK Narayan'
}

currWinning = 0
i = 1
for Question, Options in Questions.items():
    print(f'{Fore.YELLOW}Q{i} {Question}{Style.RESET_ALL}')
    print(f"{Fore.CYAN} {Options}{Style.RESET_ALL}")
    winning = random.randint(50000, 150000)
    print('Yow will won Rs', winning,'for this question')
    inputAns = input("Enter your answer(a/b/c/d)\n").lower()
    if('Ganesha' in Options):
        correct_ans = 'd'
    elif('Money' in Options):
        correct_ans = 'a'
    elif('Jaipur' in Options):
        correct_ans = 'c'
    elif('Rabindranath Tagore' in Options):
        correct_ans = 'a'
    
    if(inputAns == correct_ans):
        right_answer_sound.play()
        print(f"{Fore.GREEN} Correct!{Style.RESET_ALL}")
        currWinning += winning
    else:
        wrong_answer_sound.play()
        print(f"{Fore.RED} Incorrect!,Correct answer was {correct_ans}{Style.RESET_ALL}")
        time.sleep(2)
        break
    time.sleep(2)
    i += 1

print("You won Rs", currWinning, 'in this match')
    