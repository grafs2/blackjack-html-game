# Casino Blackjack Simulator

A complete, realistic Blackjack game simulation in Python featuring a human player, dealer, and 3 AI opponents using basic strategy.

## Features

### Game Rules
- **6-deck shoe** (312 cards) with realistic shuffling
- **Standard Las Vegas casino rules**:
  - Dealer stands on soft 17
  - Blackjack pays 3:2
  - Insurance pays 2:1
  - Splitting allowed up to 3 times (4 hands maximum)
  - Doubling down allowed, including after splits
  - Automatic reshuffle at 75% penetration

### Players
- **1 Human Player**: Interactive gameplay with full control
- **3 AI Opponents**: Use optimal basic strategy for decisions
  - Alice, Bob, and Charlie play alongside you
  - Make realistic decisions based on dealer's upcard
  - All decisions are displayed to show AI behavior

### Interface
- **Colorful ASCII art** using ANSI color codes
- **Card symbols**: ♥ ♦ ♣ ♠ with red/white coloring
- **Clear table layout** showing:
  - Dealer's hand and upcard
  - Each player's hands, bets, and bankrolls
  - Current totals with soft/hard indication
  - Split hands labeled clearly
- **Realistic timing** with delays for card dealing

### Gameplay Features
- **Insurance betting** when dealer shows Ace
- **Hand splitting** with automatic hand management
- **Double down** with bet doubling
- **Bankroll tracking** across multiple rounds
- **Blackjack detection** with special payout
- **Push handling** for ties
- **Detailed round summaries** showing wins/losses

## How to Run

### Requirements
- Python 3.6 or higher
- No external dependencies (uses only standard library)

### Running the Game

1. **Navigate to the directory**:
   ```bash
   cd blackjack
   ```

2. **Run the game**:
   ```bash
   python blackjack.py
   ```

3. **Alternative (if executable)**:
   ```bash
   ./blackjack.py
   ```

### On Windows
```cmd
python blackjack.py
```

### On Linux/Mac
```bash
python3 blackjack.py
```

## How to Play

### Starting the Game
1. Enter your name when prompted
2. Each player starts with $1,000 bankroll

### Each Round
1. **Place Bet**: Enter bet amount ($10-$500 or your remaining bankroll)
2. **Receive Cards**: Two cards dealt to each player and dealer
3. **Insurance**: If dealer shows Ace, option to place insurance bet
4. **Play Hand**: Choose actions for each hand:
   - **(h)it**: Take another card
   - **(s)tand**: Keep current hand
   - **(d)ouble**: Double your bet and receive one final card
   - **s(p)lit**: Split pairs into separate hands (if you have matching cards)

5. **Dealer Plays**: Dealer reveals cards and plays by house rules
6. **Settlement**: Winnings/losses calculated and bankrolls updated

### Winning Conditions
- **Blackjack**: Natural 21 (Ace + 10-value card) pays 3:2
- **Beat Dealer**: Higher total than dealer without busting wins 1:1
- **Dealer Busts**: Win if you didn't bust
- **Push**: Same total as dealer returns your bet
- **Bust**: Over 21 loses immediately

## Code Structure

### Object-Oriented Design

```
Card class
  - Represents individual playing cards
  - Handles rank, suit, and value calculation

Deck class
  - 6-deck shoe management
  - Shuffling and card dealing
  - Penetration tracking for reshuffle

Hand class
  - Card collection for each hand
  - Total calculation with Ace handling
  - Blackjack, bust, split detection

Player class
  - Manages bankroll and hands
  - Supports multiple hands (for splits)
  - Insurance betting

BasicStrategy class
  - AI decision-making engine
  - Implements optimal basic strategy
  - Hit/stand/double/split decisions

Game class
  - Main game controller
  - Round management
  - Bet settlement
  - Display and user interaction
```

### Key Files
- **blackjack.py**: Complete game implementation (single file)
- **README.md**: This documentation

## AI Strategy

The computer opponents use **optimal basic strategy**:

### Hard Totals
- Hit on 11 or less
- Hit on 12 against dealer 7-Ace
- Hit on 13-16 against dealer 7-Ace
- Stand on 17+

### Soft Totals
- Hit on soft 17 or less
- Hit on soft 18 against dealer 9-Ace
- Stand on soft 19+

### Doubling
- Double 9 against dealer 3-6
- Double 10 against dealer 2-9
- Always double 11
- Double soft totals based on dealer upcard

### Splitting
- Always split Aces and 8s
- Never split 5s and 10s
- Split other pairs based on dealer upcard

### Insurance
- Never take insurance (basic strategy)

## Example Gameplay

```
🎰  WELCOME TO CASINO BLACKJACK  🎰

Enter your name: John
Starting bankroll: $1000 per player

════════════════════════════════════════════════════════════
                   ROUND 1
════════════════════════════════════════════════════════════

💰  PLACE YOUR BETS

John's bankroll: $1000
Enter your bet (10-500): $50
Alice bets $25 (Bankroll: $975)
Bob bets $30 (Bankroll: $970)
Charlie bets $40 (Bankroll: $960)

Dealing cards...

════════════════════════════════════════════════════════════
                    🎰  TABLE  🎰
════════════════════════════════════════════════════════════

Dealer: [K♠] [??]

Players:
────────────────────────────────────────────────────────────
John ($950): Hand: [A♥] [9♦] = 20 (Bet: $50)
Alice ($975): Hand: [7♣] [8♣] = 15 (Bet: $25)
Bob ($970): Hand: [10♥] [6♠] = 16 (Bet: $30)
Charlie ($960): Hand: [Q♦] [Q♣] = 20 (Bet: $40)

John's Hand: [A♥] [9♦] = 20
Options: (h)it, (s)tand
Your choice: s

... (game continues)
```

## Customization Options

You can easily modify:

1. **Starting bankroll**: Change `1000` in `setup_players()`
2. **Number of decks**: Change `num_decks=6` in `Deck.__init__()`
3. **Bet limits**: Change `10-500` in `place_bets()`
4. **Number of AI players**: Add/remove in `setup_players()`
5. **Shuffle penetration**: Change `0.75` in `Deck.__init__()`
6. **AI strategy**: Modify `BasicStrategy` class methods

## Technical Notes

- **Color support**: Uses ANSI escape codes (works on modern terminals)
- **No external dependencies**: Pure Python 3 standard library
- **Single file**: Entire game in one executable file
- **Clean OOP design**: Easy to extend and modify
- **Type hints**: Modern Python typing for clarity

## Troubleshooting

### Colors not showing
Some older terminals don't support ANSI colors. The game will still work but without colors.

### Input errors
- Enter only numbers for bets
- Use lowercase letters for choices (h, s, d, p)
- Press Enter after each input

### Game crashes
- Ensure Python 3.6+ is installed
- Check that the file has proper line endings for your OS

## License

Free to use and modify for personal or educational purposes.

## Credits

Created as a comprehensive Python programming example demonstrating:
- Object-oriented design
- Game logic and state management
- Terminal UI with colors
- AI implementation
- Probability and strategy

Enjoy the game! 🎰
