"""
Trader Testimonials - 500+ Authentic-sounding testimonials
Community member experiences and reviews
"""

import random
from success_stories import FIRST_NAMES, LAST_NAMES

def generate_name():
    """Generate unique full name"""
    return f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"

# Testimonial templates
TESTIMONIAL_TEMPLATES = [
    '"{quote}" - {name}, {title}',
    '⭐⭐⭐⭐⭐ "{quote}" - {name}',
    '💬 {name} says: "{quote}"',
    '🗣️ "{quote}" - {name}, trading for {years} years',
    '"{quote}" - {name} | {achievement}',
]

# Positive quotes about the community/platform
POSITIVE_QUOTES = [
    "This community changed my trading game completely",
    "Best trading signals I've ever followed",
    "Finally found a group that actually delivers results",
    "The education here is worth thousands of dollars",
    "My account has grown {percent}% since joining",
    "These traders actually know what they're doing",
    "Transparency and authenticity - exactly what I needed",
    "Learned more here in {months} months than {years} years on my own",
    "The verification system gives me confidence in every trade",
    "Risk management tips alone paid for my subscription",
    "Community support is incredible - helped me through tough times",
    "Finally making consistent profits thanks to this group",
    "The market analysis is spot-on every time",
    "Best decision I made for my trading career",
    "Professional traders sharing real setups - priceless",
]

# Specific achievement quotes
ACHIEVEMENT_QUOTES = [
    "Made my first ${amount} in profit this month",
    "Went from losing trader to profitable in {months} months",
    "Hit my ${amount} account goal thanks to this community",
    "My win rate improved from {low}% to {high}%",
    "Finally quit my job to trade full-time",
    "Paid off my ${debt} debt with trading profits",
    "Turned ${start} into ${end} following these strategies",
    "First ${amount} day ever - couldn't have done it without you all",
    "Account up {percent}% this year - best year ever",
    "Made back everything I lost before finding this group",
]

# Learning-focused quotes
LEARNING_QUOTES = [
    "The educational content is worth more than paid courses",
    "Finally understand technical analysis properly",
    "Risk management lessons saved my account",
    "Learned to control my emotions trading",
    "The mentorship here is invaluable",
    "Went from complete beginner to confident trader",
    "Chart pattern recognition improved dramatically",
    "Understanding market psychology now",
    "The daily tips helped me stay disciplined",
    "Best trading education available anywhere",
]

# Community-focused quotes
COMMUNITY_QUOTES = [
    "Everyone here genuinely wants to see you succeed",
    "No gatekeeping - knowledge freely shared",
    "Most supportive trading community I've found",
    "The positive energy here is contagious",
    "Found my trading tribe here",
    "People actually answer questions here",
    "No toxic behavior - pure helpful content",
    "Feel like part of a family",
    "Accountability partners here kept me on track",
    "Best community in the trading space",
]

# Platform-specific quotes
PLATFORM_QUOTES = [
    "The verified trader system builds trust",
    "Love seeing real results, not fake screenshots",
    "Transparency is refreshing in trading world",
    "Real-time trade updates are incredibly helpful",
    "The trade verification gives me confidence",
    "Platform is easy to navigate and use",
    "Mobile access means I never miss alerts",
    "Integration with my broker is seamless",
    "Analytics dashboard helped me improve",
    "Best trading platform I've used",
]

# Before/After quotes
TRANSFORMATION_QUOTES = [
    "Before: Losing money every week. After: Consistent profits",
    "Before: Emotional trading. After: Disciplined and systematic",
    "Before: Confused and lost. After: Clear strategy and confidence",
    "Before: Chasing losses. After: Following the plan",
    "Before: Over-trading. After: Selective and patient",
    "Before: No risk management. After: Protect capital first",
    "Before: FOMO trades. After: Wait for setups",
    "Before: Giving up. After: More motivated than ever",
    "Before: Random trades. After: Strategic entries",
    "Before: Alone in trading. After: Supported by community",
]

# Specific feature testimonials
FEATURE_TESTIMONIALS = [
    "The market analysis posts are always accurate",
    "Daily tips keep me disciplined",
    "Success stories motivate me to keep going",
    "Risk warnings prevented me from over-leveraging",
    "Educational content is top-tier",
    "Real-time trade alerts are game-changing",
    "Portfolio tracking features are excellent",
    "The community polls spark great discussions",
    "Weekly recaps help me see progress",
    "Trade verification is brilliant innovation",
]

