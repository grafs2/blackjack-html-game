#!/usr/bin/env python3
"""
Casino Blackjack Simulator
===========================
A complete Blackjack game with dealer, human player, and 3 AI opponents.
Follows standard Las Vegas casino rules with 6-deck shoe.

To run: python blackjack.py
"""

import random
import time
import sys
from enum import Enum
from typing import List, Optional, Tuple


# ANSI Color codes for terminal output
class Color:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'


class Suit(Enum):
    """Card suits with Unicode symbols"""
    HEARTS = '♥'
    DIAMONDS = '♦'
    CLUBS = '♣'
    SPADES = '♠'


class Card:
    """Represents a single playing card"""

    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, rank: str, suit: Suit):
        self.rank = rank
        self.suit = suit

    def value(self) -> int:
        """Returns the base value of the card (Ace = 11, Face cards = 10)"""
        if self.rank == 'A':
            return 11
        elif self.rank in ['J', 'Q', 'K']:
            return 10
        else:
            return int(self.rank)

    def __str__(self) -> str:
        """ASCII representation of the card"""
        # Color red cards red, black cards white
        color = Color.RED if self.suit in [Suit.HEARTS, Suit.DIAMONDS] else Color.WHITE
        return f"{color}[{self.rank}{self.suit.value}]{Color.RESET}"

    def __repr__(self) -> str:
        return f"{self.rank}{self.suit.value}"


class Deck:
    """6-deck shoe with shuffling and penetration tracking"""

    def __init__(self, num_decks: int = 6):
        self.num_decks = num_decks
        self.cards: List[Card] = []
        self.dealt_cards = 0
        self.total_cards = num_decks * 52
        self.penetration_threshold = int(self.total_cards * 0.75)  # 75% penetration
        self.reset()

    def reset(self):
        """Create and shuffle a fresh shoe"""
        self.cards = []
        for _ in range(self.num_decks):
            for suit in Suit:
                for rank in Card.RANKS:
                    self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)
        self.dealt_cards = 0

    def deal_card(self) -> Card:
        """Deal one card from the shoe"""
        if len(self.cards) == 0:
            raise ValueError("Deck is empty!")
        self.dealt_cards += 1
        return self.cards.pop()

    def needs_shuffle(self) -> bool:
        """Check if we've reached the cut card (75% penetration)"""
        return self.dealt_cards >= self.penetration_threshold

    def shuffle(self):
        """Reshuffle the shoe"""
        print(f"\n{Color.YELLOW}{'=' * 60}")
        print("🔀  Reshuffling the shoe...")
        print(f"{'=' * 60}{Color.RESET}\n")
        time.sleep(1)
        self.reset()


class Hand:
    """Represents a Blackjack hand with cards and betting"""

    def __init__(self, bet: int = 0):
        self.cards: List[Card] = []
        self.bet = bet
        self.doubled = False
        self.split_from = None  # Track if this hand was split
        self.settled = False  # Track if this hand has been paid out

    def add_card(self, card: Card):
        """Add a card to the hand"""
        self.cards.append(card)

    def total(self) -> int:
        """Calculate hand total, handling Aces intelligently"""
        total = sum(card.value() for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == 'A')

        # Convert Aces from 11 to 1 if busting
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total

    def is_soft(self) -> bool:
        """Check if hand is soft (has an Ace counting as 11)"""
        total = sum(card.value() for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == 'A')

        # If we have an Ace and the total with Ace=11 is <= 21, it's soft
        return aces > 0 and total <= 21

    def is_blackjack(self) -> bool:
        """Check if hand is a natural blackjack (21 with 2 cards)"""
        return len(self.cards) == 2 and self.total() == 21

    def is_busted(self) -> bool:
        """Check if hand is over 21"""
        return self.total() > 21

    def can_split(self) -> bool:
        """Check if hand can be split"""
        return len(self.cards) == 2 and self.cards[0].value() == self.cards[1].value()

    def can_double(self) -> bool:
        """Check if hand can be doubled down"""
        return len(self.cards) == 2 and not self.doubled

    def __str__(self) -> str:
        """Display the hand"""
        cards_str = ' '.join(str(card) for card in self.cards)
        total = self.total()
        soft = " (soft)" if self.is_soft() else ""
        return f"{cards_str} = {total}{soft}"


