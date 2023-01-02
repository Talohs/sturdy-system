from modules import deck


money = input("What is your initial bet? ")
play_resp = input("Would you like to play or quit? ")
total = 0

while(play_resp != 'quit'):
    play_hand = {}
    deal_hand = {}

    for num in range(1, 3):
        play_hand[num] = deck.deal_card()
        deal_hand[num] = deck.deal_card()

    print(play_hand.get(1)[0], play_hand.get(2)[0])
    print(deal_hand.get(1)[0], 'Hidden')

    play_pts = play_hand.get(1)[1] + play_hand.get(2)[1]
    deal_pts = deal_hand.get(1)[1] + deal_hand.get(2)[1]
 

    print(f"Your hand has {play_pts} points.")
    print(f"The Dealer hand has {deal_hand.get(1)[1]} points visible.")

    if play_pts > 21 and ((play_hand.get(1)[1] or play_hand.get(2)[1]) == 11):
        play_pts -= 10
    if play_pts == 21:
        print(f"Blackjack! You win {int(money) * 2}")
        total = int(total) + (int(money) * 2)
    if deal_pts == 21:
        print(f"Dealer has scored Blackjack")
        print(deal_hand.get(1)[0], deal_hand.get(2)[0])
        print(f"The dealer has {deal_hand.get(1)[0] + deal_hand.get(2)[0]} points")
        total = int(total) - int(money)
        if total <= 0:
            print("Thanks for playing with us!")
            play_resp = 'quit'
        money = input("What is your new bet? ")
        play_resp = input("Would you like to play or quit? ")
        continue
    if deal_pts == 21 and play_pts == 21:
        print(f"Your hand has {play_pts} points.")
        print(deal_hand.get(1)[0], deal_hand.get(2)[0])
        print(f"The dealer has {deal_hand.get(1)[0] + deal_hand.get(2)[0]} points")
        print(f" You have ${total}")
        money = input("What is your new bet? ")
        play_resp = input("Would you like to play or quit? ")
        continue
    play_resp = input("Would you like to hit, stand or quit? ")
    num = 3
    while(play_resp != 'quit'):
        if play_resp == "hit": 
            play_hand[num] = deck.deal_card()
            for card in play_hand.values():
                print(card[0])
            play_pts += card[1]
            if play_pts > 21 and card[1] == 11:
                    play_pts -= 10
            num += 1
            print(f"Your hand has {play_pts} points.")
            if card[1] == 11 and play_pts > 21:
                play_pts -= 10
            if play_pts > 21:
                print(deal_hand.get(1)[0], deal_hand.get(2)[0])
                money = int(money) - int(money)
                if money == 0:
                    print("Thanks for playing with us!")
                    play_resp = 'quit'
                    break
        elif play_resp == "stand":
            for card in play_hand.values():
                print(card[0])    
            if play_pts > deal_hand.get(1)[1] + deal_hand.get(2)[1]:
                print(f"Your hand has {play_pts} points.")
                print(deal_hand.get(1)[0], deal_hand.get(2)[0])
                print(f"The dealer has {deal_hand.get(1)[1] + deal_hand.get(2)[1]} points")
                print("You win!")
                total = int(total) + (int(money) * 2)
                print(f"You have ${total}")
                money = input("What is your new bet? ")
                play_resp = input("Would you like to play or quit? ")
                break
            elif play_pts == deal_hand.get(1)[1] + deal_hand.get(2)[1]:
                print(f"Your hand has {play_pts} points.")
                print(deal_hand.get(1)[0], deal_hand.get(2)[0])
                print(f"The dealer has {deal_hand.get(1)[1] + deal_hand.get(2)[1]} points")
                total = int(total) + int(money) 
                print(f" You have ${total}")
                money = input("What is your new bet? ")
                play_resp = input("Would you like to play or quit? ")
                break
            else:
                print(f"Your hand has {play_pts} points.")
                print(deal_hand.get(1)[0], deal_hand.get(2)[0])
                print(f"The dealer has {deal_hand.get(1)[0] + deal_hand.get(2)[0]} points")
                total = int(total) - int(money)
                if total <= 0:
                    print("Thanks for playing with us!")
                    play_resp = 'quit'
                money = input("What is your new bet? ")
                play_resp = input("Would you like to play or quit? ")
                break
        play_resp = input("Would you like to hit, stand or quit? ")

print(f"You walk away with ${money}")
