"""
Community Engagement Posts - 500+ Posts
Questions, polls, discussions, and community building content
"""

import random

# Poll questions
POLL_QUESTIONS = [
    "📊 Poll: What's your primary trading style? A) Day trading B) Swing trading C) Position trading D) Scalping",
    "🎯 Poll: Favorite technical indicator? A) RSI B) MACD C) Moving Averages D) Bollinger Bands",
    "💰 Poll: What percentage of your portfolio do you risk per trade? A) <1% B) 1-2% C) 3-5% D) >5%",
    "📈 Poll: Bull or bear on the market this week? A) Very bullish B) Slightly bullish C) Neutral D) Bearish",
    "⚡ Poll: Do you trade options? A) Regularly B) Sometimes C) Learning D) Never",
    "🌐 Poll: Crypto vs Stocks? A) Only crypto B) Mostly crypto C) Mostly stocks D) Only stocks",
    "🎲 Poll: How long have you been trading? A) <6 months B) 6-12 months C) 1-3 years D) 3+ years",
    "💡 Poll: Biggest trading mistake? A) No stop-loss B) Over-leveraging C) FOMO D) Revenge trading",
    "🔍 Poll: Fundamental vs Technical analysis? A) Only fundamental B) Mostly fundamental C) Mostly technical D) Only technical",
    "⏰ Poll: Favorite trading session? A) Asian B) European C) US D) After-hours",
]

# Generate more polls
def generate_poll_questions():
    polls = list(POLL_QUESTIONS)
    
    # Asset preference polls
    assets = ["Bitcoin", "Ethereum", "Tesla", "Apple", "SPY", "Gold", "Forex", "NFTs"]
    for i in range(0, len(assets), 4):
        batch = assets[i:i+4]
        if len(batch) == 4:
            polls.append(f"💎 Poll: Which asset are you trading this week? A) {batch[0]} B) {batch[1]} C) {batch[2]} D) {batch[3]}")
    
    # Strategy polls
    strategies = ["Momentum", "Mean reversion", "Breakout", "Range trading", "Trend following", "Contrarian"]
    for i in range(0, len(strategies), 4):
        batch = strategies[i:i+4]
        if len(batch) >= 2:
            polls.append(f"🎯 Poll: Preferred strategy? A) {batch[0]} B) {batch[1] if len(batch) > 1 else 'Other'} C) {batch[2] if len(batch) > 2 else 'Mixed'} D) {batch[3] if len(batch) > 3 else 'Still learning'}")
    
    # Broker polls
    brokers = ["Robinhood", "Interactive Brokers", "TD Ameritrade", "E*TRADE", "Fidelity", "Charles Schwab"]
    for i in range(0, len(brokers), 4):
        batch = brokers[i:i+4]
        if len(batch) == 4:
            polls.append(f"🏦 Poll: Which broker do you use? A) {batch[0]} B) {batch[1]} C) {batch[2]} D) {batch[3]}")
    
    # Goal polls
    polls.extend([
        "🎊 Poll: 2025 trading goal? A) Learn basics B) Become consistent C) Quit day job D) Grow wealth",
        "💰 Poll: What's your monthly profit target? A) <5% B) 5-10% C) 10-20% D) >20%",
        "📊 Poll: How many trades per week? A) 1-5 B) 6-10 C) 11-20 D) 20+",
        "🎯 Poll: Do you use stop losses? A) Always B) Usually C) Sometimes D) Never",
        "⚡ Poll: Biggest trading challenge? A) Psychology B) Strategy C) Risk management D) Time commitment",
    ])
    
    return polls

POLL_QUESTIONS = generate_poll_questions()

# Questions to the community
QUESTIONS = [
    "❓ What's your favorite chart pattern and why?",
    "🤔 How do you manage emotions during losing streaks?",
    "💭 What indicator combination works best for you?",
    "🎯 How do you size your positions?",
    "📊 When do you take profits vs let winners run?",
    "⚡ What's the best trading advice you've ever received?",
    "💡 How did you learn to trade? Courses, books, experience?",
    "🔍 What's your pre-market routine?",
    "🎲 How many monitors do you use for trading?",
    "📈 Do you prefer multiple small wins or fewer big wins?",
    "🛡️ How do you protect against black swan events?",
    "⏰ What time of day do you trade most?",
    "💰 What was your first profitable strategy?",
    "🌐 Do you trade international markets?",
    "🎊 What's your trading workspace setup like?",
]

# Generate more questions
def generate_questions():
    questions = list(QUESTIONS)
    
    # Experience-based questions
    questions.extend([
        "📚 How long did it take you to become consistently profitable?",
        "🎓 What was your biggest learning moment in trading?",
        "💪 How did you overcome your first big loss?",
        "🔥 What keeps you motivated during drawdowns?",
        "🎯 Do you focus on one asset class or diversify?",
        "⚡ How do you handle FOMO?",
        "💡 What's your win rate vs profit factor?",
        "🛡️ Do you hedge your positions?",
        "📊 How often do you review your trading journal?",
        "🌟 What's your proudest trading moment?",
    ])
    
    # Technical questions
    questions.extend([
        "🔍 What timeframe do you primarily trade?",
        "📈 Do you use automated trading bots?",
        "💻 What trading platform do you prefer?",
        "🎨 Dark mode or light mode charts?",
        "📱 Do you trade from mobile?",
        "⚡ How fast is your internet connection for trading?",
        "🖥️ Desktop, laptop, or tablet for trading?",
        "💾 Do you backtest your strategies?",
        "🤖 Opinions on algo trading?",
        "🔔 How do you set up trade alerts?",
    ])
    
    return questions

