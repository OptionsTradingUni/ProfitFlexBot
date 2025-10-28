"""
Success Stories - 500+ Trader Success Stories
Inspiring stories from the trading community
"""

import random

# Success story templates
SUCCESS_TEMPLATES = [
    "🎉 Trader turned ${start_amount} into ${end_amount} in {timeframe} trading {asset_class}!",
    "💰 From ${start_amount} to ${end_amount} - {name}'s {strategy} strategy paying off!",
    "🚀 {name} just hit ${milestone} in total profits - started with only ${start_amount}!",
    "📈 ${gain} profit today trading {symbol} - {name}'s best day ever!",
    "🎯 {name} achieved {percent}% returns this {timeframe} - consistency is key!",
    "💎 Held {symbol} from ${entry} to ${exit} - patience = profits!",
    "🔥 {name}'s {timeframe} streak continues - {wins} winning trades in a row!",
    "⚡ Quick ${profit} scalping {symbol} - in and out in {minutes} minutes!",
    "🏆 {name} quit their job to trade full-time - now making ${monthly}/month!",
    "💪 From losing ${loss} to making ${profit} - {name}'s comeback story!",
]

# Detailed success stories
DETAILED_STORIES = [
    """💎 DIAMOND HANDS PAID OFF
{name} held {symbol} through {percent}% drawdown and was rewarded with {gain}% total gain. 
Entry: ${entry} | Exit: ${exit} | Profit: ${profit}
"The key was conviction in my analysis and risk management" - {name}""",
    
    """🎯 PERFECT TIMING
{name} caught the exact bottom on {symbol} using {indicator} divergence.
{timeframe} trade netted ${profit} ({percent}% return)
"Patience and waiting for the perfect setup always wins" - {name}""",
    
    """🚀 BREAKOUT MASTER
{name} identified {symbol} breakout pattern early and rode it to ${target}
Entry: ${entry} | Current: ${current} | Unrealized P/L: ${profit}
"Technical analysis gave me the confidence to size up" - {name}""",
    
    """📊 CONSISTENT WINNER
{name} posted {wins} wins out of {total} trades this month ({percent}% win rate)
Average win: ${avg_win} | Average loss: ${avg_loss} | Net: ${net_profit}
"Following my rules religiously - no exceptions" - {name}""",
    
    """💰 LIFE CHANGING TRADE
{name}'s ${start_amount} position in {symbol} now worth ${end_amount}
Held through volatility for {months} months - life-changing profits!
"This trade paid off my student loans" - {name}""",
    
    """🎓 FROM STUDENT TO PRO
{name} started learning to trade {years} years ago with ${start_amount}
Now managing ${portfolio_size} portfolio with {percent}% annual returns
"Education and discipline made all the difference" - {name}""",
    
    """⚡ SCALPER EXTRAORDINAIRE
{name} made {trades} trades today, {wins} winners = ${total_profit}
Hit rate: {percent}% | Average profit per trade: ${avg_profit}
"Small consistent wins compound into big gains" - {name}""",
    
    """📈 TREND FOLLOWER SUCCESS
{name} rode {symbol} trend from ${start} to ${end} over {timeframe}
Never tried to pick the top - let the trend run its course
Profit: ${profit} ({percent}% gain) - "{quote}" """,
    
    """🔥 OPTIONS MASTER
{name} turned ${premium} options premium into ${profit} on {symbol} calls
Strike: ${strike} | Expiry: {expiry} | Return: {percent}%
"Leverage used responsibly can accelerate gains" - {name}""",
    
    """💎 HODL STRATEGY WINS
{name} accumulated {symbol} at ${avg_price} average over {months} months
Current price: ${current_price} | Portfolio value: ${value} | Gain: {percent}%
"DCA and patience beats trying to time the market" - {name}""",
]

# Milestone celebrations
MILESTONE_STORIES = [
    "🎊 {name} just hit ${amount} in trading account - started {timeframe} ago with ${start}!",
    "🏆 First ${milestone} day for {name} trading {symbol} - dream come true!",
    "💯 {name} achieved {trades} consecutive profitable days - incredible consistency!",
    "🎯 {name}'s account up {percent}% YTD - crushing the market!",
    "🚀 {name} crossed ${amount} net profit milestone - started from ${start}!",
    "💰 {name} withdrew ${amount} in profits - paid off their {debt_type}!",
    "🎉 {name} hit {percent}% win rate over {trades} trades - master trader status!",
    "⚡ {name} just had their first ${amount} week - consistency paying off!",
    "💎 {name}'s portfolio hit ${portfolio} - {years} years of disciplined trading!",
    "🔥 {name} made ${profit} in {timeframe} - exceeded annual salary!",
]

