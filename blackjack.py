class Player():
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.hand = []
    def hit(self,deck):
        self.hand.append(deck.deal_one())
    def bet(self,bet_amount):
        self.bet_amount = bet_amount
        self.balance -= bet_amount
    def win(self):
        self.balance+= self.bet_amount * 2
    def __str__(self):
        return f"{self.name}, your current balance is £{self.balance}"


values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, 
          "Nine":9, "Ten":10, "Jack": 10, "Queen":10, "King":10, "Ace": 11}



class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit



class Deck:
    def __init__(self):
        self.deck = []
        for rank in values:
            self.deck.append(Card("Clubs", rank))
            self.deck.append(Card("Hearts", rank))
            self.deck.append(Card("Spades", rank))
            self.deck.append(Card("Diamonds", rank))
    def shuffle(self):
        random.shuffle(self.deck)
    def deal_one(self):
        return self.deck.pop(0)


import random


class Dealer:
    def __init__(self):
        self.hand = []
    def hit(self,deck):
        self.hand.append(deck.deal_one()) 


def who_won(play_on, player_sum, dealer_sum, player, dealer, bet_amount):
    if player_sum > dealer_sum:
        print(f"Congratulations {player.name}, you win!")
        player.win()
        print(f"You've won £{bet_amount}, you now have £{player.balance}")
    elif dealer_sum > player_sum:
        print("DEALER WINS. Better luck next time!")
        print(f"You lose your bet of £{bet_amount}, you have £{player.balance} left")
        if player.balance == 0:
            print("You got no more cash brokie. Better luck next time!")
            play_on = False

    else:
        if len(player.hand) < len(dealer.hand):
            print(f"Congratulations {player.name}, you win!")
            player.win()
            print(f"You've won £{bet_amount}, you now have £{player.balance}.")
        elif len(dealer.hand) < len(player.hand):
            print("DEALER WINS. Better luck next time!")
            print(f"You lose your bet of £{bet_amount}, you have £{player.balance} left.")
            if player.balance == 0:
                print("You got no more cash brokie. Better luck next time!")
                play_on = False
        else:
            print("It's a tie!")


def dealer_plays(dealer_bust, dealer_turn, player, dealer, bet_amount):
    while dealer_turn:
        dealer_sum = 0
        aces = 0
        print("Dealer has the following cards:")
        cards = ""
        for card in dealer.hand:
            cards +="| " + str(card) + " |"
        print(cards)
        for card in dealer.hand:
            if card.rank == "Ace":
                aces += 1
            else:
                dealer_sum += card.value
        if aces > 0:
            if 21 - dealer_sum >= 11:
                dealer_sum += 11
                aces -= 1
                if 21 - dealer_sum >= aces:
                    dealer_sum += aces
                    aces = 0
        if dealer_sum > 21:
            print("DEALER BUSTS. YOU WIN!")
            dealer_bust = True
            player.win()
            print(f"You've won £{bet_amount}, you now have £{player.balance}")

            dealer_turn = False
            break
        elif dealer_sum >= 17:
            print("Dealer stays.")
            print(f"Dealer has a final total of {dealer_sum}")
            dealer_turn = False
            break
        elif dealer_sum < 17:
            dealer.hit(deck)
            print("Dealer hits.")
            if dealer_sum > 21:
                print("DEALER BUSTS. YOU WIN!")
                dealer_bust = True
                player.win()
                print(f"You've won £{bet_amount}, you now have £{player.balance}")

                dealer_turn = False
                break
            else:
                continue


def equal_sum(player, dealer, bet_amount):
    if len(player.hand) < len(dealer.hand):
        print(f"Congratulations {player.name}, you win!")
        player.win()
        print(f"You've won £{bet_amount}, you now have £{player.balance}.")
    elif len(dealer.hand) < len(player.hand):
        print("DEALER WINS. Better luck next time!")
        print(f"You lose your bet of £{bet_amount}, you have £{player.balance} left.")
        if player.balance == 0:
            print("You got no more cash brokie. Better luck next time!")
    else:
        print("It's a tie!")


def compare_sums(player_sum, dealer_sum, player, dealer, bet_amount):
    if player_sum > dealer_sum:
        print(f"Congratulations {player.name}, you win!")
        player.win()
        print(f"You've won £{bet_amount}, you now have £{player.balance}")
    elif dealer_sum > player_sum:
        print("DEALER WINS. Better luck next time!")
        print(f"You lose your bet of £{bet_amount}, you have £{player.balance} left")
        if player.balance == 0:
            print("You got no more cash brokie. Better luck next time!")
    else:
        equal_sum(player, dealer, bet_amount)


def initialise_player():
    name = input("Welcome! Enter your name: ")

    balance = input("How much (£) do you want to play with: ")
    while balance.isdigit() == False:
        balance = input("Please input a number - How much (£) do you want to play with: ")

    player = Player(name,int(balance))
    
    return player