class Player:
    """Represents a player (human or AI)"""

    def __init__(self, name: str, bankroll: int, is_human: bool = False):
        self.name = name
        self.bankroll = bankroll
        self.is_human = is_human
        self.hands: List[Hand] = []
        self.current_hand_index = 0
        self.insured = False
        self.insurance_bet = 0

    def place_bet(self, amount: int) -> bool:
        """Place initial bet for the round"""
        if amount > self.bankroll:
            return False
        self.hands = [Hand(bet=amount)]
        self.current_hand_index = 0
        self.insured = False
        self.insurance_bet = 0
        return True

    def add_hand(self, hand: Hand):
        """Add a new hand (from splitting)"""
        self.hands.append(hand)

    def get_current_hand(self) -> Optional[Hand]:
        """Get the hand currently being played"""
        if self.current_hand_index < len(self.hands):
            return self.hands[self.current_hand_index]
        return None

    def next_hand(self):
        """Move to the next hand"""
        self.current_hand_index += 1

    def has_more_hands(self) -> bool:
        """Check if player has more hands to play"""
        return self.current_hand_index < len(self.hands)


class BasicStrategy:
    """AI decision-making using basic Blackjack strategy"""

    @staticmethod
    def should_hit(hand: Hand, dealer_upcard: Card) -> bool:
        """Determine if AI should hit based on basic strategy"""
        player_total = hand.total()
        dealer_value = dealer_upcard.value() if dealer_upcard.rank != 'A' else 11
        is_soft = hand.is_soft()

        # Can't hit on 21
        if player_total == 21:
            return False

        # Hard totals
        if not is_soft:
            if player_total <= 11:
                return True
            if player_total == 12:
                return dealer_value in [2, 3, 7, 8, 9, 10, 11]
            if player_total >= 13 and player_total <= 16:
                return dealer_value >= 7
            return False  # Stand on 17+

        # Soft totals
        else:
            if player_total <= 17:
                return True
            if player_total == 18:
                return dealer_value >= 9
            return False  # Stand on soft 19+

    @staticmethod
    def should_double(hand: Hand, dealer_upcard: Card) -> bool:
        """Determine if AI should double down"""
        if not hand.can_double():
            return False

        player_total = hand.total()
        dealer_value = dealer_upcard.value() if dealer_upcard.rank != 'A' else 11
        is_soft = hand.is_soft()

        # Hard totals
        if not is_soft:
            if player_total == 9:
                return dealer_value in [3, 4, 5, 6]
            if player_total == 10:
                return dealer_value <= 9
            if player_total == 11:
                return True
            return False

        # Soft totals
        else:
            if player_total in [13, 14]:
                return dealer_value in [5, 6]
            if player_total in [15, 16]:
                return dealer_value in [4, 5, 6]
            if player_total in [17, 18]:
                return dealer_value in [3, 4, 5, 6]
            return False

    @staticmethod
    def should_split(hand: Hand, dealer_upcard: Card, num_splits: int) -> bool:
        """Determine if AI should split"""
        if not hand.can_split() or num_splits >= 3:
            return False

        card_value = hand.cards[0].value()
        card_rank = hand.cards[0].rank
        dealer_value = dealer_upcard.value() if dealer_upcard.rank != 'A' else 11

        # Always split Aces and 8s
        if card_rank in ['A', '8']:
            return True

        # Never split 5s and 10s
        if card_rank == '5' or card_value == 10:
            return False

        # Split 2s, 3s, 7s against dealer 2-7
        if card_rank in ['2', '3', '7']:
            return dealer_value <= 7

        # Split 4s against dealer 5-6
        if card_rank == '4':
            return dealer_value in [5, 6]

        # Split 6s against dealer 2-6
        if card_rank == '6':
            return dealer_value <= 6

        # Split 9s against dealer 2-9 except 7
        if card_rank == '9':
            return dealer_value <= 9 and dealer_value != 7

        return False

    @staticmethod
    def should_take_insurance(hand: Hand) -> bool:
        """Determine if AI should take insurance (basic strategy: never)"""
        # Basic strategy says never take insurance unless counting cards
        return False


