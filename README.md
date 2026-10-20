# viccom.se

En statisk webbplats som består av ren HTML, CSS och lite JavaScript. Den behöver ingen byggprocess eller databas och fungerar på vilket webbhotell som helst.

## Innehåll

| Fil | Vad det är |
|---|---|
| `index.html` | Startsidan: hero med frostad ruta, spel, om, kontakt |
| `integritetspolicy.html` | Integritetspolicy (GDPR), går att använda som policy-URL i Google Play |
| `press.html` | Presskit: fakta, texter, logotyper, färger |
| `404.html` | Sida som visas när en adress inte finns |
| `CNAME` | Talar om för GitHub Pages att sajten ska ligga på viccom.se |
| `favicon.svg` | Ikon i webbläsarfliken |
| `assets/style.css` | All design. Färgerna ligger överst som variabler |
| `assets/frost.js` | Den frostade rutan på startsidan |
| `assets/press/` | Logotyper i SVG och en zip med alla |
| `assets/og.png` | Bild som visas när någon delar länken |
| `assets/fonts/` | Unbounded och Familjen Grotesk (fria typsnitt, OFL) |

## Fyll i innan publicering

Sök efter `[Ditt namn]`, `[Your name]` och `[fylls i]` i `press.html` och `integritetspolicy.html`. Organisationsnumret fyller du i när Verksamt är klart.

## Publicera med GitHub Pages (rekommenderat)

1. Skapa ett nytt publikt repo under **VICCOM-devs**, till exempel `viccom.se`.
2. Ladda upp alla filer i den här mappen till repots rot. På webben gör du det med *Add file → Upload files*.
3. Gå till **Settings → Pages**. Under *Source* väljer du *Deploy from a branch*, sedan `main` och `/ (root)`.
4. Under *Custom domain* skriver du `viccom.se` (filen `CNAME` gör det automatiskt).
5. Hos **One.com → DNS** ändrar du bara de här posterna:
   - **A-poster** för `viccom.se` (@): `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - **CNAME** för `www`: `viccom-devs.github.io`
6. Vänta tills GitHub visar att DNS är okej (från några minuter upp till ett dygn). Kryssa sedan i **Enforce HTTPS**.

Rör inte MX, SPF, DKIM, DMARC eller google-site-verification. De sköter e-posten.

## Andra ställen

- **One.com webbhotell**: ladda upp mappens innehåll till `public_html` via filhanteraren eller FTP. Filen `CNAME` behövs inte där.
- **Netlify / Cloudflare Pages**: dra och släpp mappen och koppla domänen enligt deras guide.

## Lägga till mer senare

- **Nytt spel**: kopiera `<article class="game">` i `index.html` och ändra status, namn och text. Vill du ha en egen sida per spel skapar du till exempel `spel/namn.html` utifrån `press.html`.
- **Tillverkning, butik eller annan ny sektion**: kopiera ett `<section class="section">`-block på startsidan, eller skapa en ny sida och lägg till en länk i menyn (`site-nav`) på alla sidor.
- **Färger**: ändra variablerna överst i `assets/style.css`.
