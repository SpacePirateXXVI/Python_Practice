while True:
    num = input( "Please give me a number, my good lad/lass: ").strip()
    divide = int(num) %  2
    if divide > 0:
        print('  "You have to be odd to be number one" - Dr. Seuss ')
    if int(num) % 4 == 0:
        print (' "When angry count to four; when very angry, swear" - Mark Twain')

    else:
        print(""" "Even if you fall on your face, you're still moving forward." - Victor Kiam """)