class Game:
    """Main Blackjack game controller"""

    def __init__(self):
        self.deck = Deck(num_decks=6)
        self.dealer = Player("Dealer", 1000000, is_human=False)
        self.players: List[Player] = []
        self.round_number = 0

    def setup_players(self):
        """Initialize players"""
        print(f"\n{Color.CYAN}{Color.BOLD}{'=' * 60}")
        print("🎰  WELCOME TO CASINO BLACKJACK  🎰")
        print(f"{'=' * 60}{Color.RESET}\n")
        time.sleep(0.5)

        # Human player
        print("Enter your name: ", end='')
        name = input().strip() or "Player"
        self.players.append(Player(name, 1000, is_human=True))

        # 3 AI players
        self.players.append(Player("Alice", 1000, is_human=False))
        self.players.append(Player("Bob", 1000, is_human=False))
        self.players.append(Player("Charlie", 1000, is_human=False))

        print(f"\n{Color.GREEN}Starting bankroll: $1000 per player{Color.RESET}")
        time.sleep(1)

    def place_bets(self):
        """Collect bets from all players"""
        print(f"\n{Color.YELLOW}{'─' * 60}")
        print("💰  PLACE YOUR BETS")
        print(f"{'─' * 60}{Color.RESET}\n")

        active_players = []

        for player in self.players:
            if player.bankroll <= 0:
                print(f"{Color.RED}{player.name} is out of money!{Color.RESET}")
                continue

            if player.is_human:
                while True:
                    print(f"{player.name}'s bankroll: ${player.bankroll}")
                    try:
                        bet = int(input(f"Enter your bet (10-{min(500, player.bankroll)}): $"))
                        if 10 <= bet <= min(500, player.bankroll):
                            if player.place_bet(bet):
                                player.bankroll -= bet
                                active_players.append(player)
                                break
                        print(f"{Color.RED}Invalid bet amount!{Color.RESET}")
                    except ValueError:
                        print(f"{Color.RED}Please enter a number!{Color.RESET}")
            else:
                # AI bets 10-50
                bet = random.randint(10, min(50, player.bankroll))
                player.place_bet(bet)
                player.bankroll -= bet
                print(f"{player.name} bets ${bet} (Bankroll: ${player.bankroll})")
                active_players.append(player)
                time.sleep(0.3)

        return active_players

    def deal_initial_cards(self, active_players: List[Player]):
        """Deal two cards to each player and dealer"""
        print(f"\n{Color.CYAN}Dealing cards...{Color.RESET}\n")
        time.sleep(0.5)

        # First card to each player
        for player in active_players:
            player.hands[0].add_card(self.deck.deal_card())
        self.dealer.hands = [Hand()]
        self.dealer.hands[0].add_card(self.deck.deal_card())

        time.sleep(0.3)

        # Second card to each player
        for player in active_players:
            player.hands[0].add_card(self.deck.deal_card())
        self.dealer.hands[0].add_card(self.deck.deal_card())

        time.sleep(0.3)

    def display_table(self, active_players: List[Player], hide_dealer_card: bool = True):
        """Display the current state of the table"""
        print(f"\n{Color.BOLD}{'═' * 60}")
        print("                    🎰  TABLE  🎰")
        print(f"{'═' * 60}{Color.RESET}\n")

        # Show dealer
        dealer_hand = self.dealer.hands[0]
        if hide_dealer_card and len(dealer_hand.cards) > 0:
            print(f"{Color.BOLD}Dealer:{Color.RESET} {dealer_hand.cards[0]} [??]")
        else:
            print(f"{Color.BOLD}Dealer:{Color.RESET} {dealer_hand}")

        print(f"\n{Color.BOLD}Players:{Color.RESET}")
        print("─" * 60)

        # Show players
        for player in active_players:
            status_parts = []
            for i, hand in enumerate(player.hands):
                hand_str = str(hand)
                bet_str = f"${hand.bet}"
                if hand.doubled:
                    bet_str += " (DOUBLED)"
                if len(player.hands) > 1:
                    hand_label = f"Hand {i+1}"
                else:
                    hand_label = "Hand"

                if hand.is_busted():
                    status_parts.append(f"{hand_label}: {hand_str} {Color.RED}BUST{Color.RESET} (Bet: {bet_str})")
                elif hand.is_blackjack():
                    status_parts.append(f"{hand_label}: {hand_str} {Color.GREEN}BLACKJACK!{Color.RESET} (Bet: {bet_str})")
                else:
                    status_parts.append(f"{hand_label}: {hand_str} (Bet: {bet_str})")

            player_display = f"{Color.BOLD}{player.name}{Color.RESET} (${player.bankroll}): "
            player_display += " | ".join(status_parts)

            if player.insured:
                player_display += f" {Color.YELLOW}[INSURED ${player.insurance_bet}]{Color.RESET}"

            print(player_display)

        print()

    def offer_insurance(self, active_players: List[Player]):
        """Offer insurance if dealer shows Ace"""
        dealer_upcard = self.dealer.hands[0].cards[0]
        if dealer_upcard.rank != 'A':
            return

        print(f"\n{Color.YELLOW}Dealer shows Ace! Insurance available.{Color.RESET}\n")
        time.sleep(0.5)

        for player in active_players:
            hand = player.hands[0]
            max_insurance = hand.bet // 2

            if player.is_human:
                choice = input(f"{player.name}, take insurance? (y/n): ").lower()
                if choice == 'y':
                    if player.bankroll >= max_insurance:
                        player.insured = True
                        player.insurance_bet = max_insurance
                        player.bankroll -= max_insurance
                        print(f"{Color.GREEN}Insurance placed: ${max_insurance}{Color.RESET}")
                    else:
                        print(f"{Color.RED}Not enough money for insurance!{Color.RESET}")
            else:
                # AI uses basic strategy (never take insurance)
                if BasicStrategy.should_take_insurance(hand):
                    player.insured = True
                    player.insurance_bet = max_insurance
                    player.bankroll -= max_insurance
                    print(f"{player.name} takes insurance: ${max_insurance}")
                else:
                    print(f"{player.name} declines insurance")
                time.sleep(0.3)

    def check_dealer_blackjack(self, active_players: List[Player]) -> bool:
        """Check if dealer has blackjack"""
        if self.dealer.hands[0].is_blackjack():
            print(f"\n{Color.RED}{Color.BOLD}Dealer has BLACKJACK!{Color.RESET}\n")
            self.display_table(active_players, hide_dealer_card=False)

            # Pay insurance bets
            for player in active_players:
                if player.insured:
                    winnings = player.insurance_bet * 3  # 2:1 payout plus original bet
                    player.bankroll += winnings
                    print(f"{Color.GREEN}{player.name} insurance pays ${player.insurance_bet * 2}{Color.RESET}")

            time.sleep(1)
            return True
        else:
            # Collect insurance bets
            for player in active_players:
                if player.insured:
                    print(f"{Color.RED}{player.name} loses insurance bet ${player.insurance_bet}{Color.RESET}")
            return False

    def play_player_hand(self, player: Player, hand: Hand, dealer_upcard: Card, hand_index: int = 0, num_splits: int = 0):
        """Play a single hand for a player"""
        if hand.is_blackjack():
            return  # Blackjack stands automatically

        while not hand.is_busted() and hand.total() < 21:
            # Display current state
            self.display_table([player], hide_dealer_card=True)

            hand_label = f"Hand {hand_index + 1}" if len(player.hands) > 1 else "Hand"
            print(f"\n{Color.BOLD}{player.name}'s {hand_label}: {hand}{Color.RESET}")

            if player.is_human:
                # Human player decision
                options = ['(h)it', '(s)tand']

                if hand.can_double() and player.bankroll >= hand.bet:
                    options.append('(d)ouble')

                if hand.can_split() and num_splits < 3 and player.bankroll >= hand.bet:
                    options.append('s(p)lit')

                print(f"Options: {', '.join(options)}")
                choice = input("Your choice: ").lower()

                if choice == 'h':
                    hand.add_card(self.deck.deal_card())
                    print(f"You drew {hand.cards[-1]}")
                    time.sleep(0.5)

                elif choice == 's':
                    print(f"{Color.GREEN}You stand on {hand.total()}{Color.RESET}")
                    time.sleep(0.5)
                    break

                elif choice == 'd' and hand.can_double() and player.bankroll >= hand.bet:
                    player.bankroll -= hand.bet
                    hand.bet *= 2
                    hand.doubled = True
                    hand.add_card(self.deck.deal_card())
                    print(f"{Color.YELLOW}Doubled down! Drew {hand.cards[-1]}{Color.RESET}")
                    time.sleep(0.5)
                    break

                elif choice == 'p' and hand.can_split() and num_splits < 3 and player.bankroll >= hand.bet:
                    # Split the hand
                    player.bankroll -= hand.bet
                    new_hand = Hand(bet=hand.bet)
                    new_hand.add_card(hand.cards.pop())
                    hand.add_card(self.deck.deal_card())
                    new_hand.add_card(self.deck.deal_card())
                    player.add_hand(new_hand)
                    print(f"{Color.YELLOW}Hand split!{Color.RESET}")
                    time.sleep(0.5)
                    # Continue playing current hand

                else:
                    print(f"{Color.RED}Invalid choice!{Color.RESET}")
                    time.sleep(0.5)

            else:
                # AI player decision
                time.sleep(0.8)

                # Check split first
                if BasicStrategy.should_split(hand, dealer_upcard, num_splits) and player.bankroll >= hand.bet:
                    player.bankroll -= hand.bet
                    new_hand = Hand(bet=hand.bet)
                    new_hand.add_card(hand.cards.pop())
                    hand.add_card(self.deck.deal_card())
                    new_hand.add_card(self.deck.deal_card())
                    player.add_hand(new_hand)
                    print(f"{Color.YELLOW}{player.name} splits{Color.RESET}")
                    time.sleep(0.5)
                    continue

                # Check double
                elif BasicStrategy.should_double(hand, dealer_upcard) and player.bankroll >= hand.bet:
                    player.bankroll -= hand.bet
                    hand.bet *= 2
                    hand.doubled = True
                    hand.add_card(self.deck.deal_card())
                    print(f"{Color.YELLOW}{player.name} doubles down and draws {hand.cards[-1]}{Color.RESET}")
                    time.sleep(0.5)
                    break

                # Check hit
                elif BasicStrategy.should_hit(hand, dealer_upcard):
                    hand.add_card(self.deck.deal_card())
                    print(f"{player.name} hits and draws {hand.cards[-1]}")
                    time.sleep(0.5)

                # Otherwise stand
                else:
                    print(f"{Color.GREEN}{player.name} stands on {hand.total()}{Color.RESET}")
                    time.sleep(0.5)
                    break

        if hand.is_busted():
            print(f"{Color.RED}{player.name} busts with {hand.total()}!{Color.RESET}")
            time.sleep(0.5)

    def play_dealer(self):
        """Play the dealer's hand"""
        print(f"\n{Color.CYAN}{Color.BOLD}Dealer's turn{Color.RESET}")
        time.sleep(1)

        dealer_hand = self.dealer.hands[0]
        print(f"Dealer reveals: {dealer_hand}")
        time.sleep(1)

        # Dealer hits on soft 17 or less, stands on hard 17+
        while dealer_hand.total() < 17 or (dealer_hand.total() == 17 and dealer_hand.is_soft()):
            card = self.deck.deal_card()
            dealer_hand.add_card(card)
            print(f"Dealer hits: {card}")
            print(f"Dealer's hand: {dealer_hand}")
            time.sleep(1)

        if dealer_hand.is_busted():
            print(f"{Color.RED}Dealer busts with {dealer_hand.total()}!{Color.RESET}")
        else:
            print(f"{Color.GREEN}Dealer stands on {dealer_hand.total()}{Color.RESET}")

        time.sleep(1)

    def settle_bets(self, active_players: List[Player]):
        """Determine winners and pay out bets"""
        print(f"\n{Color.CYAN}{Color.BOLD}{'═' * 60}")
        print("                💰  SETTLING BETS  💰")
        print(f"{'═' * 60}{Color.RESET}\n")

        dealer_hand = self.dealer.hands[0]
        dealer_total = dealer_hand.total()
        dealer_busted = dealer_hand.is_busted()
        dealer_blackjack = dealer_hand.is_blackjack()

        for player in active_players:
            print(f"\n{Color.BOLD}{player.name}:{Color.RESET}")

            for i, hand in enumerate(player.hands):
                hand_label = f"Hand {i+1}" if len(player.hands) > 1 else "Hand"
                player_total = hand.total()
                player_busted = hand.is_busted()
                player_blackjack = hand.is_blackjack()

                if player_busted:
                    print(f"  {hand_label}: {Color.RED}BUST - Lost ${hand.bet}{Color.RESET}")

                elif player_blackjack and not dealer_blackjack:
                    # Blackjack pays 3:2
                    winnings = int(hand.bet * 2.5)
                    player.bankroll += winnings
                    profit = winnings - hand.bet
                    print(f"  {hand_label}: {Color.GREEN}BLACKJACK! Won ${profit} (paid {winnings}){Color.RESET}")

                elif dealer_busted and not player_busted:
                    winnings = hand.bet * 2
                    player.bankroll += winnings
                    print(f"  {hand_label}: {Color.GREEN}Dealer busts - Won ${hand.bet}{Color.RESET}")

                elif player_blackjack and dealer_blackjack:
                    player.bankroll += hand.bet
                    print(f"  {hand_label}: {Color.YELLOW}Push (both blackjack) - Bet returned{Color.RESET}")

                elif player_total > dealer_total:
                    winnings = hand.bet * 2
                    player.bankroll += winnings
                    print(f"  {hand_label}: {Color.GREEN}Won ${hand.bet} ({player_total} vs {dealer_total}){Color.RESET}")

                elif player_total < dealer_total:
                    print(f"  {hand_label}: {Color.RED}Lost ${hand.bet} ({player_total} vs {dealer_total}){Color.RESET}")

                else:
                    player.bankroll += hand.bet
                    print(f"  {hand_label}: {Color.YELLOW}Push ({player_total}) - Bet returned{Color.RESET}")

            print(f"  New bankroll: ${player.bankroll}")
            time.sleep(0.5)

    def play_round(self):
        """Play one complete round of Blackjack"""
        self.round_number += 1

        # Check if shuffle needed
        if self.deck.needs_shuffle():
            self.deck.shuffle()

        print(f"\n{Color.MAGENTA}{Color.BOLD}{'═' * 60}")
        print(f"                   ROUND {self.round_number}")
        print(f"{'═' * 60}{Color.RESET}")

        # Place bets
        active_players = self.place_bets()

        if not active_players:
            print(f"{Color.RED}No active players!{Color.RESET}")
            return False

        # Deal initial cards
        self.deal_initial_cards(active_players)
        self.display_table(active_players, hide_dealer_card=True)

        # Offer insurance
        self.offer_insurance(active_players)

        # Check for dealer blackjack
        if self.check_dealer_blackjack(active_players):
            # Settle only blackjack vs blackjack pushes
            for player in active_players:
                for hand in player.hands:
                    if hand.is_blackjack():
                        player.bankroll += hand.bet  # Push
                        print(f"{Color.YELLOW}{player.name} pushes with blackjack{Color.RESET}")
            time.sleep(1)
            return True

        # Players play their hands
        for player in active_players:
            if player.hands[0].is_blackjack():
                print(f"\n{Color.GREEN}{player.name} has BLACKJACK!{Color.RESET}")
                time.sleep(1)
                continue

            # Play all hands (including splits)
            original_hand_count = len(player.hands)
            for i in range(len(player.hands)):
                num_splits = len(player.hands) - original_hand_count
                dealer_upcard = self.dealer.hands[0].cards[0]
                self.play_player_hand(player, player.hands[i], dealer_upcard, i, num_splits)

        # Check if all players busted
        all_busted = all(
            all(hand.is_busted() for hand in player.hands)
            for player in active_players
        )

        # Dealer plays if anyone is still in
        if not all_busted:
            self.play_dealer()
        else:
            print(f"\n{Color.RED}All players busted! Dealer wins.{Color.RESET}")
            time.sleep(1)

        # Show final table
        self.display_table(active_players, hide_dealer_card=False)

        # Settle bets
        self.settle_bets(active_players)

        return True

    def run(self):
        """Main game loop"""
        self.setup_players()

        while True:
            # Check if human player can continue
            human_player = self.players[0]
            if human_player.bankroll <= 0:
                print(f"\n{Color.RED}You're out of money! Game over.{Color.RESET}")
                break

            # Play round
            if not self.play_round():
                break

            # Ask to continue
            print(f"\n{Color.CYAN}Continue playing? (y/n): {Color.RESET}", end='')
            choice = input().lower()
            if choice != 'y':
                break

        # Final summary
        print(f"\n{Color.MAGENTA}{Color.BOLD}{'═' * 60}")
        print("                  FINAL STANDINGS")
        print(f"{'═' * 60}{Color.RESET}\n")

        for player in self.players:
            profit = player.bankroll - 1000
            color = Color.GREEN if profit >= 0 else Color.RED
            sign = "+" if profit >= 0 else ""
            print(f"{player.name}: ${player.bankroll} ({color}{sign}${profit}{Color.RESET})")

        print(f"\n{Color.CYAN}Thanks for playing! 🎰{Color.RESET}\n")


def main():
    """Entry point for the game"""
    try:
        game = Game()
        game.run()
    except KeyboardInterrupt:
        print(f"\n\n{Color.YELLOW}Game interrupted. Thanks for playing!{Color.RESET}\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
