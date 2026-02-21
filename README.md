# 🎰 Casino Blackjack - HTML5 Web Version

A stunning, fully-featured graphical Blackjack game built with HTML5, CSS3, and JavaScript. Play in your browser with beautiful casino-style visuals!

## 🎮 How to Play

### Quick Start
1. **Open the game**: Double-click `blackjack.html` or open it in any modern web browser
2. **Click "Start Game"** to begin
3. **Place your bet** using the colorful chips or enter an amount
4. **Click "Place Bet & Deal"** to start the round
5. **Make your moves**: Hit, Stand, Double, or Split
6. **Watch the AI opponents** play with optimal strategy
7. **See the results** and start a new round!

### No Installation Required
- Works in **any modern browser** (Chrome, Firefox, Safari, Edge)
- **No server needed** - runs completely offline
- **No dependencies** - single HTML file with everything included

## ✨ Features

### 🎨 Beautiful Graphics
- **Casino green felt table** with realistic wood border
- **Animated playing cards** with smooth dealing animations
- **Colorful poker chips** for betting ($10, $25, $50, $100, $500)
- **Gradient backgrounds** and professional styling
- **Responsive design** - works on desktop, tablet, and mobile

### 🎯 Complete Game Mechanics
- **6-deck shoe** with automatic reshuffling at 75% penetration
- **Standard casino rules**:
  - Dealer stands on soft 17
  - Blackjack pays 3:2
  - Insurance available when dealer shows Ace
  - Splitting allowed up to 4 hands
  - Doubling down allowed (including after splits)
- **Real-time deck penetration** tracking
- **Bankroll management** across multiple rounds

### 🤖 Smart AI Opponents
- **3 AI players** (Alice, Bob, Charlie) using optimal basic strategy
- **Visible AI decisions** - watch them hit, stand, double, and split
- **Realistic betting** patterns
- **Strategic play** based on dealer's upcard

### 📊 Game Information Display
- **Round counter** tracks your session
- **Deck penetration** percentage shown
- **Running count** (Hi-Lo card counting system) displayed
  - Green (+) indicates favorable deck for player
  - Red (-) indicates favorable deck for dealer
  - Automatically resets when deck is shuffled
- **True count** (Running Count ÷ Decks Remaining)
  - Normalized count that accounts for remaining deck size
  - More accurate indicator of player advantage
  - Color-coded same as running count
- **Your bankroll** prominently displayed
- **All player bankrolls** visible
- **Bet amounts** and hand values clearly shown

### 🎬 Smooth Animations
- **Card dealing** with slide-in animation
- **Chip selection** with hover effects
- **Shuffle notification** when deck is reset
- **Fade-in messages** for game events
- **Active player highlighting**

### 💡 User-Friendly Interface
- **Clear action buttons** with color coding:
  - 🟢 Green for Hit
  - 🔵 Blue for Stand
  - 🟡 Yellow for Double
  - 🔴 Red for Split
- **Disabled buttons** when actions aren't available
- **Status badges** for Blackjack, Bust, Win, Push
- **Helpful messages** guide you through gameplay
- **Bet input** with chip shortcuts
- **💡 Basic Strategy Suggestions** displayed during your turn:
  - Shows the optimal move based on your hand and dealer's upcard
  - Explains the reasoning behind each suggestion
  - Updates automatically after each card
  - Follows professional basic strategy rules

## 🎲 Gameplay Details

### Betting Phase
1. Use **colorful chips** to quickly add to your bet
2. Or **type any amount** in the bet field ($10-$1000)
3. **Clear Bet** button resets to minimum
4. AI players automatically bet random amounts

### Playing Phase
- **Your turn is highlighted** with a glowing border
- Available actions:
  - **Hit**: Take another card
  - **Stand**: Keep your current total
  - **Double**: Double your bet, take one card, then stand
  - **Split**: Split matching cards into two hands (costs additional bet)
- **Hand values** update in real-time
- **Soft hands** are labeled (when Ace counts as 11)