# Generate comprehensive testimonials
def generate_testimonial():
    """Generate a realistic testimonial"""
    template = random.choice(TESTIMONIAL_TEMPLATES)
    quote_categories = [
        POSITIVE_QUOTES,
        ACHIEVEMENT_QUOTES,
        LEARNING_QUOTES,
        COMMUNITY_QUOTES,
        PLATFORM_QUOTES,
        TRANSFORMATION_QUOTES,
        FEATURE_TESTIMONIALS
    ]
    
    quote = random.choice(random.choice(quote_categories))
    
    # Fill in template variables
    quote = quote.format(
        percent=random.randint(10, 200),
        months=random.randint(1, 12),
        years=random.randint(1, 5),
        amount=f"{random.choice([1000, 5000, 10000, 25000, 50000]):,}",
        low=random.randint(20, 40),
        high=random.randint(60, 85),
        debt=f"{random.choice([10000, 25000, 50000]):,}",
        start=f"{random.choice([1000, 5000, 10000]):,}",
        end=f"{random.choice([25000, 50000, 100000]):,}"
    )
    
    testimonial = template.format(
        quote=quote,
        name=generate_name(),
        title=random.choice([
            "Day Trader",
            "Swing Trader",
            "Options Trader",
            "Crypto Trader",
            "Forex Trader",
            "Full-time Trader",
            "Part-time Trader",
            "Professional Trader"
        ]),
        years=random.randint(1, 10),
        achievement=random.choice([
            "Profitable 8 months running",
            "Grew account 150% this year",
            "Quit day job",
            "Consistent winner",
            "Trading full-time",
            "Six-figure trader"
        ])
    )
    
    return testimonial

# Pre-generate testimonials
ALL_TESTIMONIALS = []
for _ in range(500):
    ALL_TESTIMONIALS.append(generate_testimonial())

# Detailed testimonials (longer form)
DETAILED_TESTIMONIALS = []

def generate_detailed_testimonial():
    """Generate longer, detailed testimonial"""
    name = generate_name()
    story_templates = [
        f"""⭐⭐⭐⭐⭐ LIFE-CHANGING EXPERIENCE
\"{random.choice(POSITIVE_QUOTES)}. {random.choice(ACHIEVEMENT_QUOTES).format(
    percent=random.randint(50, 300),
    months=random.randint(3, 12),
    years=random.randint(1, 3),
    amount=f'{random.choice([10000, 25000, 50000]):,}',
    low=random.randint(20, 40),
    high=random.randint(65, 85),
    debt=f'{random.choice([15000, 30000]):,}',
    start=f'{random.choice([2000, 5000]):,}',
    end=f'{random.choice([30000, 75000]):,}'
)}. {random.choice(LEARNING_QUOTES)}. {random.choice(COMMUNITY_QUOTES)}.\"
- {name}, member since {random.choice(['Jan 2024', 'Mar 2024', 'Jun 2024', 'Sep 2024'])}""",

        f"""💎 HIGHLY RECOMMEND
\"{random.choice(TRANSFORMATION_QUOTES)}. {random.choice(PLATFORM_QUOTES)}. {random.choice(FEATURE_TESTIMONIALS)}. This isn't just a signal group - it's a complete trading education.\"
- {name}, {random.choice(['Professional Trader', 'Full-time Trader', 'Former Engineer'])}""",

        f"""🚀 EXCEEDED EXPECTATIONS
\"I was skeptical at first, but {random.choice(POSITIVE_QUOTES).lower()}. {random.choice(ACHIEVEMENT_QUOTES).format(
    percent=random.randint(75, 250),
    months=random.randint(2, 8),
    years=random.randint(1, 4),
    amount=f'{random.choice([5000, 15000, 35000]):,}',
    low=random.randint(25, 45),
    high=random.randint(70, 90),
    debt=f'{random.choice([20000, 40000]):,}',
    start=f'{random.choice([3000, 8000]):,}',
    end=f'{random.choice([40000, 100000]):,}'
)}. Worth every penny and more.\"
- {name}, trading for {random.randint(2, 8)} years""",
    ]
    
    return random.choice(story_templates)

for _ in range(100):
    DETAILED_TESTIMONIALS.append(generate_detailed_testimonial())

ALL_TESTIMONIALS.extend(DETAILED_TESTIMONIALS)

# Add video-style testimonials
VIDEO_STYLE = []
for _ in range(50):
    name = generate_name()
    VIDEO_STYLE.append(f"""
🎥 {name} - Video Testimonial
"{random.choice(POSITIVE_QUOTES)}. My results speak for themselves: {random.choice(ACHIEVEMENT_QUOTES).format(
    percent=random.randint(40, 180),
    months=random.randint(2, 10),
    years=random.randint(1, 5),
    amount=f'{random.choice([8000, 20000, 45000]):,}',
    low=random.randint(30, 45),
    high=random.randint(68, 88),
    debt=f'{random.choice([12000, 28000]):,}',
    start=f'{random.choice([2500, 6000]):,}',
    end=f'{random.choice([25000, 65000]):,}'
)}. If you're serious about trading, join this community."
⭐⭐⭐⭐⭐
    """.strip())

ALL_TESTIMONIALS.extend(VIDEO_STYLE)

def get_random_testimonial():
    """Get a random testimonial"""
    return random.choice(ALL_TESTIMONIALS)

def get_detailed_testimonial():
    """Get a detailed/longer testimonial"""
    return random.choice(DETAILED_TESTIMONIALS + VIDEO_STYLE)

def get_short_testimonial():
    """Get a short testimonial"""
    short_ones = [t for t in ALL_TESTIMONIALS if len(t) < 150]
    return random.choice(short_ones) if short_ones else get_random_testimonial()

__all__ = [
    'ALL_TESTIMONIALS',
    'get_random_testimonial',
    'get_detailed_testimonial',
    'get_short_testimonial'
]

print(f"✅ Loaded {len(ALL_TESTIMONIALS)} trader testimonials")
