#!/usr/bin/env python3
"""Bygger viccom.se på engelska (rot) och svenska (/sv/).

Kör:  python3 _src/build.py      (från repots rot)

All text ligger i det här skriptet, i par: E (engelska) och S (svenska).
Ändra här och kör om, så hålls båda språken, menyer och sidfötter i synk.
Mappar som börjar med _ publiceras inte av GitHub Pages.
"""
from pathlib import Path
import html

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://viccom.se"
CSS_V = "3"  # höj när style.css eller frost.js ändras, så att webbläsare hämtar nytt

# ---------------------------------------------------------------- sökvägar
# Integritetspolicy och radera-konto på svenska ligger kvar i roten:
# de adresserna är inlagda i Google Play Console.
PATHS = {
    "home":    {"en": "/",                   "sv": "/sv/"},
    "ww":      {"en": "/wobble-wheels.html", "sv": "/sv/wobble-wheels.html"},
    "wyrm":    {"en": "/wyrmwind.html",      "sv": "/sv/wyrmwind.html"},
    "anylap":  {"en": "/anylap.html",        "sv": "/sv/anylap.html"},
    "psst":    {"en": "/psst.html",          "sv": "/sv/psst.html"},
    "press":   {"en": "/press.html",         "sv": "/sv/press.html"},
    "privacy": {"en": "/privacy.html",       "sv": "/integritetspolicy.html"},
    "delete":  {"en": "/delete-account.html","sv": "/radera-konto.html"},
}

def url(key, lang, anchor=""):
    return PATHS[key][lang] + anchor

def outfile(key, lang):
    p = PATHS[key][lang]
    if p.endswith("/"):
        d = p.strip("/")
        return ROOT / d / "index.html" if d else ROOT / "index.html"
    return ROOT / p.strip("/")

def L(lang, en, sv):
    return en if lang == "en" else sv

