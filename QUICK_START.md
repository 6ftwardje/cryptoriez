# Quick Start: WebP Conversie & Optimalisatie

## 📋 Overzicht

Alle images op `index.html` zijn geconfigureerd om WebP te gebruiken met fallbacks naar originele formaten. Dit verbetert de laadtijden aanzienlijk.

## 🚀 Snelle Start (3 stappen)

### Stap 1: Converteer Images naar WebP

Gebruik de specificaties uit `WEBP_CONVERSION_GUIDE.md` om je images te converteren:

**Aanbevolen tool**: [Squoosh.app](https://squoosh.app) (gratis, online)
- Upload je image
- Selecteer WebP
- Pas kwaliteit aan volgens de guide
- Download

**Of gebruik command line:**
```bash
# Installeer cwebp (macOS)
brew install webp

# Converteer
cwebp -q 85 hero.png -o hero.webp
```

### Stap 2: Upload naar Supabase Storage

1. Ga naar je Supabase project → Storage
2. Maak bucket `images` (als deze nog niet bestaat)
3. Upload images naar de juiste folders:
   - `images/hero/hero.webp`
   - `images/logos/cryptoriez.webp`
   - `images/illustrations/illustratie.webp`
   - `images/testimonials/glen.webp`
   - `images/testimonials/glen_profile.webp`
   - `images/team/rousso.webp`
   - `images/social/fysieke_opleiding_hero.webp`

### Stap 3: Vervang URLs in HTML

**Optie A: Automatisch (aanbevolen)**
```bash
python replace_supabase_urls.py jouw-project-id
```

**Optie B: Handmatig**
- Open `index.html`
- Zoek en vervang: `YOUR_SUPABASE_PROJECT`
- Vervang met: je Supabase project ID

## ✅ Wat is er al gedaan?

- ✅ Alle `<img>` tags zijn aangepast met `<picture>` elementen
- ✅ WebP sources zijn toegevoegd met fallbacks
- ✅ Lazy loading is toegevoegd voor below-the-fold images
- ✅ Width/height attributes zijn toegevoegd voor layout stability
- ✅ Preload is geoptimaliseerd voor kritieke images
- ✅ Meta tags zijn aangepast voor social sharing

## 📊 Verwachte Verbeteringen

- **Bestandsgrootte**: 25-35% kleiner dan PNG/JPG
- **Laadtijd**: 30-50% sneller op mobiel
- **Lighthouse Score**: +10-15 punten voor Performance
- **Bandwidth**: Minder dataverbruik voor gebruikers

## 🔍 Testen

1. Open `index.html` in browser
2. Open Developer Tools (F12) → Network tab
3. Herlaad pagina
4. Controleer:
   - ✅ Images laden correct
   - ✅ WebP formaten worden gebruikt (zie `.webp` in Network tab)
   - ✅ Geen 404 errors

## 📝 Images die geconverteerd moeten worden

| Image | Huidig Formaat | WebP Bestand | Locatie |
|-------|---------------|--------------|---------|
| Hero achtergrond | `hero.png` | `hero.webp` | `images/hero/` |
| Logo | `cryptoriez.png` | `cryptoriez.webp` | `images/logos/` |
| Illustratie | `illustratie.jpg` | `illustratie.webp` | `images/illustrations/` |
| Glen testimonial | `glen.jpg` | `glen.webp` | `images/testimonials/` |
| Glen profiel | `glen_profile.png` | `glen_profile.webp` | `images/testimonials/` |
| Rousso profiel | `Rousso.jpg` | `rousso.webp` | `images/team/` |
| Social preview | `fysieke_opleiding_hero.jpg` | `fysieke_opleiding_hero.webp` | `images/social/` |

## 🆘 Problemen?

Zie `SUPABASE_SETUP.md` voor uitgebreide troubleshooting.

## 📚 Meer Informatie

- `WEBP_CONVERSION_GUIDE.md` - Gedetailleerde conversie instructies
- `SUPABASE_SETUP.md` - Supabase Storage setup guide