def play_again():
    choice = input("Would you like to play again (Y/N)? >> ")
    while choice.lower() != "y" and choice.lower() != "n":
        choice = input("Please choose Y or N - Would you like to play again? >> ")
    if choice.lower() == "y":
        return True
    else:
        return False


def game():
    player = initialise_player()

    replay = True
    play_on = True
    while replay and play_on:
        player.hand.clear()
        betting = True
        while betting:
            bet_amount = input("How much (£) do you want to bet this round? >> ")
            while bet_amount.isdigit() == False:
                bet_amount = input("Please input a number - How much (£) do you want to bet this round? >> ")
            if int(bet_amount) > player.balance:
                print(f"You only have £{player.balance}, you can't bet £{int(bet_amount)}.")
                continue
            else:
                player.bet(int(bet_amount))
                break



        dealer = Dealer()
        deck = Deck()
        deck.shuffle()
        player.hit(deck)
        player.hit(deck)

        player_bust = False
        dealer_bust = False

        player_sum = 0
        aces = 0

        for card in player.hand:
                    if card.rank == "Ace":
                        aces +=1
                    else:
                        player_sum+=card.value

        player_turn = True

        while player_turn:
            print("\n")
            print(f"{player.name}, you have the following cards:")

            cards = ""
            for card in player.hand:
                cards +="| " + str(card) + " |"
            print(cards)

            play = input("Hit or Stay? ")
            if play.lower() == "hit":
                player.hit(deck)

                if player.hand[-1].rank == "Ace":
                    aces += 1
                else:
                    player_sum += player.hand[-1].value

                if player_sum > 21:
                    cards = ""
                    for card in player.hand:
                        cards +="| " + str(card) + " |"
                    print(cards)
                    print("BUST - YOU LOSE")
                    player_bust = True
                    print(f"Your final total was {player_sum}")
                    print(f"You lose your bet of £{bet_amount}, you have £{player.balance} left.")
                    if player.balance == 0:
                        print("You got no more cash brokie. Better luck next time!")
                        play_on = False                    

                    player_turn = False
                    break
                elif player_sum + aces>21:
                    cards = ""
                    for card in player.hand:
                        cards +="| " + str(card) + " |"
                    print(cards)
                    print("BUST - YOU LOSE")
                    player_bust = True
                    print(f"Your final total was {player_sum}")
                    print(f"You lose your bet of £{bet_amount}, you have £{player.balance} left.")
                    if player.balance == 0:
                        print("You got no more cash brokie. Better luck next time!")
                        play_on = False

                    player_turn = False
                    break
                else:
                    continue


            elif play.lower() == "stay":
                if aces > 0:
                    if 21 - player_sum < 11:
                        player_sum += aces
                    elif 21 - player_sum >= 11:
                        player_sum +=11
                        aces-=1
                        if 21 - player_sum >= aces:
                            player_sum += aces
                            aces = 0
                        elif 21 - player_sum < aces:
                            player_sum -= 11
                            aces +=1
                            player_sum += aces
                else:
                    pass

            else:
                print("Invalid input - Hit or Stay? ")
                continue
            print(f"Your total is {player_sum}")
            print("\n")
            print("Let's see what the dealer can do!")
            print("\n")
            player_turn = False

        if play_on == False:
            break

        if player_bust == True:
            replay = play_again()
            continue
        else:
            dealer_turn = True

            dealer.hit(deck)
            dealer.hit(deck)

            while dealer_turn:
                dealer_sum = 0
                aces = 0
                print("Dealer has the following cards:")
                cards = ""
                for card in dealer.hand:
                    cards +="| " + str(card) + " |"
                print(cards)
                for card in dealer.hand:
                    if card.rank == "Ace":
                        aces += 1
                    else:
                        dealer_sum += card.value
                if aces > 0:
                    if 21 - dealer_sum >= 11:
                        dealer_sum += 11
                        aces -= 1
                        if 21 - dealer_sum >= aces:
                            dealer_sum += aces
                            aces = 0
                if dealer_sum > 21:
                    print("DEALER BUSTS. YOU WIN!")
                    dealer_bust = True
                    player.win()
                    print(f"You've won £{bet_amount}, you now have £{player.balance}")

                    dealer_turn = False
                    break
                elif dealer_sum >= 17:
                    print("Dealer stays.")
                    print(f"Dealer has a final total of {dealer_sum}")
                    dealer_turn = False
                    break
                elif dealer_sum < 17:
                    dealer.hit(deck)
                    print("Dealer hits.")
                    if dealer_sum > 21:
                        print("DEALER BUSTS. YOU WIN!")
                        dealer_bust = True
                        player.win()
                        print(f"You've won £{bet_amount}, you now have £{player.balance}")

                        dealer_turn = False
                        break
                    else:
                        continue

            if dealer_bust == False and player_bust == False:
                compare_sums(player_sum, dealer_sum, player, dealer, bet_amount)
            else:
                pass

            if player.balance == 0:
                break

            replay = play_again()


class Blackjack():
    def newgame(self):
        game()


first_game = Blackjack()


first_game.newgame()