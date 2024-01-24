import random
import hangman_words
import hangman_graph
#如果创建了一份list包含很多单词，用import引用
import os
#引入清屏函数，google找的

chosen_word = random.choice(hangman_words.word_list)
#也可以写成from hangman_word import word_list
#chosen_word = random.choice(word_list)，下同


display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
#根据随机的单词长度,生成一个空的列表,用来存储用户猜测的单词

print(hangman_graph.logo)

live = 17
end_game = False
while not end_game:
    guess = input("Guess a letter: \n").lower()
    os.system("cls")
    #每次回答后清屏
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
#把print放在与for loop循环统一登记，就不会出现因为猜的字母中有重复而打印几次的情况
    
    #老师的方法，使用连接功能"".join()把列表用""里的内容连接起来，并转换为字符串
    #print(f"{' '.join(display)}")
    
    if guess in display:
        print(f"You have already guessed {guess} this word!")
        
    if "_" not in display:
        end_game = True
        print("You Win!")  
#设置游戏结束的初始条件为false，当全猜对了，那就转换为true。    
 
    if guess not in chosen_word:
      live -= 1
      print(hangman_graph.stages[live])
      print(f"Wrong guess, you have {live} time(s) left.")
#这个if语句应该跟for loop在同一个运行层次，因为不是判断字母跟猜测是否一致，而是判断用户是否猜对了
      if live == 0:
        end_game = True
        print("You Lose!")
        print("The answer was {chosen_word}")    