# Recovery stories
RECOVERY_STORIES = [
    """💪 COMEBACK STORY
{name} was down ${loss} after {reason} but recovered through discipline
Current P/L: ${profit} | Time to recovery: {timeframe}
"Losses taught me more than wins ever did" - {name}""",
    
    """🎯 FROM BLOWN ACCOUNT TO PROFITABLE
{name} lost ${loss} learning, then made ${profit} after changing approach
Key change: {change}
"Failure is tuition paid to the market university" - {name}""",
    
    """📊 TURNED IT AROUND
After {losing_streak} losing trades, {name} analyzed mistakes and came back strong
Next {winning_streak} trades: {percent}% win rate, ${profit} recovered
"The pain of loss motivated me to improve" - {name}""",
]

# Strategy-specific successes
STRATEGY_SUCCESSES = [
    "📈 {strategy} strategy: {name} made ${profit} with {percent}% win rate",
    "🎯 {name}'s {strategy} approach netted ${profit} in {timeframe}",
    "💡 Using {strategy}, {name} turned ${start} into ${end}",
    "⚡ {strategy} trading working perfectly for {name} - ${profit} this week",
    "🔥 {name} mastered {strategy} - {percent}% monthly returns",
]

# Asset-specific success
ASSET_SUCCESSES = [
    "₿ Crypto success: {name} made ${profit} trading {crypto} - {percent}% gain",
    "📊 Stock win: {name} caught {stock} move from ${entry} to ${exit}",
    "💱 Forex profits: {name} scalped ${profit} on {pair} volatility",
    "🥇 Commodities: {name} rode gold rally for ${profit} gain",
    "🎯 Options: {name}'s {symbol} options returned {percent}% - ${profit} profit",
]