# ---------------------------------------------------------------- produkter
# status: live | test | dev | proto     meter: 0–100 (grov känsla, inte exakt)
PRODUCTS = [
    {
        "key": "ww", "name": "Wobble Wheels", "kind": "game", "status": "test", "meter": 90,
        "accent": "#DD700B",
        "art": "/ww-feature.webp", "art_png": "/ww-feature-1024x500.png",
        "type":    {"en": "Mobile game", "sv": "Mobilspel"},
        "badge":   {"en": "Closed test · Launching November", "sv": "Stängt test · Släpps i november"},
        "tagline": {"en": "Draw your wheels. Beat your friends.", "sv": "Rita dina hjul. Slå dina vänner."},
        "alt":     {"en": "Wobble Wheels: five cars with hand-drawn wheels racing along a road at sunset.",
                    "sv": "Wobble Wheels: fem bilar med handritade hjul racar längs en väg i solnedgång."},
        "short":   {"en": "A racing game where you draw your own wheels, then redraw them mid-race when the road changes. Spikes bite on ice, paddles get you through floods, small wheels fit low tunnels. Race friends live, chase world-record flags and climb ranked seasons.",
                    "sv": "Ett racingspel där du ritar dina egna hjul, och ritar om dem mitt i loppet när vägen byter skepnad. Spikar biter på is, paddlar tar dig genom översvämningar, små hjul klarar låga tunnlar. Tävla live mot vänner, jaga världsrekordflaggor och klättra i rankade säsonger."},
        "body": {
            "en": ["In Wobble Wheels the wheels are all that matter. You draw them yourself, with your finger, and redraw them any time during a race. The road keeps changing: glare ice, floods, low tunnels, mud and roots, speed bumps. Every surface wants a different wheel, and the best driver is the one who redraws first.",
                   "You race real players in live races, a weekly Sunday cup and ranked seasons from Bronze to Grandmaster. Every best run leaves a flag on the road, so you see exactly where the world record is.",
                   "Every car drives exactly the same. Bodies, paints, tyres and flags are looks only, and you earn them by playing."],
            "sv": ["I Wobble Wheels är hjulen det enda som räknas. Du ritar dem själv, med fingret, och ritar om dem när som helst mitt i loppet. Vägen byter hela tiden skepnad: glansig is, översvämningar, låga tunnlar, lera och rötter, farthinder. Varje underlag vill ha ett annat hjul, och den som hinner rita om först vinner.",
                   "Du kör mot riktiga spelare i live-lopp, i en veckovis söndagscup och i rankade säsonger från Bronze till Grandmaster. Varje bästa tid lämnar en flagga på vägen, så du ser exakt var världsrekordet ligger.",
                   "Alla bilar kör exakt likadant. Karosser, lack, däck och flaggor är bara utseende, och du tjänar dem genom att spela."],
        },
        "specs": [
            ({"en": "Platform", "sv": "Plattform"}, {"en": "Android on Google Play. Test build in your browser. iOS later.", "sv": "Android via Google Play. Testversion i webbläsaren. iOS senare."}),
            ({"en": "Status", "sv": "Status"}, {"en": "Closed test on Google Play", "sv": "Stängt test på Google Play"}),
            ({"en": "Launch", "sv": "Släpp"}, {"en": "November 2026", "sv": "November 2026"}),
            ({"en": "Players", "sv": "Spelare"}, {"en": "Up to 5 per live race", "sv": "Upp till 5 per live-lopp"}),
            ({"en": "Price", "sv": "Pris"}, {"en": "Free to play. No pay to win.", "sv": "Gratis att spela. Inget pay to win."}),
        ],
        "features": [
            ({"en": "Draw your wheels", "sv": "Rita dina hjul"}, {"en": "Draw any shape on the pad. Spikes bite on ice, round wheels slide. The shape decides everything.", "sv": "Rita valfri form på ritytan. Spikar biter på is, runda hjul glider. Formen avgör allt."}),
            ({"en": "Redraw mid-race", "sv": "Rita om mitt i loppet"}, {"en": "Small wheels for low tunnels, paddles for floods, cogs for mud and roots, big round ones for speed bumps.", "sv": "Små hjul för låga tunnlar, paddlar för översvämningar, kuggar för lera och rötter, stora runda för farthinder."}),
            ({"en": "Live online races", "sv": "Live-lopp online"}, {"en": "Up to five players in the same race, with boost and grip you choose when to use.", "sv": "Upp till fem spelare i samma lopp, med boost och grepp som du väljer när du använder."}),
            ({"en": "The Sunday cup", "sv": "Söndagscupen"}, {"en": "One week, one track, one winner. Every Sunday.", "sv": "En vecka, en bana, en vinnare. Varje söndag."}),
            ({"en": "World-record flags", "sv": "Världsrekordflaggor"}, {"en": "Every best run leaves a flag on the road. Pass it and you're on record pace.", "sv": "Varje bästa tid lämnar en flagga på vägen. Kör förbi den och du är på rekordtempo."}),
            ({"en": "Ranked seasons", "sv": "Rankade säsonger"}, {"en": "Leagues from Bronze to Grandmaster, with leaderboards and seasons.", "sv": "Ligor från Bronze till Grandmaster, med topplistor och säsonger."}),
            ({"en": "18 car bodies", "sv": "18 karosser"}, {"en": "Hot dog, bathtub, shopping cart, rocket, skeleton car, ghost car, truck, Santa's sleigh and more. All drive the same.", "sv": "Korv, badkar, kundvagn, raket, skelettbil, spökbil, lastbil, tomtesläde och fler. Alla kör likadant."}),
            ({"en": "No pay to win", "sv": "Inget pay to win"}, {"en": "Earn the looks, not the stats. No car is faster than any other.", "sv": "Du tjänar utseendet, inte statsen. Ingen bil är snabbare än någon annan."}),
        ],
        "shots": [
            ("/ww-shot-1.webp", {"en": "Fly past the leader: low gravity and big air on the moon.", "sv": "Flyg förbi ledaren: låg gravitation och höga hopp på månen."}),
            ("/ww-shot-2.webp", {"en": "Draw your wheels: spiked wheels on glare ice.", "sv": "Rita dina hjul: spikhjul på glansig is."}),
            ("/ww-shot-3.webp", {"en": "Redraw for every road: small wheels, paddles, spikes, cogs and big round wheels.", "sv": "Rita om för varje väg: små hjul, paddlar, spikar, kuggar och stora runda hjul."}),
            ("/ww-shot-4.webp", {"en": "Pass the world record: a record flag on the road and confetti.", "sv": "Slå världsrekordet: en rekordflagga på vägen och konfetti."}),
            ("/ww-shot-5.webp", {"en": "Beat your friends: live online races at sunset.", "sv": "Slå dina vänner: live online-lopp i solnedgång."}),
            ("/ww-shot-6.webp", {"en": "Climb to Grandmaster: ranked leagues and leaderboard.", "sv": "Klättra till Grandmaster: rankade ligor och topplista."}),
            ("/ww-shot-7.webp", {"en": "No pay to win: 18 car bodies that all drive the same.", "sv": "Inget pay to win: 18 bilkarosser som alla kör likadant."}),
        ],
        "cta": [
            ({"en": "Play the test build", "sv": "Spela testversionen"}, "/play/", "btn"),
            ({"en": "Follow the launch", "sv": "Följ släppet"}, "https://www.instagram.com/viccom_games/", "btn ghost"),
        ],
        "note": {"en": "The Google Play link goes here at launch. Until then, the browser version is the newest test build.",
                 "sv": "Länken till Google Play hamnar här vid släppet. Fram till dess är webbversionen det senaste testbygget."},
    },
    {
        "key": "wyrm", "name": "Wyrmwind", "kind": "game", "status": "proto", "meter": 20,
        "accent": "#8B5CF6",
        "art": "/wyrmwind-feature.webp", "art_png": "/wyrmwind-feature-1024x500.png",
        "type":    {"en": "Game", "sv": "Spel"},
        "badge":   {"en": "Prototype", "sv": "Prototyp"},
        "tagline": {"en": "Race dragons through the storm.", "sv": "Kappflyg med drakar genom stormen."},
        "alt":     {"en": "Wyrmwind: a red dragon breathes fire toward a glowing portal above a castle in a storm.",
                    "sv": "Wyrmwind: en röd drake sprutar eld mot en lysande portal ovanför ett slott i storm."},
        "short":   {"en": "A dragon racing game. Fly through storm-torn skies, hit the portals and leave the other riders behind. It's an early prototype, and it ships when it's done.",
                    "sv": "Ett racingspel med drakar. Flyg genom stormiga himlar, träffa portalerna och lämna de andra ryttarna bakom dig. Det är en tidig prototyp, och det släpps när det är klart."},
        "body": {
            "en": ["Wyrmwind is our dragon racing game. You ride a dragon through storm-torn skies, chain portals for speed and race other riders to the finish.",
                   "It's an early prototype. We're getting the flying to feel right before anything else, and we'll show more when there's something worth showing. It ships when it's done."],
            "sv": ["Wyrmwind är vårt racingspel med drakar. Du rider en drake genom stormiga himlar, kedjar ihop portaler för fart och tävlar mot andra ryttare till mål.",
                   "Det är en tidig prototyp. Först ska flygandet kännas rätt, sedan resten, och vi visar mer när det finns något värt att visa. Det släpps när det är klart."],
        },
        "specs": [
            ({"en": "Genre", "sv": "Genre"}, {"en": "Racing", "sv": "Racing"}),
            ({"en": "Platform", "sv": "Plattform"}, {"en": "To be announced", "sv": "Meddelas senare"}),
            ({"en": "Status", "sv": "Status"}, {"en": "Prototype", "sv": "Prototyp"}),
            ({"en": "Launch", "sv": "Släpp"}, {"en": "When it's done", "sv": "När det är klart"}),
        ],
        "features": [],
        "shots": [],
        "cta": [
            ({"en": "Follow development", "sv": "Följ utvecklingen"}, "https://www.instagram.com/viccom_games/", "btn ghost"),
        ],
        "note": None,
    },
    {
        "key": "anylap", "name": "AnyLap", "kind": "app", "status": "dev", "meter": 45,
        "accent": "#E10600",
        "art": None,
        "icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="13" r="8"/><path d="M12 13V8M9 2h6M19 5l1.5-1.5"/></svg>',
        "type":    {"en": "App", "sv": "App"},
        "badge":   {"en": "In development · v0.3", "sv": "Under utveckling · v0.3"},
        "tagline": {"en": "A lap timer for RC cars that runs on your phone's camera.", "sv": "Ett varvtidtagarur för radiostyrda bilar som använder mobilens kamera."},
        "alt":     {"en": "", "sv": ""},
        "short":   {"en": "Point your phone at the finish line and AnyLap counts laps and times them as the cars cross it. No transponders, no extra hardware.",
                    "sv": "Rikta mobilen mot mållinjen så räknar AnyLap varv och tar tid när bilarna passerar. Inga transpondrar, ingen extra utrustning."},
        "body": {
            "en": ["AnyLap turns your phone into a lap timer for RC cars. Set it up by the track, point the camera at the finish line, and it recognises each car as it crosses and times the lap.",
                   "No transponders and no timing loop. Lap times, stats and replays are saved on your phone, so you can compare runs and see if that setup change actually helped. No account, no ads, and nothing leaves the phone unless you share it."],
            "sv": ["AnyLap gör mobilen till ett varvtidtagarur för radiostyrda bilar. Ställ den vid banan, rikta kameran mot mållinjen, så känner den igen varje bil som passerar och tar tid på varvet.",
                   "Inga transpondrar och ingen tidtagningsslinga. Varvtider, statistik och repriser sparas i mobilen, så att du kan jämföra körningar och se om ändringen i inställningarna faktiskt hjälpte. Inget konto, ingen reklam, och inget lämnar mobilen om du inte delar det själv."],
        },
        "specs": [
            ({"en": "Platform", "sv": "Plattform"}, {"en": "Android first, iOS later", "sv": "Android först, iOS senare"}),
            ({"en": "Status", "sv": "Status"}, {"en": "In development (v0.3)", "sv": "Under utveckling (v0.3)"}),
            ({"en": "Price", "sv": "Pris"}, {"en": "To be announced", "sv": "Meddelas senare"}),
        ],
        "features": [
            ({"en": "Camera finish line", "sv": "Mållinje med kameran"}, {"en": "Photograph each car once. The phone watches the line and knows who crossed it.", "sv": "Fotografera varje bil en gång. Mobilen bevakar linjen och vet vem som passerade."}),
            ({"en": "Lap times as you drive", "sv": "Varvtider medan du kör"}, {"en": "See each lap and your best lap while the session runs.", "sv": "Se varje varv och ditt bästa varv medan passet pågår."}),
            ({"en": "Stats and replays", "sv": "Statistik och repriser"}, {"en": "Compare runs over time and replay each finish-line crossing. Everything stays on your phone.", "sv": "Jämför körningar över tid och se repris på varje passering. Allt stannar i mobilen."}),
        ],
        "shots": [],
        "cta": [
            ({"en": "Get notified", "sv": "Få besked vid släpp"}, "https://www.instagram.com/viccom_games/", "btn ghost"),
        ],
        "note": None,
    },
    {
        "key": "psst", "name": "Psst", "kind": "app", "status": "test", "meter": 55,
        "accent": "#D9DADF",
        "art": None,
        "icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8a6 6 0 1 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/></svg>',
        "type":    {"en": "App", "sv": "App"},
        "badge":   {"en": "Closed test on Android · Launching December", "sv": "Stängt test på Android · Släpps i december"},
        "tagline": {"en": "One tap. Everyone knows.", "sv": "Ett tryck. Alla vet."},
        "alt":     {"en": "", "sv": ""},
        "short":   {"en": "Send an alert to everyone in your group with one tap, straight from a home-screen widget. For the moments when a chat thread is too slow: the boss is on the floor, coffee's ready, table 12 is waiting.",
                    "sv": "Skicka en signal till alla i gruppen med ett tryck, direkt från en widget på hemskärmen. För de gånger en chattråd är för långsam: chefen är på golvet, kaffet är klart, bord 12 väntar."},
        "body": {
            "en": ["Psst sends an alert to everyone in your group with a single tap. Put the widget on your home screen and you don't even need to open the app. The alert lands on every phone in about a second, with its own sound, so people know what it means without looking.",
                   "It's built for teams and groups that need each other's attention right now: a coffee break, a customer at the desk, time to leave. Write your own buttons, give them an emoji and a sound, and let one fire on its own at 15:00 every weekday.",
                   "Psst is free with 3 buttons and one group. Psst+ gives you 8 buttons, as many groups as you like and AI voices that read the alert out loud."],
            "sv": ["Psst skickar en signal till alla i gruppen med ett enda tryck. Lägg widgeten på hemskärmen så behöver du inte ens öppna appen. Signalen landar i allas mobiler på ungefär en sekund, med sitt eget ljud, så alla vet vad den betyder utan att titta.",
                   "Den är byggd för team och grupper som behöver varandras uppmärksamhet direkt: fikapaus, kund i disken, dags att gå. Skriv dina egna knappar, ge dem en emoji och ett ljud, och låt en gå av själv klockan 15:00 varje vardag.",
                   "Psst är gratis med 3 knappar och en grupp. Psst+ ger dig 8 knappar, hur många grupper du vill och AI-röster som läser upp signalen."],
        },
        "specs": [
            ({"en": "Platform", "sv": "Plattform"}, {"en": "Android on Google Play. iPhone later.", "sv": "Android via Google Play. iPhone senare."}),
            ({"en": "Status", "sv": "Status"}, {"en": "Closed test on Google Play", "sv": "Stängt test på Google Play"}),
            ({"en": "Launch", "sv": "Släpp"}, {"en": "December 2026", "sv": "December 2026"}),
            ({"en": "Price", "sv": "Pris"}, {"en": "Free. Psst+ is an optional upgrade.", "sv": "Gratis. Psst+ är ett valfritt tillägg."}),
            ({"en": "Languages", "sv": "Språk"}, {"en": "22, including English and Swedish", "sv": "22, bland annat svenska och engelska"}),
        ],
        "features": [
            ({"en": "One-tap alerts", "sv": "Signal med ett tryck"}, {"en": "No typing, no thread. One tap reaches the whole group in about a second.", "sv": "Inget skrivande, ingen tråd. Ett tryck når hela gruppen på ungefär en sekund."}),
            ({"en": "Home-screen widget", "sv": "Widget på hemskärmen"}, {"en": "Send from the widget without opening the app.", "sv": "Skicka från widgeten utan att öppna appen."}),
            ({"en": "Your buttons, your words", "sv": "Dina knappar, dina ord"}, {"en": "Write the text, pick an emoji, a colour and a sound. Everyone in the group gets the same buttons.", "sv": "Skriv texten, välj emoji, färg och ljud. Alla i gruppen får samma knappar."}),
            ({"en": "Join with a code", "sv": "Gå med via en kod"}, {"en": "A 4-character code or a QR code, valid for 10 minutes. Everyone sees who's in the group.", "sv": "En kod på 4 tecken eller en QR-kod som gäller i 10 minuter. Alla ser vem som är med i gruppen."}),
            ({"en": "Scheduled buttons", "sv": "Schemalagda knappar"}, {"en": "Coffee break at 15:00, Monday to Friday, sends itself.", "sv": "Fika klockan 15:00, måndag till fredag, skickas av sig själv."}),
            ({"en": "Sounds and voices", "sv": "Ljud och röster"}, {"en": "Ding, horn, alarm or pop. Add a robot voice, or with Psst+ an AI voice or your own recording.", "sv": "Pling, tuta, alarm eller pop. Lägg till en robotröst, eller med Psst+ en AI-röst eller en egen inspelning."}),
            ({"en": "Psst+", "sv": "Psst+"}, {"en": "8 buttons, unlimited groups and AI voices. Monthly, yearly or once for life.", "sv": "8 knappar, obegränsat med grupper och AI-röster. Per månad, per år eller en gång för alltid."}),
        ],
        "shots": [],
        "cta": [
            ({"en": "Follow the launch", "sv": "Följ släppet"}, "https://www.instagram.com/viccom_games/", "btn ghost"),
        ],
        "note": {"en": "The Google Play link goes here at launch. Psst is in closed testing with a crew of Android users right now.",
                 "sv": "Länken till Google Play hamnar här vid släppet. Psst testas just nu i ett stängt test med ett gäng Android-användare."},
    },
]
BY_KEY = {p["key"]: p for p in PRODUCTS}

