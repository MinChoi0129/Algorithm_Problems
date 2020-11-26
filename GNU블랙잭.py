from random import shuffle
from cs1graphics import Canvas, Text, Image

img_path = "./images/"
suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
face_names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
bj_board = Canvas(600, 400, 'dark green', 'Blackjack')


class Card:
    pass


def create_deck():
    deck = []
    for suit in suit_names:
        for i in range(len(face_names)):
            card = Card()
            card.suit = suit
            card.face = face_names[i]
            card.value = value[i]
            card.image = Image(img_path + suit + "_" + face_names[i] + ".png")
            card.hidden = False
            deck.append(card)
    shuffle(deck)
    return deck


def hand_value(hand):
    sum_of_values = 0
    for card in hand:
        sum_of_values += card.value
    return sum_of_values


def card_string(card):
    return card.face + " of " + card.suit


def ask_yesno(prompt):
    ans = ""
    while True:
        ans = input(prompt)
        if ans not in ['y', 'Y', 'n', 'N']:
            print("I beg your pardon!")
        else:
            break
    return True if ans in ['y', 'Y'] else False


def draw_card(dealer, player):
    bj_board.clear()
    dealer_score = Text("The dealer's Total : " + str(hand_value(dealer)), 20)
    player_score = Text("Your Total : " + str(hand_value(player)), 20)
    dealer_score.setFontColor("white")
    player_score.setFontColor("white")
    dealer_score.moveTo(450, 100)
    player_score.moveTo(450, 300)

    x0, y0 = 100, 100  # for dealer
    x1, y1 = 100, 300  # for player
    dx_dealer = 0
    dx_player = 0

    if dealer[0].hidden:  # 게임 안 끝남(내 점수만 표시)
        for card in dealer:
            if card.hidden:
                back_img = Image(img_path + "Back.png")
                back_img.moveTo(x0 + dx_dealer, y0)
                bj_board.add(back_img)
                dx_dealer += 20
            else:
                front_img = card.image
                front_img.moveTo(x0 + dx_dealer, y0)
                bj_board.add(front_img)
                dx_dealer += 20

        for card in player:
            front_img = card.image
            front_img.moveTo(x1 + dx_player, y1)
            bj_board.add(front_img)
            dx_player += 20

        bj_board.add(player_score)
    else:  # 게임 끝남(두 사람 점수 모두 표시)
        for card in dealer:
            if card.hidden:
                back_img = Image(img_path + "Back.png")
                back_img.moveTo(x0 + dx_dealer, y0)
                bj_board.add(back_img)
                dx_dealer += 20
            else:
                front_img = card.image
                front_img.moveTo(x0 + dx_dealer, y0)
                bj_board.add(front_img)
                dx_dealer += 20

        for card in player:
            front_img = card.image
            front_img.moveTo(x1 + dx_player, y1)
            bj_board.add(front_img)
            dx_player += 20

        bj_board.add(dealer_score)
        bj_board.add(player_score)


def main():
    deck = []

    while True:
        print("Welcome to Blackjack World!\n")
        if len(deck) < 12:
            deck = create_deck()

        # create two hands of dealer and player
        dealer = []
        player = []

        # initial two dealings
        card = deck.pop()
        print("You are dealt " + card_string(card))
        player.append(card)

        card = deck.pop()
        print("Dealer is dealt a hidden card\n")
        card.hidden = True
        dealer.append(card)

        card = deck.pop()
        print("You are dealt " + card_string(card))
        player.append(card)

        card = deck.pop()
        print("Dealer is dealt " + card_string(card) + "\n")
        dealer.append(card)

        print("Your total is", hand_value(player), "\n")
        draw_card(dealer, player)

        # player's turn to draw cards
        while hand_value(player) < 21 and ask_yesno("Would you like another card? (y/n) "):
            # draw a card for the player
            card = deck.pop()
            print("You are dealt " + card_string(card))
            player.append(card)
            print("Your total is", hand_value(player), "\n")

            draw_card(dealer, player)
        # if the player's score is over 21, the player loses immediately.
        if hand_value(player) > 21:
            print("You went over 21! You lost.")
            dealer[0].hidden = False
            draw_card(dealer, player)
        else:
            # draw cards for the dealer while the dealer's score is less than 17
            print("The dealer's hidden card was " + card_string(dealer[0]))
            while hand_value(dealer) < 17:
                card = deck.pop()
                print("Dealer is dealt " + card_string(card))
                dealer.append(card)
                print("The dealer's total is", hand_value(dealer), "\n")

            dealer[0].hidden = False
            draw_card(dealer, player)
            # summary
            player_total = hand_value(player)
            dealer_total = hand_value(dealer)
            print("Your total is", player_total)
            print("The dealer's total is", dealer_total)

            if dealer_total > 21:
                print("The dealer went over 21! You win!")
            else:
                if player_total > dealer_total:
                    print("You win!")
                elif player_total < dealer_total:
                    print("You lost!")
                else:
                    print("You have a tie!")

        if not ask_yesno("Play another round? (y/n) "):
            bj_board.close()
            break

main()