# Generate realistic names - 500+ unique combinations
FIRST_NAMES = [
    "Alex", "Sarah", "Mike", "Jennifer", "David", "Emily", "Chris", "Amanda",
    "Jason", "Lisa", "Kevin", "Michelle", "Brian", "Jessica", "Ryan", "Ashley",
    "Matthew", "Stephanie", "Daniel", "Lauren", "Andrew", "Nicole", "James", "Rachel",
    "Robert", "Megan", "John", "Rebecca", "Michael", "Laura", "William", "Hannah",
    "Thomas", "Samantha", "Joseph", "Amy", "Timothy", "Melissa", "Richard", "Susan",
    "Joshua", "Elizabeth", "Anthony", "Christina", "Mark", "Patricia", "Steven", "Maria",
    "Paul", "Nancy", "Donald", "Linda", "George", "Karen", "Kenneth", "Betty",
    "Brandon", "Helen", "Adam", "Sandra", "Eric", "Donna", "Nathan", "Carol",
    "Tyler", "Ruth", "Justin", "Sharon", "Aaron", "Michelle", "Jacob", "Dorothy",
    "Nicholas", "Angela", "Jonathan", "Kimberly", "Kyle", "Brenda", "Ethan", "Deborah",
    "Noah", "Pamela", "Logan", "Anna", "Lucas", "Virginia", "Benjamin", "Katherine",
    "Mason", "Christine", "Oliver", "Debra", "Elijah", "Catherine", "Aiden", "Carolyn",
    "Jackson", "Janet", "Sebastian", "Frances", "Carter", "Heather", "Jayden", "Diane",
    "Dylan", "Joyce", "Luke", "Julie", "Gabriel", "Evelyn", "Owen", "Joan",
    "Henry", "Victoria", "Isaac", "Kelly", "Wyatt", "Lauren", "Jack", "Christina",
    "Connor", "Alice", "Caleb", "Judith", "Julian", "Rose", "Levi", "Doris",
    "Hunter", "Kathryn", "Eli", "Gloria", "Jordan", "Teresa", "Cameron", "Sara",
    "Austin", "Janice", "Adrian", "Jean", "Colton", "Cheryl", "Dominic", "Mildred",
    "Ian", "Beverly", "Brayden", "Denise", "Jaxon", "Marilyn", "Xavier", "Amber",
    "Miles", "Danielle", "Easton", "Brittany", "Cooper", "Madison", "Landon", "Diana",
    "Parker", "Jane", "Christian", "Lori", "Carson", "Olivia", "Hudson", "Sophia",
    "Chase", "Emma", "Bentley", "Ava", "Blake", "Isabella", "Tristan", "Mia",
    "Cole", "Charlotte", "Brody", "Abigail", "Kai", "Harper", "Zachary", "Ella",
    "Maximus", "Avery", "Greyson", "Scarlett", "Wesley", "Grace", "Sawyer", "Chloe",
    "Maxwell", "Natalie", "Kingston", "Lily", "Ashton", "Zoe", "Roman", "Victoria",
    "Griffin", "Penelope", "Declan", "Riley", "Preston", "Nora", "Tucker", "Lillian",
    "Everett", "Aria", "Jace", "Leah", "Barrett", "Audrey", "Jude", "Brooklyn",
    "Silas", "Bella", "Elliot", "Claire", "Finn", "Skylar", "Rowan", "Lucy",
    "Marcus", "Paisley", "Colin", "Everly", "Ryker", "Anna", "Knox", "Caroline",
    "Phoenix", "Nova", "Jasper", "Genesis", "Cash", "Emilia", "Gage", "Kennedy",
    "River", "Samantha", "Leon", "Maya", "Atticus", "Willow", "Emmett", "Kinsley",
    "Reed", "Naomi", "Archer", "Aaliyah", "Ezra", "Elena", "Rhett", "Sarah",
    "Atlas", "Ariana", "Maddox", "Allison", "Theo", "Gabriella", "Beckett", "Alice",
    "Dean", "Madelyn", "Matteo", "Cora", "August", "Ruby", "Axel", "Eva",
    "Camden", "Serenity", "Felix", "Autumn", "Zane", "Adeline", "Clayton", "Hailey",
    "Crew", "Gianna", "Beau", "Valentina", "Brooks", "Isla", "Jonah", "Eliana",
    "Keegan", "Quinn", "Ronan", "Nevaeh", "Paxton", "Ivy", "Dallas", "Sadie",
    "Elliott", "Piper", "Graham", "Lydia", "Simon", "Alexa", "Tanner", "Josephine",
    "Peter", "Emery", "Victor", "Julia", "Antonio", "Delilah", "Gavin", "Arianna",
    "Bennett", "Vivian", "Harrison", "Kaylee", "Spencer", "Sophie", "Holden", "Brielle"
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas",
    "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White",
    "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", "Young",
    "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell",
    "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker",
    "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales", "Murphy",
    "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson", "Bailey",
    "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson",
    "Watson", "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza",
    "Ruiz", "Hughes", "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers",
    "Long", "Ross", "Foster", "Jimenez", "Powell", "Jenkins", "Perry", "Russell",
    "Sullivan", "Bell", "Coleman", "Butler", "Henderson", "Barnes", "Gonzales", "Fisher",
    "Vasquez", "Simmons", "Romero", "Jordan", "Patterson", "Alexander", "Hamilton", "Graham",
    "Reynolds", "Griffin", "Wallace", "Moreno", "West", "Cole", "Hayes", "Bryant",
    "Herrera", "Gibson", "Ellis", "Tran", "Medina", "Aguilar", "Stevens", "Murray",
    "Ford", "Castro", "Marshall", "Owens", "Harrison", "Fernandez", "McDonald", "Woods",
    "Washington", "Kennedy", "Wells", "Vargas", "Henry", "Chen", "Freeman", "Webb",
    "Tucker", "Guzman", "Burns", "Crawford", "Olson", "Simpson", "Porter", "Hunter"
]

def generate_name():
    """Generate unique full name"""
    return f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"

def generate_success_story():
    """Generate a random success story"""
    template = random.choice(SUCCESS_TEMPLATES)
    
    start_amounts = [500, 1000, 2000, 5000, 10000, 20000]
    multipliers = [2, 3, 5, 10, 20, 50, 100]
    
    start = random.choice(start_amounts)
    mult = random.choice(multipliers)
    end = start * mult
    
    return template.format(
        name=generate_name(),
        start_amount=f"{start:,}",
        end_amount=f"{end:,}",
        timeframe=random.choice(["3 months", "6 months", "1 year", "2 years"]),
        asset_class=random.choice(["stocks", "crypto", "forex", "options"]),
        strategy=random.choice(["momentum", "swing trading", "scalping", "position trading"]),
        symbol=random.choice(["BTC", "TSLA", "NVDA", "SPY", "ETH"]),
        milestone=random.choice(["10k", "50k", "100k", "250k", "500k"]),
        gain=f"{random.randint(1000, 50000):,}",
        percent=random.randint(50, 500),
        wins=random.randint(5, 20),
        profit=f"{random.randint(500, 10000):,}",
        minutes=random.randint(5, 60),
        monthly=f"{random.randint(5000, 50000):,}",
        loss=f"{random.randint(1000, 10000):,}",
        entry=random.randint(10, 200),
        exit=random.randint(50, 500)
    )

