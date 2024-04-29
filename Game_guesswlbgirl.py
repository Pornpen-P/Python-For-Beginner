#pseudo-code
import random

#ตัวแปรที่ระบุสถานะของเกม
score = 0
lives = 3
words = ['jackie','por','ple','bumebim','nan','kaofang','nat','tonmint','pook']

def update_clue(guess,secret_word,clue):
    #guess ไล่ไปทีละคัวอักษรใน secret_word ดูว่ามีตัวไหนบ้างตรงกับที่ทาย
    for i in range(len(secret_word)):
        #ถ้าทายตรงกับตัวไหน ก็อัปเดตตำแหน่งนั้น
        if guess == secret_word[i]:
            clue[i] = guess
    win = ''.join(clue) == secret_word
    return win #ทายจนหมด '?' แล้ว  -> True, ยังเหลือ -> False

#ตราบใดที่ยังมีคำให้ทายอยู่ และ ชีวิตยังเหลือ --> เล่นต่อไป
while (len(words) > 0) and (lives > 0):
    #สุ่มคำจาก words แล้วดึงคำนั้นออกจาก List
    random.shuffle(words)
    secret_word = words.pop()
    clue = list('?'*len(secret_word)) #จำนวนเท่ากับตัวอักษรของ secret_word

    #ตราบใดที่ยังทายคำนี้ไม่เสร็จหรือชีวิตยังไม่หมด
    while True:
        print(clue)
        print('ชีวิตที่เหลือ: ' + str(lives))
        guess = input('ทายตัวอักษรสิจ๊ะ: ')

        #check ว่าตัวอักษรที่ทาย อยู่ใน secret_word หรือไม่?
        if guess in secret_word:
            win = update_clue(guess,secret_word,clue)
            if win:
                print('เย้!! คนนั้นก็คือ: '+secret_word)
                score = score + 1
                print('Score: ' + str(score))
                break #ทายคำนี้ชนะแล้ว
        else: #ที่ guess มา ไม่อยู่ใน secret_word
                    print('ผิด!! โดนฟันหนึ่งฉับ')
                    lives = lives - 1
                    if lives == 0:
                        print('เลือดหมดตัว เจ้าแพ้แล้ว!! คนนั้นก็คือ : ' + secret_word)
                        break #เกมจบแล้ว

print('Final score: ' + str(score))
print('Game end!')