SOCIAL = [
    ("Instagram", "https://www.instagram.com/viccom_games/"),
    ("X", "https://x.com/VICCOM_Games"),
    ("TikTok", "https://www.tiktok.com/@viccom_games"),
    ("Twitch", "https://www.twitch.tv/viccom_games"),
    ("GitHub", "https://github.com/VICCOM-devs"),
]

def esc(s):
    return html.escape(s, quote=True)

# ---------------------------------------------------------------- ramverk
def head(lang, key, title, desc, og_image="/ww-feature-1024x500.png", noindex=False):
    alt_lang = "sv" if lang == "en" else "en"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <meta name="theme-color" content="#121311">
  {'<meta name="robots" content="noindex">' if noindex else ''}
  <link rel="canonical" href="{SITE}{url(key, lang)}">
  <link rel="alternate" hreflang="en" href="{SITE}{url(key, 'en')}">
  <link rel="alternate" hreflang="sv" href="{SITE}{url(key, 'sv')}">
  <link rel="alternate" hreflang="x-default" href="{SITE}{url(key, 'en')}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{SITE}{url(key, lang)}">
  <meta property="og:image" content="{SITE}{og_image}">
  <meta property="og:locale" content="{'en_GB' if lang == 'en' else 'sv_SE'}">
  <meta property="og:locale:alternate" content="{'sv_SE' if lang == 'en' else 'en_GB'}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="preload" href="/unbounded.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/style.css?v={CSS_V}">
</head>
<body>
  <a class="skip" href="#innehall">{L(lang, 'Skip to content', 'Hoppa till innehållet')}</a>
"""

def header(lang, key, active=None):
    home = url("home", lang)
    items = [
        ("games", L(lang, "Games", "Spel"), home + "#games"),
        ("apps", L(lang, "Apps", "Appar"), home + "#apps"),
        ("about", L(lang, "About", "Om"), home + "#about"),
        ("contact", L(lang, "Contact", "Kontakt"), home + "#contact"),
        ("press", L(lang, "Press", "Press"), url("press", lang)),
    ]
    lis = "\n".join(
        f'            <li><a href="{h}"{" aria-current=\"page\"" if k == active else ""}>{t}</a></li>'
        for k, t, h in items)
    other = "sv" if lang == "en" else "en"
    sw_label = L(lang, "Svenska", "English")
    sw_short = L(lang, "SV", "EN")
    return f"""
  <header class="site-header">
    <div class="wrap">
      <a class="brand" href="{home}" aria-label="{L(lang, 'VICCOM, home', 'VICCOM, till startsidan')}">
        <img src="/viccom-mark-frost.svg" alt="" width="34" height="34">
        <span>VICCOM</span>
      </a>
      <nav class="site-nav" aria-label="{L(lang, 'Main menu', 'Huvudmeny')}">
        <ul>
{lis}
            <li class="lang"><a href="{url(key, other)}" hreflang="{other}" lang="{other}" title="{sw_label}" aria-label="{sw_label}"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/></svg>{sw_short}</a></li>
        </ul>
      </nav>
    </div>
  </header>
"""

def footer(lang, key):
    soc = "\n".join(f'          <li><a href="{h}">{t}</a></li>' for t, h in SOCIAL)
    prods = "\n".join(
        f'          <li><a href="{url(p["key"], lang)}"{" aria-current=\"page\"" if p["key"] == key else ""}>{p["name"]}</a></li>'
        for p in PRODUCTS)
    more = [("press", L(lang, "Press kit", "Presskit")), ("privacy", L(lang, "Privacy policy", "Integritetspolicy")),
            ("delete", L(lang, "Delete account", "Radera konto"))]
    mores = "\n".join(
        f'          <li><a href="{url(k, lang)}"{" aria-current=\"page\"" if k == key else ""}>{t}</a></li>'
        for k, t in more)
    other = "sv" if lang == "en" else "en"
    return f"""
  <footer class="site-footer">
    <div class="wrap">
      <div class="foot-brand">
        <img class="foot-wordmark" src="/viccom-wordmark-frost.svg" alt="VICCOM" width="260" height="40">
        <small>© 2026 VICCOM. {L(lang, 'Made in Sweden.', 'Gjort i Sverige.')}</small>
        <small><a href="{url(key, other)}" hreflang="{other}" lang="{other}">{L(lang, 'På svenska', 'In English')}</a></small>
      </div>
      <div>
        <h2>{L(lang, 'Products', 'Produkter')}</h2>
        <ul>
{prods}
        </ul>
      </div>
      <div>
        <h2>{L(lang, 'Follow', 'Följ oss')}</h2>
        <ul>
{soc}
        </ul>
      </div>
      <div>
        <h2>{L(lang, 'More', 'Mer')}</h2>
        <ul>
{mores}
          <li><a href="mailto:info@viccom.se">info@viccom.se</a></li>
        </ul>
      </div>
    </div>
  </footer>
