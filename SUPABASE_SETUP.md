# Supabase Storage Setup Instructies

## Stap 1: Supabase Storage Configureren

1. Ga naar je Supabase project dashboard
2. Navigeer naar **Storage** in het menu
3. Maak een nieuwe bucket genaamd `images` (of gebruik een bestaande)
4. Zorg dat de bucket **public** is (niet private)

## Stap 2: Folder Structuur Aanmaken

Upload je WebP images naar de volgende structuur in Supabase Storage:

```
images/
  ├── hero/
  │   └── hero.webp
  ├── logos/
  │   └── cryptoriez.webp
  ├── illustrations/
  │   └── illustratie.webp
  ├── testimonials/
  │   ├── glen.webp
  │   └── glen_profile.webp
  ├── team/
  │   └── rousso.webp
  └── social/
      └── fysieke_opleiding_hero.webp
```

## Stap 3: Public URL Ophalen

Voor elk bestand in Supabase Storage:
1. Klik op het bestand
2. Kopieer de **Public URL**
3. De URL ziet er zo uit: `https://YOUR_PROJECT_ID.supabase.co/storage/v1/object/public/images/hero/hero.webp`

## Stap 4: URL Vervangen in HTML

Vervang alle instanties van `YOUR_SUPABASE_PROJECT` in `index.html` met je daadwerkelijke Supabase project URL.

**Voorbeeld:**
- Zoek: `YOUR_SUPABASE_PROJECT`
- Vervang met: `abcdefghijklmnop` (je project ID)

Of gebruik het Python script hieronder om dit automatisch te doen.

## Stap 5: Python Script voor Automatische Vervanging

```python
# replace_supabase_urls.py
import re

# Vervang deze waarde met je Supabase project ID
SUPABASE_PROJECT_ID = "jouw-project-id-hier"

# Lees het HTML bestand
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Vervang alle instanties
content = content.replace(
    'YOUR_SUPABASE_PROJECT',
    SUPABASE_PROJECT_ID
)

# Schrijf terug
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Alle URLs zijn vervangen met project ID: {SUPABASE_PROJECT_ID}")
```

## Stap 6: Testen

1. Open `index.html` in je browser
2. Open Developer Tools (F12)
3. Ga naar Network tab
4. Herlaad de pagina
5. Controleer of alle images correct laden
6. Controleer of WebP formaten worden gebruikt (in Network tab zie je `.webp` bestanden)

## Troubleshooting

### Images laden niet
- Controleer of de bucket **public** is
- Controleer of de folder structuur exact overeenkomt
- Controleer of de bestandsnamen exact overeenkomen (hoofdlettergevoelig!)

### WebP wordt niet gebruikt
- Controleer of je browser WebP ondersteunt (moderne browsers doen dit)
- Controleer de Network tab om te zien welk formaat wordt geladen
- Fallback naar PNG/JPG is normaal voor oudere browsers

### CORS Errors
- Zorg dat CORS is ingeschakeld in Supabase Storage settings
- Controleer of de bucket public is

## Performance Tips

1. **CDN**: Supabase Storage gebruikt automatisch een CDN, dus images worden snel geladen
2. **Caching**: Images worden automatisch gecached door browsers
3. **Lazy Loading**: Below-the-fold images gebruiken al `loading="lazy"`
4. **Preload**: Kritieke images (hero) worden al gepreload

## Bestandsgroottes Controleren

Na upload naar Supabase, controleer de bestandsgroottes:
- Hero image: < 200KB
- Logo: < 20KB
- Illustratie: < 150KB
- Testimonial: < 250KB
- Profielfoto's: < 20KB

Als bestanden te groot zijn, gebruik een hogere compressie kwaliteit (lagere waarde) bij conversie.

