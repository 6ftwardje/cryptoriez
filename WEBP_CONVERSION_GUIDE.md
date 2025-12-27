# WebP Conversie & Optimalisatie Guide

## Images die geconverteerd moeten worden

### 1. **hero.png** → hero.webp
- **Gebruik**: Hero achtergrond (desktop)
- **Aanbevolen resolutie**: 1920x1080px (16:9)
- **Max bestandsgrootte**: < 200KB
- **Kwaliteit**: 80-85%
- **Notitie**: Dit is een kritieke above-the-fold image, maar wordt alleen op desktop getoond

### 2. **cryptoriez.png** → cryptoriez.webp
- **Gebruik**: Logo (meerdere keren gebruikt: nav, mobile menu, footer)
- **Aanbevolen resolutie**: 400x100px (originele aspect ratio behouden)
- **Max bestandsgrootte**: < 20KB
- **Kwaliteit**: 90-95% (logo moet scherp blijven)
- **Notitie**: Logo's moeten scherp blijven, hogere kwaliteit

### 3. **illustratie.jpg** → illustratie.webp
- **Gebruik**: Illustratie in "Voor wie is deze opleiding?" sectie
- **Aanbevolen resolutie**: 1200x800px (3:2 ratio)
- **Max bestandsgrootte**: < 150KB
- **Kwaliteit**: 80-85%

### 4. **glen.jpg** → glen.webp
- **Gebruik**: Testimonial achtergrond (groot, featured)
- **Aanbevolen resolutie**: 1920x1080px (16:9)
- **Max bestandsgrootte**: < 250KB
- **Kwaliteit**: 80-85%

### 5. **glen_profile.png** → glen_profile.webp
- **Gebruik**: Profielfoto in testimonial card
- **Aanbevolen resolutie**: 200x200px (1:1, square)
- **Max bestandsgrootte**: < 15KB
- **Kwaliteit**: 85-90%

### 6. **Rousso.jpg** → rousso.webp
- **Gebruik**: Profielfoto in call-to-action sectie
- **Aanbevolen resolutie**: 200x200px (1:1, square)
- **Max bestandsgrootte**: < 20KB
- **Kwaliteit**: 85-90%

### 7. **fysieke_opleiding_hero.jpg** → fysieke_opleiding_hero.webp
- **Gebruik**: Open Graph / Social media preview
- **Aanbevolen resolutie**: 1200x630px (1.91:1 - Facebook/Twitter standaard)
- **Max bestandsgrootte**: < 200KB
- **Kwaliteit**: 80-85%

## Conversie Commando's (voor lokaal gebruik)

### Met cwebp (Google WebP tools):
```bash
# Hero image
cwebp -q 85 hero.png -o hero.webp

# Logo
cwebp -q 95 cryptoriez.png -o cryptoriez.webp

# Illustratie
cwebp -q 85 illustratie.jpg -o illustratie.webp

# Testimonial
cwebp -q 85 glen.jpg -o glen.webp

# Profielfoto's
cwebp -q 90 glen_profile.png -o glen_profile.webp
cwebp -q 90 Rousso.jpg -o rousso.webp

# Social media image
cwebp -q 85 fysieke_opleiding_hero.jpg -o fysieke_opleiding_hero.webp
```

### Met ImageMagick:
```bash
# Voor PNG/JPG naar WebP
magick hero.png -quality 85 hero.webp
magick illustratie.jpg -quality 85 -resize 1200x800 illustratie.webp
```

## Supabase Storage Structuur

Aanbevolen folder structuur:
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

## Performance Optimalisaties

1. **Lazy Loading**: Voor images below the fold
2. **Preload**: Alleen voor kritieke above-the-fold images
3. **Responsive Images**: srcset gebruiken waar nodig
4. **Fallbacks**: Altijd PNG/JPG fallback voor browsers zonder WebP support
5. **CDN**: Supabase Storage fungeert als CDN

## Browser Support

WebP wordt ondersteund door:
- Chrome 23+
- Firefox 65+
- Edge 18+
- Safari 14+
- Opera 12.1+

Fallback naar origineel formaat voor oudere browsers.

