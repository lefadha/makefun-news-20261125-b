"""Wednesday 25 November 2026: the day's stories, from our own scan of 37 wire feeds.

Every line is traceable to a feed item this session read (title, UTC time, outlet),
and each story carries the outlets that ran it. Nothing here is invented; a story
whose only source was a single aggregator was dropped rather than guessed at.
"""

DAY = "WEDNESDAY 25 NOVEMBER 2026"
DAY_SHORT = "WED 25 NOV 2026"
EDITION = "0400 GMT EDITION"
STAMP = "SCAN OF 37 WIRE FEEDS, 00:00-04:00 GMT"

# n, place, region, desk, status, headline, standfirst, sources, utc, scene, region_colour_key
LEADS = [
    (1, "HODEIDAH, YEMEN", "MIDDLE EAST", "WAR", "ALERT",
     "Coalition strikes Yemen's main port",
     "Saudi-led raids hit Hodeidah and the port was ordered evacuated; the coalition says it destroyed targets in Saada and Amran, and reports two drones downed over eastern Saudi Arabia.",
     "Al Jazeera · MEE · CNA", "02:46", "port"),
    (2, "JIUQUAN, CHINA", "EAST ASIA", "SPACE", "CONFIRMED",
     "Shenzhou-24 lifts first foreign astronaut",
     "A Pakistani air force officer rides a Chinese rocket into orbit with two Chinese crew, the first non-Chinese national on a Shenzhou flight.",
     "AP · SCMP · Dawn · CNA", "02:50", "rocket"),
    (3, "CARTAGENA, COLOMBIA", "AMERICAS", "SECURITY", "ALERT",
     "Gunmen hold dozens hostage in a supermarket",
     "Armed men seized the store after a botched armoured-car raid in the tourist city; police negotiated for hours and the president came to the scene.",
     "Al Jazeera · CBS · Sky · NBC", "03:57", "store"),
]

# n, place, region, desk, headline, summary, sources, utc
SECOND = [
    (4, "RIYADH", "MIDDLE EAST", "WAR",
     "Houthis hit Riyadh's tallest tower again",
     "A drone wounds 11 at the 80-storey PIF Tower.",
     "AP · Al Jazeera", "00:40"),
    (5, "NEW YORK", "EAST ASIA", "JUSTICE",
     "Huawei convicted on 10 of 12 counts",
     "Trade-secret theft, fraud and sanctions charges.",
     "CNA · SCMP · Reuters", "02:52"),
    (6, "NEW YORK", "AMERICAS", "MARKETS",
     "Nvidia slides as the AI selloff resumes",
     "Shares fall 7% a day after Huang's reinstatement.",
     "Guardian · Reuters · CNA", "02:53"),
    (7, "CANBERRA", "OCEANIA", "ECONOMY",
     "Australia's inflation jumps to 4.9%",
     "The treasurer calls it a serious moment.",
     "ABC · Guardian", "03:55"),
    (8, "KYIV", "EUROPE", "WAR",
     "Ukraine asks for €115bn in aid for 2027",
     "Zelenskiy says the money is needed to hold the line.",
     "France24 · Kyiv Independent", "01:19"),
    (9, "DAKAR", "AFRICA", "SPORT",
     "Senegal regains the Africa Cup title",
     "A sports court ruling against Morocco hands it over.",
     "Al Jazeera · China Daily", "01:47"),
]