### AI Turn
- **Watch AI players** make strategic decisions
- **Messages show** what each AI does
- **Realistic timing** between actions

### Dealer Turn
- **Dealer reveals** hidden card
- **Automatic play** following house rules
- **Stand on 17+** (hits soft 17)

### Settlement
- **Detailed results** for each player
- **Win amounts** calculated and displayed
- **Bankrolls updated** automatically
- **Next round** button or change bet option

## 🎯 Visual Features

### Card Design
- **Realistic playing cards** with proper suits (♥ ♦ ♣ ♠)
- **Red cards** (hearts, diamonds) in red color
- **Black cards** (clubs, spades) in black color
- **Card back** with casino-themed design
- **3D shadow effects** for depth

### Table Layout
- **Oval casino table** with green felt texture
- **Wood border** surrounding the table
- **Dashed betting line** for authenticity
- **Dealer position** at top
- **4 player positions** in grid below

### Chip Design
- **5 chip denominations** with distinct colors:
  - $10 - Blue
  - $25 - Green
  - $50 - Red
  - $100 - Black
  - $500 - Purple
- **Hover animations** on chips
- **Dashed circle** decoration for realism

### Color Scheme
- **Dark background** (navy blue gradient)
- **Gold accents** for headers and highlights
- **Green table** for authentic casino feel
- **Colorful status badges** for quick recognition

## 🔧 Technical Details

### Browser Compatibility
- ✅ Chrome/Edge 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Opera 76+

### Technologies Used
- **HTML5** for structure
- **CSS3** for styling:
  - Flexbox and Grid layouts
  - Gradients and shadows
  - Animations and transitions
  - Media queries for responsiveness
- **Vanilla JavaScript** for game logic:
  - Object-oriented design
  - Event-driven architecture
  - DOM manipulation
  - No external libraries!

### Performance
- **Lightweight** - single ~30KB HTML file
- **Fast loading** - no external resources
- **Smooth animations** - CSS-powered
- **Optimized rendering** - efficient DOM updates

## 🃏 Card Counting System

The game includes both **Running Count** and **True Count** trackers that help you understand the composition of the remaining deck:

### How It Works
- **Low cards (2-6)**: +1 to the count
- **Neutral cards (7-9)**: 0 to the count
- **High cards (10, J, Q, K, A)**: -1 to the count

### Running Count vs True Count

#### Running Count
The **Running Count** is the raw total of all cards dealt since the last shuffle:
- Simple cumulative total
- Increases/decreases with each card
- Resets to 0 when deck is shuffled

#### True Count
The **True Count** is the normalized count that accounts for how many decks remain:
```
True Count = Running Count ÷ Decks Remaining
```

**Why True Count Matters:**
- A running count of +6 means different things at different penetration levels
- **Example 1**: Running Count +6 with 5 decks remaining = True Count +1.2 (weak advantage)
- **Example 2**: Running Count +6 with 1.5 decks remaining = True Count +4.0 (strong advantage!)

The True Count gives you a **per-deck** measure of your advantage, making it far more useful for betting decisions.

### What the Counts Mean
- **Positive count** (shown in green): More high cards remaining in deck
  - Favorable for player
  - Better odds for blackjack
  - Consider increasing your bet
- **Negative count** (shown in red): More low cards remaining in deck
  - Favorable for dealer
  - Lower odds for blackjack
  - Consider minimum betting
- **Zero count** (shown in white): Neutral deck

### Using the Counts

#### Betting Strategy Based on True Count
Professional card counters adjust bets using the True Count:
- **True Count ≤ 0**: Bet minimum ($10)
- **True Count +1**: Bet 1-2 units ($10-$20)
- **True Count +2**: Bet 2-4 units ($20-$40)
- **True Count +3**: Bet 4-6 units ($40-$60)
- **True Count +4**: Bet 6-8 units ($60-$80)
- **True Count +5 or higher**: Bet 8-10+ units ($80-$100+)