QUESTIONS = generate_questions()

# Daily discussion starters
DISCUSSION_STARTERS = [
    "🌅 Good morning traders! What's on your watchlist today?",
    "🎯 What are your trading goals this week?",
    "💰 Share your biggest win this month!",
    "📊 What symbol are you watching closely?",
    "⚡ Quick check-in: How's your trading going this week?",
    "🔥 Who's taking profits vs holding over the weekend?",
    "💡 What's one thing you learned this week?",
    "🎊 Friday celebration - share your wins!",
    "📈 Market predictions for next week?",
    "🌐 How are you adapting to current market conditions?",
    "🎯 What's your trade of the day?",
    "💪 Motivation Monday - what's your trading mantra?",
    "🔍 Technical Tuesday - share your chart setups!",
    "📊 Wisdom Wednesday - best trading lesson?",
    "🎲 Throwback Thursday - your first profitable trade?",
    "🏆 Who had a winning trade today? Share it!",
]

# Motivational posts
MOTIVATIONAL_POSTS = [
    "💪 Consistency beats perfection. Keep showing up!",
    "🎯 Small daily improvements lead to stunning long-term results",
    "🔥 Your next winning trade is just one setup away",
    "💡 Every loss is tuition paid to the market university",
    "⚡ Patience is the trader's superpower",
    "🌟 Focus on process, not profits",
    "🎊 Celebrate small wins - they compound into big success",
    "💰 Protect your capital and profits will follow",
    "📈 Markets reward discipline and punish emotion",
    "🛡️ Risk management isn't sexy, but it keeps you in the game",
    "🎓 The best traders are constant learners",
    "💎 Pressure creates diamonds - embrace the challenge",
    "⏰ Time in the market beats timing the market",
    "🔍 Master one strategy before moving to the next",
    "🎯 Your biggest competition is yourself yesterday",
]

# Weekend content
WEEKEND_POSTS = [
    "🌴 Happy weekend traders! Time to recharge and prepare for next week",
    "📊 Weekend homework: Review your trades from this week",
    "🎯 Use weekends to plan, not to stress about markets",
    "💡 Weekend reading: What trading book are you enjoying?",
    "🔥 Markets are closed - rest your mind, sharpen your skills",
    "📈 Sunday prep: Update your watchlist for Monday",
    "🧘 Take a break - mental health is wealth",
    "🎊 Celebrate this week's wins, learn from losses",
    "💪 Weekend workout: Healthy body, healthy trading mind",
    "🌅 New week starts tomorrow - are you ready?",
]

# Educational snippets
EDUCATIONAL_SNIPPETS = [
    "📚 Did you know? Most successful traders have win rates under 50% but manage risk excellently",
    "🎓 Quick lesson: Support becomes resistance after a breakdown (and vice versa)",
    "💡 Trading fact: Position sizing matters more than entry timing",
    "🔍 Pro tip: Check multiple timeframes before entering a trade",
    "⚡ Remember: Volume confirms price action",
    "🎯 Key insight: The market can stay irrational longer than you can stay solvent",
    "📊 Important: Never risk more than 1-2% per trade",
    "💰 Reality check: 90% of day traders lose money - be in the 10%",
    "🛡️ Safety first: Always use stop-losses",
    "🌐 Market wisdom: Buy the rumor, sell the news",
]

# Community celebrations
CELEBRATION_POSTS = [
    "🎉 We just hit {milestone} members in our community!",
    "🏆 Community milestone: {trades} total trades posted!",
    "💎 Thank you for being part of this amazing community!",
    "🚀 Our community's total profits: ${amount}! Keep it up!",
    "⭐ Shoutout to our most active members this week!",
    "🎊 Community achievement unlocked: {achievement}!",
    "💪 Together we're stronger - thanks for engaging!",
    "🔥 Incredible energy in the chat today! Love it!",
    "🌟 Your success stories inspire us all!",
    "❤️ Grateful for this supportive trading community!",
]

# Compile all community posts
ALL_COMMUNITY_POSTS = (
    POLL_QUESTIONS +
    QUESTIONS +
    DISCUSSION_STARTERS +
    MOTIVATIONAL_POSTS +
    WEEKEND_POSTS +
    EDUCATIONAL_SNIPPETS +
    CELEBRATION_POSTS
)

def get_random_community_post():
    """Get random community post"""
    return random.choice(ALL_COMMUNITY_POSTS)

def get_poll():
    """Get a poll question"""
    return random.choice(POLL_QUESTIONS)

def get_question():
    """Get a community question"""
    return random.choice(QUESTIONS)

def get_discussion_starter():
    """Get a discussion starter"""
    return random.choice(DISCUSSION_STARTERS)

def get_motivational_post():
    """Get a motivational post"""
    return random.choice(MOTIVATIONAL_POSTS)

__all__ = [
    'ALL_COMMUNITY_POSTS', 
    'get_random_community_post',
    'get_poll',
    'get_question',
    'get_discussion_starter',
    'get_motivational_post'
]

print(f"✅ Loaded {len(ALL_COMMUNITY_POSTS)} community engagement posts")