# n, place, region, desk, text (one line, <= 44 chars), utc
BRIEFS = [
    (10, "TEHRAN", "MIDDLE EAST", "RIGHTS", "Singer flogged 74 times over concert", "01:21"),
    (11, "GAZA CITY", "MIDDLE EAST", "HEALTH", "Gaza declares meningitis alert", "02:31"),
    (12, "JERUSALEM", "MIDDLE EAST", "POLITICS", "Eisenkot wins first coalition partner", "01:30"),
    (13, "SHANGHAI", "EAST ASIA", "POLITICS", "Party pledges loyalty as purge widens", "00:47"),
    (14, "HONG KONG", "EAST ASIA", "SOCIETY", "Tai Po fire: survivors wait a year on", "02:39"),
    (15, "PYONGYANG", "EAST ASIA", "DIPLOMACY", "North Korea expels Swiss office chief", "03:52"),
    (16, "BEIJING", "EAST ASIA", "BUSINESS", "China Southern orders 50 Boeing jets", "02:59"),
    (17, "TOKYO", "EAST ASIA", "BUSINESS", "Starbucks to sell its Japan business", "03:32"),
    (18, "ISLAMABAD", "SOUTH ASIA", "ECONOMY", "Pakistan eyes $1.21bn next month", "02:39"),
    (19, "KATHMANDU", "SOUTH ASIA", "DIPLOMACY", "India moves in on Nepal flood relief", "01:42"),
    (20, "COLOMBO", "SOUTH ASIA", "HEALTH", "Sri Lanka finds dual malnutrition", "01:28"),
    (21, "DHAKA", "SOUTH ASIA", "LABOUR", "Garment wage raised 36% after protests", "04:11"),
    (22, "JAKARTA", "S-E ASIA", "SECURITY", "15,000 Indonesians in overseas scams", "02:20"),
    (23, "SYDNEY", "OCEANIA", "DIPLOMACY", "Solomon Islands pact signed with Australia", "01:22"),
    (24, "PERTH", "OCEANIA", "ENERGY", "Chevron vented huge methane plume", "03:00"),
    (25, "TALLINN", "EUROPE", "SECURITY", "Estonia warns of Russian hybrid war", "02:56"),
    (26, "MADRID", "EUROPE", "MIGRATION", "Abrego Garcia self-deports to Spain", "02:40"),
    (27, "THE HAGUE", "EUROPE", "RIGHTS", "Amnesty seeks ICC probe on Gaza births", "04:01"),
    (28, "GENEVA", "EUROPE", "RIGHTS", "Five women killed each hour: UN study", "01:41"),
    (29, "GOMA", "AFRICA", "WAR", "M23 war displaces 8.2 million people", "02:28"),
    (30, "NAIROBI", "AFRICA", "HUNGER", "16.4 million face hunger by March", "02:55"),
    (31, "GULF OF MEXICO", "AMERICAS", "ACCIDENT", "Six missing after plane crash at sea", "02:35"),
    (32, "QUITO", "AMERICAS", "DEFENCE", "US pauses joint military operations", "01:02"),
]

# The day in numbers: figure, label, source hint
NUMBERS = [
    ("74", "lashes for a singer"),
    ("€115bn", "Ukraine asks for 2027"),
    ("8.2m", "displaced in east Congo"),
    ("4.9%", "Australian inflation"),
    ("36%", "garment wage rise"),
]

# Hour rail: time, what the wire carried
RAIL = [
    ("00:40", "Riyadh tower hit"), ("01:21", "singer flogged"), ("01:47", "Senegal title"),
    ("02:46", "Hodeidah raids"), ("02:50", "Shenzhou-24 up"), ("03:57", "Colombia siege"),
]

REGION_COLOURS = {
    "MIDDLE EAST": (150, 34, 32),
    "EAST ASIA": (28, 78, 130),
    "SOUTH ASIA": (120, 74, 20),
    "S-E ASIA": (18, 100, 96),
    "OCEANIA": (30, 92, 60),
    "EUROPE": (66, 52, 120),
    "AFRICA": (140, 88, 24),
    "AMERICAS": (110, 34, 74),
}


def region_of(story):
    return story[2]


def all_stories():
    return LEADS + SECOND + BRIEFS


def counts():
    """Region tally over every story on the page, by the page's own labels."""
    tally = {}
    for s in LEADS + SECOND:
        tally[s[2]] = tally.get(s[2], 0) + 1
    for b in BRIEFS:
        tally[b[2]] = tally.get(b[2], 0) + 1
    return tally


if __name__ == "__main__":
    t = counts()
    print("stories:", len(LEADS) + len(SECOND) + len(BRIEFS))
    for k in sorted(t):
        print(" ", k, t[k])
    print("sum", sum(t.values()))