#### Example Progression
```
Round 5:  Penetration 15%, Running Count +3, True Count +0.6  → Bet $10
Round 12: Penetration 50%, Running Count +8, True Count +2.7  → Bet $30-40
Round 18: Penetration 70%, Running Count +7, True Count +4.7  → Bet $80-100!
```

**Note**: This is for educational purposes. Card counting is a mental skill, and these trackers help you learn how it works!

## 💡 Dual Strategy Suggestion Feature

The game now includes a **split-screen strategy advisor** that shows TWO suggestions side-by-side!

### Two-Column Layout

#### 📚 Left Side: Basic Strategy
- Traditional basic strategy recommendations
- Works regardless of the count
- Perfect for beginners learning the fundamentals
- **ℹ️ Info button** with detailed explanation on hover

#### 🎯 Right Side: True Count Strategy
- **Professional card counting adjustments**
- Shows what an expert counter would do
- Displays the current True Count
- **Highlights when it differs from basic strategy** with a pulsing animation
- **ℹ️ Info button** explaining count-based deviations

### How It Works
- Automatically analyzes your hand, dealer's upcard, AND the true count
- Updates after every card you receive
- Shows reasoning for each suggestion
- **Green highlighting** on True Count strategy when it deviates from basic

### Index Plays (True Count Deviations)

The True Count strategy includes professional "index plays" that adjust based on the count:

#### Standing Adjustments (High Count = Stand More)
- **16 vs 10**: Stand when TC ≥ 0 (basic says hit)
- **15 vs 10**: Stand when TC ≥ +4
- **12 vs 3**: Stand when TC ≥ +2
- **12 vs 2**: Stand when TC ≥ +3
- **13 vs 2**: Stand when TC ≥ -1

#### Doubling Adjustments (High Count = Double More)
- **10 vs 10**: Double when TC ≥ +4 (basic says hit)
- **10 vs Ace**: Double when TC ≥ +4
- **9 vs 2**: Double when TC ≥ +1
- **9 vs 7**: Double when TC ≥ +3
- **8 vs 5/6**: Double when TC ≥ +2

#### Splitting Adjustments (Very High Count)
- **10s vs 5**: Split when TC ≥ +5 (basic says never split 10s!)
- **10s vs 6**: Split when TC ≥ +4
- **9s vs 7**: Don't split when TC < -2

### Example Display

```
┌─────────────────────────────────┬─────────────────────────────────┐
│     📚 BASIC STRATEGY           │   🎯 TRUE COUNT STRATEGY        │
│                                 │        TC: +4.2                 │
├─────────────────────────────────┼─────────────────────────────────┤
│         HIT                     │      DOUBLE ✨ (pulsing)       │
│    Hit vs dealer 10             │  TC +4.2: Double 10 vs 10       │
└─────────────────────────────────┴─────────────────────────────────┘
```

### Interactive Info Tooltips (New!)

Each strategy column now has an **ℹ️ info button** that reveals detailed explanations when you hover over it:

#### Basic Strategy Tooltips Explain:
- **Why Hit**: "You cannot bust" or "Dealer likely to make a hand"
- **Why Stand**: "Pat hand" or "Dealer likely to bust with weak card"
- **Why Double**: "High probability of strong hand" with percentages
- **Why Split**: "Two chances at 21" or "Better than single weak hand"
- **Mathematical reasoning** based on millions of simulated hands
- **Bust probabilities** for dealer's upcard

#### True Count Tooltips Explain:
- **Current True Count** and what it means
- **Whether it's a deviation** from basic strategy
- **Why the count justifies the play**: "More 10s in deck" or "More small cards remain"
- **Index play explanations** like "Most important deviation!"
- **Player edge percentage** from following the count-based play
- **Professional insights** on card counting strategy

#### Example Tooltip Content:

**Basic Strategy (16 vs 10 - Hit):**
```
HIT - Why?
─────────────────
Stiff Hand (16): Dealer shows 10, which is a strong
card. Dealer is likely to make a hand, so you must
try to improve.

Math: Hitting gives you a better chance of winning
than standing with 16.

This is computer-perfect basic strategy based on
millions of simulated hands.
```

**True Count Strategy (16 vs 10 - Stand, TC +2.3):**
```
STAND - Count-Based Play
─────────────────────────
True Count: +2.3

⚠️ Index Play Deviation!
Basic strategy says HIT, but the True Count
justifies STAND instead.

Why Stand?
High count means more 10s remain. Dealer likely to
bust when hitting their 10. You also risk busting
with 16.

This is the most important index play! Stand on
16 vs 10 when TC ≥ 0.

Player Edge: Following this deviation gives you
approximately 1.2% edge over the house!

Professional card counters use these "index plays"
to maximize their advantage.
```

### When Strategies Differ

When the True Count strategy differs from basic strategy:
- The **True Count recommendation pulses** to draw your attention
- The reasoning explains the count-based deviation
- **Hover over the ℹ️ to see WHY** the count justifies the deviation
- This is when the count gives you an edge!

### Learning Tool

This dual-display feature with interactive tooltips helps you:
- **Compare basic vs counting strategy** side-by-side
- **Learn the WHY** - hover over ℹ️ for detailed mathematical explanations
- **Understand probabilities** - tooltips show bust chances and odds
- **Learn index plays** - see exactly when to deviate and why
- **Understand the power of counting** - visualize your edge with percentages
- **Practice like a pro** - train yourself on count-based decisions
- **See the True Count impact** in real-time with full explanations
- **Master the math** - tooltips explain the reasoning behind every play

### When to Follow Which Strategy

- **New to Blackjack?** Follow the left (Basic Strategy)
- **Learning to count?** Watch how the right side differs as count changes
- **Experienced counter?** Follow the right (True Count Strategy)
- **Maximum advantage?** Always follow True Count Strategy when you're counting

You can still make any move you want - these are just expert-level suggestions!

## 🎮 Game Strategy (AI Uses This!)

The AI opponents follow **optimal basic strategy**:

### Hard Totals
- Hit on 11 or less
- Hit on 12 vs dealer 7-Ace
- Hit on 13-16 vs dealer 7-Ace
- Stand on 17+

### Soft Totals
- Hit on soft 17 or less
- Hit on soft 18 vs dealer 9-Ace
- Stand on soft 19+

### Doubling
- Double 9 vs dealer 3-6
- Double 10 vs dealer 2-9
- Always double 11
- Double soft 13-18 vs specific dealer cards

### Splitting
- Always split Aces and 8s
- Never split 5s and 10s
- Other splits depend on dealer upcard

## 📱 Mobile Support

The game is **fully responsive**:
- **Smaller cards** on mobile devices
- **Stacked layout** for narrow screens
- **Touch-friendly** buttons and chips
- **Optimized font sizes** for readability

## 🎨 Customization

Easy to customize! Edit the HTML file to change:

### Colors
```css
/* Find these in the <style> section */
background: linear-gradient(...) /* Background gradient */
.casino-table { background: ... } /* Table color */
.chip-10 { background: ... } /* Chip colors */
```

### Game Rules
```javascript
/* Find these in the <script> section */
createDeck(6) // Number of decks
penetration = 0.75 // When to reshuffle
bankroll: 1000 // Starting money
```

### Bet Limits
```javascript
/* In the placeBet() function */
if (betAmount < 10) // Minimum bet
max="1000" // Maximum bet in HTML
```

## 🎯 Features Compared to Python Version

| Feature | Python CLI | HTML5 Web |
|---------|-----------|-----------|
| Graphics | ASCII Text | Beautiful Cards & Table |
| Colors | ANSI Codes | CSS Gradients & Styling |
| Animations | Time delays | Smooth CSS transitions |
| Platform | Python required | Any browser |
| Portability | Single .py file | Single .html file |
| Mobile | No | Yes (responsive) |
| Accessibility | Terminal only | Visual & interactive |

