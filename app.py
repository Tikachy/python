secert_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess= int(input('Guess: '))
    guess_count +=1
    if guess==secert_number:
        print("u win")
        # break 
else:
    print("sorry u failed")