def generate_detailed_story():
    """Generate detailed success story"""
    template = random.choice(DETAILED_STORIES)
    
    return template.format(
        name=generate_name(),
        symbol=random.choice(["BTC", "ETH", "TSLA", "NVDA", "AAPL", "SPY"]),
        percent=random.randint(10, 50),
        gain=random.randint(50, 500),
        entry=random.randint(20, 100),
        exit=random.randint(100, 500),
        profit=f"{random.randint(5000, 100000):,}",
        indicator=random.choice(["RSI", "MACD", "Volume"]),
        timeframe=random.choice(["swing", "day", "position"]),
        target=random.randint(200, 500),
        current=random.randint(150, 400),
        wins=random.randint(15, 25),
        total=random.randint(20, 30),
        avg_win=f"{random.randint(200, 1000):,}",
        avg_loss=f"{random.randint(100, 500):,}",
        net_profit=f"{random.randint(5000, 20000):,}",
        start_amount=f"{random.randint(1000, 10000):,}",
        end_amount=f"{random.randint(50000, 500000):,}",
        months=random.randint(3, 18),
        years=random.randint(1, 5),
        portfolio_size=f"{random.randint(100000, 1000000):,}",
        trades=random.randint(20, 100),
        total_profit=f"{random.randint(1000, 5000):,}",
        avg_profit=f"{random.randint(50, 200):,}",
        start=random.randint(50, 150),
        end=random.randint(200, 500),
        premium=f"{random.randint(500, 5000):,}",
        strike=random.randint(100, 300),
        expiry=random.choice(["1 week", "2 weeks", "1 month"]),
        avg_price=random.randint(20, 100),
        current_price=random.randint(100, 300),
        value=f"{random.randint(50000, 500000):,}",
        quote=random.choice([
            "Trust the process",
            "Patience pays",
            "Follow your plan",
            "Risk management is everything"
        ])
    )

# Compile all stories
ALL_STORIES = []

# Generate hundreds of variations
for _ in range(200):
    ALL_STORIES.append(generate_success_story())

for _ in range(100):
    ALL_STORIES.append(generate_detailed_story())

# Add milestone stories
for _ in range(100):
    template = random.choice(MILESTONE_STORIES)
    ALL_STORIES.append(template.format(
        name=generate_name(),
        amount=f"{random.choice([10000, 25000, 50000, 100000, 250000]):,}",
        start=f"{random.choice([500, 1000, 5000, 10000]):,}",
        timeframe=random.choice(["6 months", "1 year", "2 years"]),
        milestone=random.choice([1000, 5000, 10000, 50000]),
        symbol=random.choice(["BTC", "TSLA", "NVDA"]),
        trades=random.randint(10, 30),
        percent=random.randint(50, 300),
        debt_type=random.choice(["mortgage", "student loans", "car loan", "credit card debt"]),
        profit=f"{random.randint(10000, 100000):,}",
        portfolio=f"{random.randint(100000, 1000000):,}",
        years=random.randint(2, 10)
    ))

# Add recovery stories
for _ in range(50):
    template = random.choice(RECOVERY_STORIES)
    ALL_STORIES.append(template.format(
        name=generate_name(),
        loss=f"{random.randint(5000, 50000):,}",
        reason=random.choice(["revenge trading", "over-leveraging", "ignoring stops"]),
        profit=f"{random.randint(10000, 100000):,}",
        timeframe=random.choice(["3 months", "6 months", "1 year"]),
        change=random.choice(["strict risk management", "following a system", "cutting losses quickly"]),
        losing_streak=random.randint(5, 15),
        winning_streak=random.randint(10, 25),
        percent=random.randint(60, 90)
    ))

# Add strategy successes
strategies = ["momentum", "scalping", "swing", "breakout", "mean reversion", "trend following"]
for strategy in strategies:
    for _ in range(10):
        template = random.choice(STRATEGY_SUCCESSES)
        ALL_STORIES.append(template.format(
            strategy=strategy,
            name=generate_name(),
            profit=f"{random.randint(5000, 50000):,}",
            percent=random.randint(60, 95),
            timeframe=random.choice(["this month", "this week", "today"]),
            start=f"{random.randint(1000, 10000):,}",
            end=f"{random.randint(20000, 100000):,}"
        ))

def get_random_story():
    """Get random success story"""
    return random.choice(ALL_STORIES)

def get_milestone_story():
    """Get milestone-focused story"""
    milestones = [s for s in ALL_STORIES if any(word in s for word in ["hit", "crossed", "achieved", "First"])]
    return random.choice(milestones) if milestones else get_random_story()

__all__ = ['ALL_STORIES', 'get_random_story', 'get_milestone_story']

print(f"✅ Loaded {len(ALL_STORIES)} success stories")