## 🎲 Tips for Players

1. **Watch BOTH Strategy Suggestions!**
   - **Left (Basic)**: Always mathematically correct
   - **Right (True Count)**: Adjusts for card counting advantage
   - When they differ (pulsing), the count is giving you an edge!
   - **Hover over ℹ️ icons** to see detailed explanations of WHY each play is recommended

2. **Use the Info Tooltips to Learn**
   - **Hover over ℹ️ icons** before making your decision
   - Read WHY each play is recommended
   - Learn the mathematical reasoning and probabilities
   - Understand deck composition effects on strategy
   - See your actual edge percentage when following count plays!

3. **Learn Index Plays**
   - Watch for situations like "16 vs 10" when TC is positive
   - Notice how the True Count side suggests standing more when count is high
   - See aggressive doubles (like 10 vs 10) when TC ≥ +4
   - **Tooltip shows "⚠️ Index Play Deviation!"** when count overrides basic

4. **Bet Sizing Based on True Count**
   - True Count ≤ 0: Minimum bet ($10)
   - True Count +1 to +2: 2-3 units ($20-30)
   - True Count +3 to +4: 4-6 units ($40-60)
   - True Count +5+: Max bet ($100+)

5. **Watch Deck Penetration with Count**
   - Early rounds (low penetration): Follow basic strategy mostly
   - Later rounds (high penetration): True Count deviations become critical
   - At 70%+ penetration with high TC, this is where counters make money!

6. **Pay Attention to Deviations**
   - If True Count suggests splitting 10s, the deck is VERY favorable
   - Standing on 16 vs 10 when TC ≥ 0 is a key index play
   - Doubling 10 vs 10 at TC +4 is a powerful move
   - **Check the tooltip** to see your edge percentage!

7. **Practice Mode**
   - Try following basic strategy (left) for a few rounds
   - Then switch to true count strategy (right)
   - Notice how your results improve with counting!
   - **Read tooltips** to understand each decision deeply

8. **Bankroll Management**
   - Don't bet your whole bankroll at once
   - Scale bets with True Count, not emotion
   - Variance is high even with counting - be prepared

9. **Learning Path**
   - Beginners: Follow left column + read basic tooltips
   - Intermediate: Watch both, notice when they differ, read both tooltips
   - Advanced: Follow right column + understand the math via tooltips

10. **Key Index Plays to Remember**
    - 16 vs 10: Stand at TC ≥ 0 (most important!)
    - 10 vs 10: Double at TC ≥ +4
    - 12 vs 3: Stand at TC ≥ +2
    - 10s vs 6: Split at TC ≥ +4 (rare but powerful!)
    - **Hover ℹ️ during these situations** to see full explanations

11. **Insurance Decision**
    - Basic strategy (left): Never take insurance
    - True Count (right): Take insurance when TC ≥ +3
    - This is one of the most profitable count-based plays!

12. **The Golden Rule**
    - When suggestions differ: The True Count is overriding basic strategy
    - This means the deck composition justifies a different play
    - Following these deviations is where counting earns its edge!
    - **Always check the tooltip** to understand WHY

## 🐛 Troubleshooting

### Game won't load
- Check that you're using a modern browser
- Make sure JavaScript is enabled
- Try opening in a different browser

### Cards not showing
- Ensure Unicode support is enabled
- Some old systems may not display card suits properly

### Slow performance
- Close other browser tabs
- Update your browser to the latest version
- Try a different browser (Chrome recommended)

### Chips not clickable
- Make sure you've clicked "Start Game" first
- Refresh the page if buttons become unresponsive

## 📜 License

Free to use, modify, and distribute for personal or educational purposes.

## 🎉 Enjoy!

Have fun playing Casino Blackjack! Try to beat the house and build your bankroll. Remember, the goal is to get as close to 21 as possible without going over!

**Good luck at the tables! 🎰♠️♥️♦️♣️**