"""

def end(scripts=""):
    return f"{scripts}</body>\n</html>\n"

def dot(status):
    return '<i class="dot live" aria-hidden="true"></i>' if status in ("live", "test") else '<i class="dot" aria-hidden="true"></i>'

def specs_html(p, lang):
    return "\n".join(f'              <li><span>{a[lang]}</span><b>{b[lang]}</b></li>' for a, b in p["specs"])

def cta_html(p, lang):
    return "\n".join(f'                <a class="{c}" href="{h}">{t[lang]}</a>' for t, h, c in p["cta"])

def art_html(p, lang, frost=False, eager=False):
    tag = f'<span class="tag">{dot(p["status"])}{p["badge"][lang]}</span>'
    if p["art"]:
        canvas = '\n            <canvas aria-hidden="true"></canvas>' if frost else ""
        return f"""<div class="feature-art"{' data-frost' if frost else ''}>
            {tag}
            <img src="{p['art']}" alt="{esc(p['alt'][lang])}" width="1024" height="500" loading="{'eager' if eager else 'lazy'}">{canvas}
          </div>"""
    return f"""<div class="feature-art icon-art" style="--p:{p['accent']}">
            {tag}
            <div class="icon-art-inner" aria-hidden="true"><div class="icon-big">{p['icon']}</div></div>
          </div>"""

# ---------------------------------------------------------------- startsida
def page_home(lang):
    k = "home"
    out = head(lang, k, "VICCOM",
               L(lang, "VICCOM is a one-person game and app studio in Sweden. Wobble Wheels launches on Google Play in November; Wyrmwind, AnyLap and Psst are on the way.",
                 "VICCOM är en enmansstudio för spel och appar i Sverige. Wobble Wheels släpps på Google Play i november, och Wyrmwind, AnyLap och Psst är på gång."))
    rows = []
    for p in PRODUCTS:
        rows.append(f"""              <tr>
                <td><a href="{url(p['key'], lang)}">{p['name']}</a></td>
                <td class="type">{p['type'][lang]}</td>
                <td><span class="status">{dot(p['status'])}{p['badge'][lang]}</span></td>
                <td class="meter-cell"><div class="meter" role="img" aria-label="{L(lang, 'Progress', 'Framsteg')} {p['meter']}%"><i style="width:{p['meter']}%;--p:{p['accent']}"></i></div></td>
              </tr>""")
    rows = "\n".join(rows)

    games = []
    for i, p in enumerate([x for x in PRODUCTS if x["kind"] == "game"]):
        frost = p["key"] == "ww"
        shots = ""
        if p["shots"]:
            pick = [p["shots"][j] for j in (1, 2, 4, 5, 6)]
            shots = '\n          <ul class="shots" aria-label="' + L(lang, f'Screenshots from {p["name"]}', f'Skärmbilder från {p["name"]}') + '">\n' + "\n".join(
                f'            <li><img src="{s}" alt="{esc(a[lang])}" width="720" height="1280" loading="lazy"></li>' for s, a in pick) + "\n          </ul>"
        hint = ""
        if frost:
            hint = f'\n          <p class="window-hint">{L(lang, "Drag across the picture to wipe off the frost.", "Dra över bilden för att torka bort frosten.")} <button class="linklike" type="button" data-frost-clear>{L(lang, "Wipe it all", "Torka hela rutan")}</button></p>'
        more = f'\n                <a class="btn ghost" href="{url(p["key"], lang)}">{L(lang, "More about " + p["name"], "Mer om " + p["name"])}</a>'
        games.append(f"""
        <article class="feature" aria-labelledby="h-{p['key']}">
          {art_html(p, lang, frost=frost, eager=(i == 0))}{hint}
          <div class="feature-body">
            <div>
              <h3 id="h-{p['key']}">{p['name']}</h3>
              <p class="tagline">{p['tagline'][lang]}</p>
              <p>{p['short'][lang]}</p>
              <div class="actions">
{cta_html(p, lang).split(chr(10))[0]}{more}
              </div>
            </div>
            <ul class="specs">
{specs_html(p, lang)}
            </ul>
          </div>{shots}
        </article>""")
    games = "".join(games)

    apps = []
    for p in [x for x in PRODUCTS if x["kind"] == "app"]:
        apps.append(f"""
          <a class="card" href="{url(p['key'], lang)}" style="--p:{p['accent']}">
            <div class="icon" aria-hidden="true">{p['icon']}</div>
            <span class="status">{dot(p['status'])}{p['badge'][lang]}</span>
            <h3>{p['name']}</h3>
            <p class="kind">{p['tagline'][lang]}</p>
            <p>{p['short'][lang]}</p>
            <span class="more">{L(lang, 'Read more', 'Läs mer')}</span>
          </a>""")
    apps = "".join(apps)

    out += f"""
  <div class="grid-bg">{header(lang, k)}
    <section class="hero" id="innehall">
      <div class="wrap">
        <h1>VICCOM</h1>
        <p class="lede">{L(lang, 'Games and apps from a one-person studio in Sweden. Two games and two apps in the pipeline, first launch in November.', 'Spel och appar från en enmansstudio i Sverige. Två spel och två appar på gång, första släppet i november.')}</p>

        <div class="board" aria-labelledby="board-title">
          <div class="board-head">
            <strong id="board-title">{L(lang, 'In the pipeline', 'I pipelinen')}</strong>
            <span>{L(lang, 'Updated October 2026', 'Uppdaterad oktober 2026')}</span>
          </div>
          <table>
            <thead>
              <tr><th scope="col">{L(lang, 'Project', 'Projekt')}</th><th scope="col">{L(lang, 'Type', 'Typ')}</th><th scope="col">Status</th><th scope="col">{L(lang, 'Progress', 'Framsteg')}</th></tr>
            </thead>
            <tbody>
{rows}
            </tbody>
          </table>
        </div>
      </div>
    </section>
  </div>

  <main>
    <section class="section" id="games" aria-labelledby="games-h">
      <div class="wrap">
        <div class="section-head">
          <h2 id="games-h">{L(lang, 'Games', 'Spel')}</h2>
          <p>{L(lang, 'One almost out the door, one in the workshop.', 'Ett nästan klart, ett i verkstaden.')}</p>
        </div>{games}
      </div>
    </section>

    <section class="section" id="apps" aria-labelledby="apps-h">
      <div class="wrap">
        <div class="section-head">
          <h2 id="apps-h">{L(lang, 'Apps', 'Appar')}</h2>
          <p>{L(lang, 'Tools we build because we wanted them ourselves.', 'Verktyg vi bygger för att vi själva ville ha dem.')}</p>
        </div>
        <div class="cards">{apps}
        </div>
      </div>
    </section>

    <section class="section" id="about" aria-labelledby="about-h">
      <div class="wrap split">
        <h2 id="about-h">{L(lang, 'About VICCOM', 'Om VICCOM')}</h2>
        <div class="prose">
          <p>{L(lang, 'VICCOM started in 2026 as a one-person studio in Sweden, run by Victor Immonen. We make games for mobile and desktop, and apps for things we were missing ourselves. Clear design, things worth coming back to, and no pay to win.', 'VICCOM startade 2026 som en enmansstudio i Sverige, driven av Victor Immonen. Vi gör spel för mobil och dator, och appar för sådant vi själva saknade. Tydlig design, saker som är värda att komma tillbaka till, och inget pay to win.')}</p>
          <p>{L(lang, 'We share the work along the way: sketches, prototypes and ideas that didn\'t make it. Most of it shows up on Instagram and TikTok first.', 'Vi visar arbetet på vägen: skisser, prototyper och idéer som inte höll. Det mesta hamnar först på Instagram och TikTok.')}</p>
        </div>
      </div>
    </section>

    <section class="section" id="contact" aria-labelledby="contact-h">
      <div class="wrap split">
        <h2 id="contact-h">{L(lang, 'Contact', 'Kontakt')}</h2>
        <ul class="contact">
          <li><a href="mailto:info@viccom.se">info@viccom.se</a><span>{L(lang, 'General questions, partnerships and press', 'Allmänna frågor, samarbeten och press')}</span></li>
          <li><a href="mailto:support@viccom.se">support@viccom.se</a><span>{L(lang, 'Help with any of our games or apps', 'Hjälp med något av våra spel eller appar')}</span></li>
          <li><a href="mailto:order@viccom.se">order@viccom.se</a><span>{L(lang, 'Orders, receipts and invoices', 'Beställningar, kvitton och fakturor')}</span></li>
          <li><a href="mailto:vic@viccom.se">vic@viccom.se</a><span>{L(lang, 'Straight to the founder', 'Direkt till grundaren')}</span></li>
        </ul>
      </div>
    </section>
  </main>
{footer(lang, k)}"""
    out += end(f'  <script src="/frost.js?v={CSS_V}" defer></script>\n')
    return out

# ---------------------------------------------------------------- produktsida
def page_product(lang, p):
    k = p["key"]
    out = head(lang, k, f"{p['name']} – VICCOM", f"{p['name']}: {p['tagline'][lang]} {p['short'][lang]}",
               og_image=p.get("art_png") or "/og.png")
    body = "\n".join(f"            <p>{t}</p>" for t in p["body"][lang])
    note = f'\n        <p class="window-hint">{p["note"][lang]}</p>' if p.get("note") else ""
    feats = ""
    if p["features"]:
        lis = "\n".join(f"          <li><b>{a[lang]}</b><span>{b[lang]}</span></li>" for a, b in p["features"])
        feats = f"""
    <section class="section" aria-labelledby="feat-h">
      <div class="wrap">
        <div class="section-head"><h2 id="feat-h">{L(lang, 'How it works', 'Så fungerar det')}</h2></div>
        <ul class="features" style="--p:{p['accent']}">
{lis}
        </ul>
      </div>
    </section>"""
    shots = ""
    if p["shots"]:
        lis = "\n".join(f'          <li><img src="{s}" alt="{esc(a[lang])}" width="720" height="1280" loading="lazy"></li>' for s, a in p["shots"])
        shots = f"""
    <section class="section" aria-labelledby="shots-h">
      <div class="wrap">
        <div class="section-head"><h2 id="shots-h">{L(lang, 'Screenshots', 'Skärmbilder')}</h2></div>
        <ul class="shots shots-full">
{lis}
        </ul>
      </div>
    </section>"""
    help_ = f"""
    <section class="section" aria-labelledby="help-h">
      <div class="wrap split">
        <h2 id="help-h">{L(lang, 'Help and terms', 'Hjälp och villkor')}</h2>
        <div class="prose">
          <p>{L(lang, f'Need help with {p["name"]}? Email', f'Behöver du hjälp med {p["name"]}? Mejla')} <a href="mailto:support@viccom.se">support@viccom.se</a>.</p>
          <p>{L(lang, 'How we handle your data is in our', 'Hur vi hanterar dina uppgifter står i vår')} <a href="{url('privacy', lang)}">{L(lang, 'privacy policy', 'integritetspolicy')}</a>. {L(lang, 'To remove your account, see', 'Vill du ta bort ditt konto, se')} <a href="{url('delete', lang)}">{L(lang, 'Delete account', 'Radera konto')}</a>.</p>
          <p>{L(lang, 'Press and creators can find logos, art and copy in the', 'Press och skapare hittar logotyper, bilder och texter i')} <a href="{url('press', lang)}">{L(lang, 'press kit', 'presskitet')}</a>.</p>
        </div>
      </div>
    </section>"""
    out += f"""
  <div class="grid-bg" style="--p:{p['accent']}">{header(lang, k, 'games' if p['kind'] == 'game' else 'apps')}
    <section class="product-hero" id="innehall">
      <div class="wrap">
        {art_html(p, lang, eager=True)}
        <h1>{p['name']}</h1>
        <p class="tagline">{p['tagline'][lang]}</p>
        <div class="actions">
{cta_html(p, lang)}
        </div>{note}
      </div>
    </section>
  </div>

  <main>
    <section class="section">
      <div class="wrap">
        <div class="feature-body">
          <div class="prose">
{body}
          </div>
          <ul class="specs">
{specs_html(p, lang)}
            <li><span>{L(lang, 'Developer', 'Utvecklare')}</span><b>VICCOM</b></li>
          </ul>
        </div>
      </div>
    </section>{feats}{shots}{help_}
  </main>
{footer(lang, k)}"""
    return out + end()

# ---------------------------------------------------------------- dokumentsidor
def doc_page(lang, key, title, desc, lede, toc, body, active=None):
    toc_html = "\n".join(f'            <li><a href="#{a}">{t}</a></li>' for a, t in toc)
    out = head(lang, key, f"{title} – VICCOM", desc)
    out += f"""
  <div class="grid-bg">{header(lang, key, active)}</div>

  <main id="innehall">
    <div class="wrap">
      <header class="page-head">
        <h1>{title}</h1>
        <p>{lede}</p>
      </header>

      <div class="doc">
        <nav class="toc" aria-label="{L(lang, 'Contents', 'Innehåll')}">
          <h2>{L(lang, 'Contents', 'Innehåll')}</h2>
          <ol>
{toc_html}
          </ol>
        </nav>

        <article class="doc-body">
{body}
        </article>
      </div>
    </div>
  </main>
{footer(lang, key)}"""
    return out + end()

def page_privacy(lang):
    E = lang == "en"
    toc = [("who", L(lang, "Who is responsible", "Vem som ansvarar")),
           ("website", L(lang, "This website", "Webbplatsen")),
           ("email", L(lang, "When you email us", "När du mejlar oss")),
           ("products", L(lang, "Our games and apps", "Våra spel och appar")),
           ("signin", L(lang, "Accounts and sign-in", "Konto och inloggning")),
           ("children", L(lang, "Children", "Barn")),
           ("providers", L(lang, "Service providers", "Leverantörer")),
           ("rights", L(lang, "Your rights", "Dina rättigheter")),
           ("changes", L(lang, "Changes", "Ändringar"))]
    if E:
        body = f"""          <h2 id="who">Who is responsible</h2>
          <p>VICCOM is a sole proprietorship run by Victor Immonen in Sweden, and is the data controller for everything described here. Contact us at <a href="mailto:info@viccom.se">info@viccom.se</a>.</p>
          <p>We're a small studio and only collect what a feature actually needs. We never sell personal data.</p>

          <h2 id="website">This website</h2>
          <p>viccom.se uses no cookies, no analytics and no tracking. Fonts are hosted on our own site, so visiting it sends nothing to third parties.</p>
          <p>The site is hosted on GitHub Pages. GitHub logs technical data such as IP addresses to keep the service running and secure. The browser version of Wobble Wheels at viccom.se/play is covered under Wobble Wheels below.</p>

          <h2 id="email">When you email us</h2>
          <p>If you write to one of our addresses, we keep your name, email address and message so we can answer and help you. Email runs on Google Workspace.</p>
          <ul>
            <li><strong>Support and general questions</strong> are kept for up to 24 months after our last contact. Legal basis: legitimate interest, or contract if it concerns something you bought.</li>
            <li><strong>Orders and receipts</strong> are kept for seven years, because Swedish bookkeeping law requires it.</li>
          </ul>

          <h2 id="products">Our games and apps</h2>
          <p>Store purchases and downloads through Google Play, the App Store, Steam or itch.io are handled by the store, which is responsible for its own data, such as payment details. We don't receive your payment details.</p>
          <p>None of our products use third-party analytics. Psst shows optional rewarded ads (see below); the others show no ads.</p>

          <h3>Wobble Wheels</h3>
          <p>When you start the game, you get a guest account automatically, so your progress and online races work without signing up. We store a player ID, the display name you choose, your progress, garage and settings, and your race results, records and leaderboard placings. Your display name and results are visible to other players on leaderboards and in live races. You can link the guest account to Google to keep it across devices.</p>
          <p>Data is stored with Supabase in Ireland (EU). The browser version also keeps some settings in your browser's local storage. Legal basis: contract, to deliver the game and its online features.</p>

          <h3>Wyrmwind</h3>
          <p>Wyrmwind is a prototype and doesn't collect any personal data. We'll update this section before it does.</p>

          <h3>AnyLap</h3>
          <p>AnyLap is a lap timer that uses your phone's camera. It needs the camera permission to see racers cross the finish line. The video is processed on your phone and is never sent to us or anyone else.</p>
          <ul>
            <li><strong>No account and no sign-in.</strong> AnyLap has no internet connection and sends no data to any server.</li>
            <li><strong>What it saves stays on your phone:</strong> racer names, car photos and colour calibration, lap times, stats and replays of finish-line crossings. Delete them by removing racers and sessions in the app, or by uninstalling it.</li>
            <li><strong>Sharing only when you choose.</strong> If you share results or a video, it goes through your phone's normal share menu to the app you pick.</li>
            <li><strong>No ads, no analytics and no tracking.</strong></li>
          </ul>
          <p>If AnyLap later gets accounts or cloud sync, we update this section before that version is released.</p>

          <h3>Psst</h3>
          <p>Psst creates an anonymous account on your phone the first time you open it, so no sign-up, email or password is needed. The account is what connects you to your groups.</p>
          <ul>
            <li><strong>What we store:</strong> an anonymous user ID, the display name you choose, the groups you're in, the buttons in those groups (emoji, text and settings written by group members), the alerts sent in them and who has seen them, and a push token for your device. Alerts are deleted after 7 days.</li>
            <li><strong>Who sees it:</strong> your display name, the buttons and the alerts are visible to the other members of your group, and only to them. Invite codes expire after 10 minutes, and the group owner can remove members.</li>
            <li><strong>Voice clips:</strong> if a group uses the robot voice, the clip is generated on your phone. Psst+ AI voices and recorded clips are stored with Supabase and downloaded to every phone in the group. AI voices are generated from the button text with Google Cloud Text-to-Speech.</li>
            <li><strong>Delivery:</strong> alerts travel through Expo's push service and Google Firebase Cloud Messaging (Apple Push Notification service on iPhone).</li>
            <li><strong>Rewarded ads:</strong> free users can watch an optional video ad in exchange for extra button edits. Ads are served by Google AdMob, which receives your advertising ID, approximate location and device information. You choose when to watch one; ads never appear when sending or receiving alerts. On iPhone, Psst asks for permission before personalised ads.</li>
            <li><strong>Psst+ purchases:</strong> subscriptions and the lifetime purchase go through Google Play or the App Store and are managed by RevenueCat, which stores a purchase record linked to your anonymous ID so we can unlock Psst+. We never see your payment details.</li>
          </ul>
          <p>Data is stored with Supabase in Stockholm (EU). Legal basis: contract for groups and alerts, consent for rewarded ads. Uninstalling Psst doesn't delete the account; see <a href="{url('delete', lang)}">Delete account</a>.</p>

          <h2 id="signin">Accounts and sign-in</h2>
          <p>Some products let you sign in with Google or Apple. We then receive a user ID and, if you allow it, your email address and name. If you hide your email when signing in with Apple, we only get Apple's forwarding address. We never receive your password.</p>
          <p>You can delete your account at any time, in the app or by email. See <a href="{url('delete', lang)}">Delete account</a> for how, and what gets deleted.</p>

          <h2 id="children">Children</h2>
          <p>We don't knowingly collect personal data from children under 13. If you're a parent and think your child has given us personal data, contact us and we'll delete it.</p>

          <h2 id="providers">Service providers</h2>
          <p>We use a small number of providers that process data on our behalf:</p>
          <ul>
            <li><strong>Supabase</strong> for databases and accounts, in Ireland and Stockholm (EU).</li>
            <li><strong>Google Workspace</strong> for email.</li>
            <li><strong>GitHub Pages</strong> for hosting this website.</li>
            <li><strong>Expo</strong> and <strong>Google Firebase</strong> for push notifications in Psst.</li>
            <li><strong>Google AdMob</strong> for rewarded ads in Psst, <strong>RevenueCat</strong> for Psst+ purchases, and <strong>Google Cloud Text-to-Speech</strong> for Psst+ AI voices.</li>
            <li><strong>Google</strong> and <strong>Apple</strong> for sign-in, if you choose to use them.</li>
          </ul>
          <p>Some are US companies. Transfers outside the EU/EEA rely on the EU–US Data Privacy Framework or the European Commission's standard contractual clauses.</p>

          <h2 id="rights">Your rights</h2>
          <p>Under the GDPR you have the right to:</p>
          <ul>
            <li>know what data we hold about you and get a copy,</li>
            <li>have incorrect data corrected,</li>
            <li>have your data deleted, unless the law requires us to keep it,</li>
            <li>restrict or object to how we use it,</li>
            <li>get data you gave us in a machine-readable format.</li>
          </ul>
          <p>To delete an account, follow <a href="{url('delete', lang)}">Delete account</a>. For anything else, email <a href="mailto:info@viccom.se">info@viccom.se</a> and we'll answer within a month. If you're unhappy with how we handle your data, you can complain to the Swedish Authority for Privacy Protection, <a href="https://www.imy.se/en/">imy.se</a>.</p>

          <h2 id="changes">Changes</h2>
          <p>We update this policy when we change how we handle data, for example when a product launches or gets a new feature. The date at the top shows the latest change.</p>"""
        lede = "Last updated 29 October 2026. What personal data we handle in our website, games and apps, why, and what rights you have."
        desc = "How VICCOM handles personal data on viccom.se and in Wobble Wheels, Wyrmwind, AnyLap and Psst."
        title = "Privacy policy"
    else:
        body = f"""          <h2 id="who">Vem som ansvarar</h2>
          <p>VICCOM är en enskild näringsverksamhet som drivs av Victor Immonen i Sverige, och är personuppgiftsansvarig för allt som beskrivs här. Du når oss på <a href="mailto:info@viccom.se">info@viccom.se</a>.</p>
          <p>Vi är en liten studio och samlar bara in det en funktion faktiskt behöver. Vi säljer aldrig personuppgifter.</p>

          <h2 id="website">Webbplatsen</h2>
          <p>viccom.se använder inga kakor (cookies), ingen analys och ingen spårning. Typsnitten ligger på vår egen sajt, så ett besök skickar inget till tredje part.</p>
          <p>Sajten ligger på GitHub Pages. GitHub sparar tekniska loggar, till exempel IP-adresser, för drift och säkerhet. Webbversionen av Wobble Wheels på viccom.se/play beskrivs under Wobble Wheels nedan.</p>

          <h2 id="email">När du mejlar oss</h2>
          <p>Om du skriver till någon av våra adresser sparar vi ditt namn, din e-postadress och det du skriver, så att vi kan svara och hjälpa dig. E-posten hanteras av Google Workspace.</p>
          <ul>
            <li><strong>Supportärenden och allmänna frågor</strong> sparas i upp till 24 månader efter senaste kontakten. Rättslig grund är berättigat intresse, eller avtal om ärendet gäller något du köpt.</li>
            <li><strong>Beställningar och kvitton</strong> sparas i sju år, eftersom bokföringslagen kräver det.</li>
          </ul>

          <h2 id="products">Våra spel och appar</h2>
          <p>Köp och nedladdningar via Google Play, App Store, Steam eller itch.io hanteras av butiken, som ansvarar för sina egna uppgifter, till exempel betalning. Vi får aldrig dina betaluppgifter.</p>
          <p>Ingen av våra produkter använder analys från tredje part. Psst visar frivilliga belöningsannonser (se nedan); de andra visar ingen reklam.</p>

          <h3>Wobble Wheels</h3>
          <p>När du startar spelet får du automatiskt ett gästkonto, så att framsteg och online-lopp fungerar utan registrering. Vi sparar ett spelar-id, det visningsnamn du väljer, dina framsteg, ditt garage och dina inställningar samt dina lopp, rekord och placeringar på topplistor. Visningsnamn och resultat syns för andra spelare på topplistor och i live-lopp. Du kan koppla gästkontot till Google för att behålla det mellan enheter.</p>
          <p>Uppgifterna lagras hos Supabase i Irland (EU). Webbversionen sparar också vissa inställningar i webbläsarens lokala lagring. Rättslig grund är avtal, alltså att kunna leverera spelet och dess onlinefunktioner.</p>

          <h3>Wyrmwind</h3>
          <p>Wyrmwind är en prototyp och samlar inte in några personuppgifter. Vi uppdaterar det här avsnittet innan det ändras.</p>

          <h3>AnyLap</h3>
          <p>AnyLap är en varvräknare som använder mobilens kamera. Appen behöver kamerabehörighet för att se när förare passerar mållinjen. Kamerabilden behandlas direkt i mobilen och skickas aldrig till oss eller någon annan.</p>
          <ul>
            <li><strong>Inget konto och ingen inloggning.</strong> AnyLap har ingen internetanslutning och skickar inga uppgifter till någon server.</li>
            <li><strong>Det som sparas, sparas i mobilen:</strong> förarnamn, foton och färgkalibrering av bilar, varvtider, statistik och repriser av passeringar. Du raderar det genom att ta bort förare och pass i appen eller genom att avinstallera den.</li>
            <li><strong>Delning sker bara när du väljer det.</strong> Delar du resultat eller en video går den via mobilens vanliga delningsmeny till den app du väljer.</li>
            <li><strong>Ingen reklam, ingen analys och ingen spårning.</strong></li>
          </ul>
          <p>Om AnyLap senare får konton eller synkning i molnet uppdaterar vi det här avsnittet innan den versionen släpps.</p>

          <h3>Psst</h3>
          <p>Psst skapar ett anonymt konto i din mobil första gången du öppnar appen, så ingen registrering, e-post eller lösenord behövs. Kontot är det som kopplar dig till dina grupper.</p>
          <ul>
            <li><strong>Vad vi sparar:</strong> ett anonymt användar-id, det visningsnamn du väljer, grupperna du är med i, knapparna i grupperna (emoji, text och inställningar som medlemmarna skrivit), signalerna som skickats i dem och vem som sett dem, samt en push-token för din enhet. Signaler raderas efter 7 dagar.</li>
            <li><strong>Vem som ser det:</strong> ditt visningsnamn, knapparna och signalerna syns för de andra medlemmarna i din grupp, och bara för dem. Inbjudningskoder slutar gälla efter 10 minuter, och gruppens ägare kan ta bort medlemmar.</li>
            <li><strong>Röstklipp:</strong> om en grupp använder robotrösten skapas klippet i din mobil. AI-röster och inspelade klipp i Psst+ lagras hos Supabase och laddas ner till alla mobiler i gruppen. AI-rösterna skapas från knappens text med Google Cloud Text-to-Speech.</li>
            <li><strong>Leverans:</strong> signalerna skickas via Expos pushtjänst och Google Firebase Cloud Messaging (Apple Push Notification service på iPhone).</li>
            <li><strong>Belöningsannonser:</strong> den som använder gratisversionen kan välja att titta på en videoannons i utbyte mot fler knappändringar. Annonserna visas av Google AdMob, som får ditt annons-id, din ungefärliga plats och information om enheten. Du väljer själv när du tittar; annonser visas aldrig när signaler skickas eller tas emot. På iPhone frågar Psst om lov innan personliga annonser visas.</li>
            <li><strong>Köp av Psst+:</strong> prenumerationer och livstidsköpet går via Google Play eller App Store och hanteras av RevenueCat, som sparar ett köpkvitto kopplat till ditt anonyma id så att vi kan låsa upp Psst+. Vi ser aldrig dina betaluppgifter.</li>
          </ul>
          <p>Uppgifterna lagras hos Supabase i Stockholm (EU). Rättslig grund är avtal för grupper och signaler, samtycke för belöningsannonser. Att avinstallera Psst raderar inte kontot; se <a href="{url('delete', lang)}">Radera konto</a>.</p>

          <h2 id="signin">Konto och inloggning</h2>
          <p>Vissa produkter låter dig logga in med Google eller Apple. Då får vi ett användar-id och, om du godkänner det, din e-postadress och ditt namn. Väljer du att dölja din e-post vid inloggning med Apple får vi bara Apples vidarebefordringsadress. Vi får aldrig ditt lösenord.</p>
          <p>Du kan radera ditt konto när du vill, i appen eller via mejl. Hur du gör och vad som raderas står på sidan <a href="{url('delete', lang)}">Radera konto</a>.</p>

          <h2 id="children">Barn</h2>
          <p>Vi samlar inte medvetet in personuppgifter från barn under 13 år. Om du är förälder och tror att ditt barn har lämnat uppgifter till oss, kontakta oss så raderar vi dem.</p>

          <h2 id="providers">Leverantörer</h2>
          <p>Vi använder ett fåtal leverantörer som behandlar uppgifter för vår räkning:</p>
          <ul>
            <li><strong>Supabase</strong> för databaser och konton, i Irland och Stockholm (EU).</li>
            <li><strong>Google Workspace</strong> för e-post.</li>
            <li><strong>GitHub Pages</strong> för den här webbplatsen.</li>
            <li><strong>Expo</strong> och <strong>Google Firebase</strong> för pushnotiser i Psst.</li>
            <li><strong>Google AdMob</strong> för belöningsannonser i Psst, <strong>RevenueCat</strong> för köp av Psst+ och <strong>Google Cloud Text-to-Speech</strong> för AI-röster i Psst+.</li>
            <li><strong>Google</strong> och <strong>Apple</strong> för inloggning, om du väljer att använda dem.</li>
          </ul>
          <p>Vissa av dem är amerikanska företag. När uppgifter överförs utanför EU/EES sker det med stöd av EU:s och USA:s ramverk för dataskydd eller EU-kommissionens standardavtalsklausuler.</p>

          <h2 id="rights">Dina rättigheter</h2>
          <p>Enligt dataskyddsförordningen (GDPR) har du rätt att:</p>
          <ul>
            <li>få veta vilka uppgifter vi har om dig och få en kopia av dem,</li>
            <li>få felaktiga uppgifter rättade,</li>
            <li>få dina uppgifter raderade, om vi inte måste spara dem enligt lag,</li>
            <li>begränsa eller invända mot hur vi använder dem,</li>
            <li>få ut uppgifter du själv lämnat i ett maskinläsbart format.</li>
          </ul>
          <p>Vill du radera ett konto följer du stegen på <a href="{url('delete', lang)}">Radera konto</a>. För övriga frågor mejlar du <a href="mailto:info@viccom.se">info@viccom.se</a>, så svarar vi inom en månad. Är du inte nöjd med hur vi hanterar dina uppgifter kan du klaga hos Integritetsskyddsmyndigheten, <a href="https://www.imy.se">imy.se</a>.</p>

          <h2 id="changes">Ändringar</h2>
          <p>Vi uppdaterar policyn när vi ändrar hur vi hanterar uppgifter, till exempel när en produkt släpps eller får en ny funktion. Datumet högst upp visar när den senast ändrades.</p>"""
        lede = "Senast uppdaterad 29 oktober 2026. Vilka personuppgifter vi hanterar på webbplatsen och i våra spel och appar, varför, och vilka rättigheter du har."
        desc = "Hur VICCOM hanterar personuppgifter på viccom.se och i Wobble Wheels, Wyrmwind, AnyLap och Psst."
        title = "Integritetspolicy"
    return doc_page(lang, "privacy", title, desc, lede, toc, body)

def page_delete(lang):
    E = lang == "en"
    toc = [("in-app", L(lang, "Delete in the app", "Radera i appen")),
           ("by-email", L(lang, "Delete by email", "Radera via mejl")),
           ("deleted", L(lang, "What gets deleted", "Vad som raderas")),
           ("kept", L(lang, "What we keep", "Vad som sparas")),
           ("partial", L(lang, "Delete only some data", "Radera bara viss data"))]
    mail = "mailto:support@viccom.se?subject=" + ("Delete%20account" if E else "Radera%20konto")
    if E:
        body = f"""          <div class="note"><p>Developer: VICCOM. Applies to Wobble Wheels and Psst. Uninstalling an app does not delete your account. AnyLap has no account: everything it saves is on your phone, and you delete it by removing racers and sessions in the app or by uninstalling it.</p></div>

          <h2 id="in-app">Delete in the app</h2>
          <p><strong>Wobble Wheels</strong></p>
          <ol>
            <li>Open the game.</li>
            <li>Go to <strong>Settings</strong>, then <strong>Account</strong>.</li>
            <li>Tap <strong>Delete account</strong> and confirm.</li>
          </ol>
          <p><strong>Psst</strong></p>
          <ol>
            <li>Open Psst.</li>
            <li>Go to the <strong>Me</strong> tab.</li>
            <li>Tap <strong>Delete account</strong> at the bottom and confirm.</li>
          </ol>
          <p>The account is deleted straight away and you're signed out. Psst accounts are anonymous (no email or password), so the app on your phone is the only key to the account: delete it before you uninstall or switch phones.</p>

          <h2 id="by-email">Delete by email</h2>
          <p>If you no longer have the app, or can't get in, we can delete the account for you.</p>
          <ol>
            <li>Email <a href="{mail}">support@viccom.se</a> from the address linked to the account, if there is one.</li>
            <li>Put <strong>Delete account</strong> in the subject line.</li>
            <li>Tell us which game or app it's about and your display name. For Psst, also tell us the name of a group you're in, so we can find the right anonymous account.</li>
          </ol>
          <p>We confirm within 7 days and delete the account within 30 days. If we can't tell that the account is yours, we'll ask you to confirm, for example by deleting it in the app.</p>
          <p><a class="btn" href="{mail}">Email support about deletion</a></p>

          <h2 id="deleted">What gets deleted</h2>
          <ul>
            <li>Your user ID and any link to Google or Apple sign-in</li>
            <li>Email address and display name</li>
            <li>Progress, garage, settings and saves in the cloud</li>
            <li>Race results, records and leaderboard placings</li>
            <li>Psst: your anonymous ID, display name, push token, your memberships, the alerts you sent, your edit and voice counters, and your Psst+ status in our database. Groups you <em>own</em> are deleted too, with their buttons and voice clips, so the other members lose that group. If you want it to live on, hand it over by email first.</li>
          </ul>

          <h2 id="kept">What we keep</h2>
          <ul>
            <li><strong>Backups</strong> of the database may contain your data for up to 30 days after deletion. Then it's gone.</li>
            <li><strong>Emails to support</strong>, including the deletion request, are kept for up to 24 months so we can show the request was handled.</li>
            <li><strong>Purchases</strong> made through Google Play or the App Store are handled by the store and aren't affected. Purchases made directly from VICCOM are kept for seven years under Swedish bookkeeping law.</li>
          </ul>

          <h2 id="partial">Delete only some data</h2>
          <p>Want to keep the account but remove, say, your name from a leaderboard? Email <a href="mailto:support@viccom.se">support@viccom.se</a> and tell us what you want removed.</p>
          <p>More on how we handle personal data is in our <a href="{url('privacy', lang)}">privacy policy</a>.</p>"""
        title, lede = "Delete account", "How to delete your account in a VICCOM game or app, and what happens to your data."
        desc = "How to delete your VICCOM account in Wobble Wheels or Psst, and what happens to your data."
    else:
        body = f"""          <div class="note"><p>Utvecklare: VICCOM. Gäller Wobble Wheels och Psst. Att avinstallera en app raderar inte kontot. AnyLap har inget konto: allt appen sparar ligger i mobilen, och du raderar det genom att ta bort förare och pass i appen eller genom att avinstallera den.</p></div>

          <h2 id="in-app">Radera i appen</h2>
          <p><strong>Wobble Wheels</strong></p>
          <ol>
            <li>Öppna spelet.</li>
            <li>Gå till <strong>Settings</strong> (Inställningar) och sedan <strong>Account</strong> (Konto).</li>
            <li>Tryck på <strong>Delete account</strong> (Radera konto) och bekräfta.</li>
          </ol>
          <p><strong>Psst</strong></p>
          <ol>
            <li>Öppna Psst.</li>
            <li>Gå till fliken <strong>Me</strong> (Jag).</li>
            <li>Tryck på <strong>Delete account</strong> (Radera konto) längst ner och bekräfta.</li>
          </ol>
          <p>Kontot raderas direkt och du loggas ut. Konton i Psst är anonyma (ingen e-post eller lösenord), så appen i din mobil är den enda nyckeln till kontot: radera det innan du avinstallerar eller byter mobil.</p>

          <h2 id="by-email">Radera via mejl</h2>
          <p>Har du inte kvar appen, eller kommer du inte in, kan vi radera kontot åt dig.</p>
          <ol>
            <li>Mejla <a href="{mail}">support@viccom.se</a> från den adress som är kopplad till kontot, om det finns en.</li>
            <li>Skriv <strong>Radera konto</strong> i ämnesraden.</li>
            <li>Ange vilket spel eller vilken app det gäller och ditt visningsnamn. För Psst, skriv också namnet på en grupp du är med i, så att vi hittar rätt anonymt konto.</li>
          </ol>
          <p>Vi bekräftar inom 7 dagar och raderar kontot inom 30 dagar. Om vi inte kan se att kontot är ditt ber vi dig bekräfta det, till exempel genom att radera det i appen.</p>
          <p><a class="btn" href="{mail}">Mejla support om radering</a></p>

          <h2 id="deleted">Vad som raderas</h2>
          <ul>
            <li>Ditt användar-id och eventuell koppling till inloggning med Google eller Apple</li>
            <li>E-postadress och visningsnamn</li>
            <li>Framsteg, garage, inställningar och sparat i molnet</li>
            <li>Lopp, rekord och placeringar på topplistor</li>
            <li>Psst: ditt anonyma id, visningsnamn, push-token, dina medlemskap, signalerna du skickat, dina räknare för ändringar och röster, samt din Psst+-status i vår databas. Grupper du <em>äger</em> raderas också, med sina knappar och röstklipp, så de andra medlemmarna förlorar gruppen. Vill du att den ska leva vidare, lämna över den via mejl först.</li>
          </ul>

          <h2 id="kept">Vad som sparas</h2>
          <ul>
            <li><strong>Säkerhetskopior</strong> av databasen kan innehålla dina uppgifter i upp till 30 dagar efter raderingen. Därefter är de borta.</li>
            <li><strong>Mejl till support</strong>, inklusive själva raderingsbegäran, sparas i upp till 24 månader så att vi kan visa att begäran har hanterats.</li>
            <li><strong>Köp</strong> via Google Play eller App Store hanteras av butiken och påverkas inte. Köp gjorda direkt hos VICCOM sparas i sju år enligt bokföringslagen.</li>
          </ul>

          <h2 id="partial">Radera bara viss data</h2>
          <p>Vill du behålla kontot men ta bort till exempel ditt namn från en topplista? Mejla <a href="mailto:support@viccom.se">support@viccom.se</a> och skriv vad du vill ha bort.</p>
          <p>Mer om hur vi hanterar personuppgifter finns i vår <a href="{url('privacy', lang)}">integritetspolicy</a>.</p>"""
        title, lede = "Radera konto", "Så raderar du ditt konto i ett spel eller en app från VICCOM, och vad som händer med dina uppgifter."
        desc = "Så raderar du ditt VICCOM-konto i Wobble Wheels eller Psst, och vad som händer med dina uppgifter."
    return doc_page(lang, "delete", title, desc, lede, toc, body)

def page_press(lang):
    E = lang == "en"
    toc = [("facts", L(lang, "Facts", "Fakta")), ("about", L(lang, "About the studio", "Om studion")),
           ("products", L(lang, "Games and apps", "Spel och appar")), ("logos", L(lang, "Logos", "Logotyper")),
           ("colours", L(lang, "Colours and type", "Färger och typsnitt")), ("contact", L(lang, "Contact", "Kontakt"))]
    social = ",\n              ".join(f'<a href="{h}">{t}</a>' for t, h in SOCIAL[:4])
    prods = []
    for p in PRODUCTS:
        art = ""
        if p["art"]:
            extra = ""
            if p["key"] == "ww":
                extra = f"""
            <li>
              <div class="preview art"><img src="/ww-shot-3.webp" alt="" style="object-position: top"></div>
              <a href="/wobble-wheels-press.zip" download>{L(lang, 'Key art and 7 screenshots (zip)', 'Nyckelbild och 7 skärmbilder (zip)')}</a>
            </li>"""
            art = f"""
          <ul class="assets">
            <li>
              <div class="preview art"><img src="{p['art']}" alt="{L(lang, 'Key art for', 'Nyckelbild för')} {p['name']}"></div>
              <a href="{p.get('art_png')}" download>{L(lang, 'Key art, 1024×500 (PNG)', 'Nyckelbild, 1024×500 (PNG)')}</a>
            </li>{extra}
          </ul>"""
        facts = "\n".join(f"            <dt>{a[lang]}</dt><dd>{b[lang]}</dd>" for a, b in p["specs"])
        prods.append(f"""
          <h3>{p['name']}</h3>
          <p>{p['short'][lang]}</p>
          <dl class="facts">
{facts}
            <dt>{L(lang, 'Page', 'Sida')}</dt><dd><a href="{url(p['key'], lang)}">viccom.se{url(p['key'], lang)}</a></dd>
          </dl>{art}""")
    prods = "\n".join(prods)
    body = f"""          <h2 id="facts">{L(lang, 'Facts', 'Fakta')}</h2>
          <dl class="facts">
            <dt>Studio</dt><dd>VICCOM</dd>
            <dt>{L(lang, 'Founded', 'Grundad')}</dt><dd>2026</dd>
            <dt>{L(lang, 'Based in', 'Bas')}</dt><dd>{L(lang, 'Sweden', 'Sverige')}</dd>
            <dt>{L(lang, 'Founder', 'Grundare')}</dt><dd>Victor Immonen</dd>
            <dt>{L(lang, 'Team size', 'Antal anställda')}</dt><dd>1</dd>
            <dt>{L(lang, 'Products', 'Produkter')}</dt><dd>Wobble Wheels, Wyrmwind, AnyLap, Psst</dd>
            <dt>{L(lang, 'Website', 'Webb')}</dt><dd><a href="https://viccom.se">viccom.se</a></dd>
            <dt>{L(lang, 'Press contact', 'Presskontakt')}</dt><dd><a href="mailto:info@viccom.se">info@viccom.se</a></dd>
            <dt>{L(lang, 'Social', 'Sociala medier')}</dt>
            <dd>
              {social}
            </dd>
          </dl>

          <h2 id="about">{L(lang, 'About the studio', 'Om studion')}</h2>
          <h3>{L(lang, 'Short', 'Kort')}</h3>
          <blockquote class="boiler"><p>{L(lang, 'VICCOM is a one-person studio in Sweden making games and apps for mobile and desktop.', 'VICCOM är en svensk enmansstudio som gör spel och appar för mobil och dator.')}</p></blockquote>
          <h3>{L(lang, 'Long', 'Längre')}</h3>
          <blockquote class="boiler"><p>{L(lang, 'VICCOM is a one-person studio in Sweden, founded in 2026 by Victor Immonen. The studio makes games and apps for mobile and desktop, focused on clear design, things worth coming back to and no pay to win. Its first game, Wobble Wheels, launches on Google Play in November 2026. The dragon racing game Wyrmwind, the RC lap timer AnyLap and the group alert app Psst are in development.', 'VICCOM är en enmansstudio i Sverige, grundad 2026 av Victor Immonen. Studion gör spel och appar för mobil och dator, med fokus på tydlig design, saker som är värda att komma tillbaka till och inget pay to win. Det första spelet, Wobble Wheels, släpps på Google Play i november 2026. Drakracingspelet Wyrmwind, varvtidtagaren AnyLap för radiostyrda bilar och gruppsignalappen Psst är under utveckling.')}</p></blockquote>

          <h2 id="products">{L(lang, 'Games and apps', 'Spel och appar')}</h2>
{prods}

          <h2 id="logos">{L(lang, 'Logos', 'Logotyper')}</h2>
          <p>{L(lang, 'SVG files that scale to any size. Use the wordmark where it fits and the V mark at small sizes, like avatars and icons. Please don\'t change the colours or proportions.', 'SVG-filer som går att skala till valfri storlek. Använd ordmärket där det får plats och symbolen i små format, som profilbilder och ikoner. Ändra inte färger eller proportioner.')}</p>
          <ul class="assets">
            <li><div class="preview on-frost"><img src="/viccom-wordmark-graphite.svg" alt="VICCOM wordmark, graphite"></div><a href="/viccom-wordmark-graphite.svg" download>{L(lang, 'Wordmark, graphite', 'Ordmärke, grafit')}</a></li>
            <li><div class="preview on-ink"><img src="/viccom-wordmark-frost.svg" alt="VICCOM wordmark, frost"></div><a href="/viccom-wordmark-frost.svg" download>{L(lang, 'Wordmark, frost', 'Ordmärke, frost')}</a></li>
            <li><div class="preview on-ink"><img src="/viccom-wordmark-ember.svg" alt="VICCOM wordmark, ember"></div><a href="/viccom-wordmark-ember.svg" download>{L(lang, 'Wordmark, ember', 'Ordmärke, glöd')}</a></li>
            <li><div class="preview on-frost"><img src="/viccom-mark-graphite.svg" alt="VICCOM V mark, graphite"></div><a href="/viccom-mark-graphite.svg" download>{L(lang, 'V mark, graphite', 'Symbol, grafit')}</a></li>
            <li><div class="preview on-ink"><img src="/viccom-mark-frost.svg" alt="VICCOM V mark, frost"></div><a href="/viccom-mark-frost.svg" download>{L(lang, 'V mark, frost', 'Symbol, frost')}</a></li>
            <li><div class="preview on-ember"><img src="/viccom-mark-graphite.svg" alt="VICCOM V mark on ember"></div><a href="/viccom-logos.zip" download>{L(lang, 'All logos (zip)', 'Alla logotyper (zip)')}</a></li>
          </ul>

          <h2 id="colours">{L(lang, 'Colours and type', 'Färger och typsnitt')}</h2>
          <p>{L(lang, 'The palette is called Frozen mist. Ember is used sparingly, as a signal.', 'Paletten heter Frozen mist. Glöd används sparsamt, som en signal.')}</p>
          <ul class="swatches">
            <li><i style="background:#121311"></i><span><b>{L(lang, 'Night', 'Natt')}</b>#121311</span></li>
            <li><i style="background:#2A2B27"></i><span><b>{L(lang, 'Graphite', 'Grafit')}</b>#2A2B27</span></li>
            <li><i style="background:#7C7D75"></i><span><b>{L(lang, 'Moss', 'Mossa')}</b>#7C7D75</span></li>
            <li><i style="background:#ADACA7"></i><span><b>{L(lang, 'Mist', 'Dimma')}</b>#ADACA7</span></li>
            <li><i style="background:#D9DADF"></i><span><b>{L(lang, 'Ice', 'Is')}</b>#D9DADF</span></li>
            <li><i style="background:#FCF8D8"></i><span><b>Frost</b>#FCF8D8</span></li>
            <li><i style="background:#DD700B"></i><span><b>{L(lang, 'Ember', 'Glöd')}</b>#DD700B</span></li>
          </ul>
          <p>{L(lang, 'Headings are set in <strong>Unbounded</strong> and body text in <strong>Familjen Grotesk</strong>, both free under the SIL Open Font License.', 'Rubriker sätts i <strong>Unbounded</strong> och brödtext i <strong>Familjen Grotesk</strong>. Båda är fria under SIL Open Font License.')}</p>

          <h2 id="contact">{L(lang, 'Contact', 'Kontakt')}</h2>
          <p>{L(lang, 'Interviews, review copies and questions:', 'Intervjuer, recensionsexemplar och frågor:')} <a href="mailto:info@viccom.se">info@viccom.se</a>. {L(lang, 'We usually reply within a couple of days.', 'Vi svarar oftast inom ett par dagar.')}</p>"""
    title = L(lang, "Press kit", "Presskit")
    lede = L(lang, 'Everything you need to write about or show VICCOM and our products. Free to use in editorial coverage, videos and streams. Missing something? Email <a href="mailto:info@viccom.se">info@viccom.se</a>.',
             'Allt du behöver för att skriva om eller visa VICCOM och våra produkter. Fritt att använda i redaktionella sammanhang, videor och strömmar. Saknar du något? Mejla <a href="mailto:info@viccom.se">info@viccom.se</a>.')
    desc = L(lang, "Facts, logos, key art, screenshots and copy about VICCOM, Wobble Wheels, Wyrmwind, AnyLap and Psst.",
             "Fakta, logotyper, nyckelbilder, skärmbilder och texter om VICCOM, Wobble Wheels, Wyrmwind, AnyLap och Psst.")
    return doc_page(lang, "press", title, desc, lede, toc, body, active="press")

def page_404():
    return """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Page not found – VICCOM</title>
  <meta name="robots" content="noindex">
  <meta name="theme-color" content="#121311">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/style.css?v=""" + CSS_V + """">
</head>
<body class="grid-bg">
  <main class="wrap lost">
    <h1>404</h1>
    <p>This page doesn't exist. Check the address or head back to the start.</p>
    <p lang="sv">Sidan finns inte. Kolla adressen eller gå till startsidan.</p>
    <p class="actions"><a class="btn" href="/">Home</a><a class="btn ghost" href="/sv/" lang="sv">Startsida på svenska</a></p>
  </main>
</body>
</html>
"""

# ---------------------------------------------------------------- bygg
def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print("wrote", path.relative_to(ROOT))

def main():
    for lang in ("en", "sv"):
        write(outfile("home", lang), page_home(lang))
        for p in PRODUCTS:
            write(outfile(p["key"], lang), page_product(lang, p))
        write(outfile("press", lang), page_press(lang))
        write(outfile("privacy", lang), page_privacy(lang))
        write(outfile("delete", lang), page_delete(lang))
    write(ROOT / "404.html", page_404())

if __name__ == "__main__":
    main()
