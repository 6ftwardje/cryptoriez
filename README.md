# Cryptoriez Website

Een complete multi-page website voor Cryptoriez, een crypto en trading opleidingsplatform in België. De website is volledig mobile-first ontworpen met focus op conversie-optimalisatie en gebruikerservaring.

## 🎯 Doel

De website heeft als primair doel:
- Inschrijvingen genereren voor fysieke crypto/trading opleidingen
- Kennismakingscalls plannen via Calendly
- Discord community leden werven
- Webinar inschrijvingen verzamelen
- Social proof tonen via testimonials en team presentatie

## 📄 Pagina's

De website bestaat uit de volgende pagina's:

### 1. **index.html** - Hoofdpagina
- Hero sectie met video achtergrond en krachtige headline
- Doelgroep sectie met probleemstelling
- Opleidingsinhoud met 6 kernmodules
- Discord community features
- Testimonials preview
- Calendly integratie voor call planning
- Navigatie naar alle andere pagina's
- Footer met contact info en social links

### 2. **fysieke-opleidingen.html** - Fysieke Opleidingen
- Hero sectie met parallax effect
- Locatie carousel met 4 steden: Brugge, Gent, Knokke, Kapellen
- Opleidingsstructuur en modules
- Prijsinformatie en inschrijving
- Voordelen van fysieke lessen
- CTA's naar Calendly

### 3. **discord.html** - Discord Community
- Hero sectie met Discord branding
- Community features en voordelen
- Trade calls en DCA Machine uitleg
- Dagelijkse markt updates
- Inschrijvingsformulier/CTA
- Social proof elementen

### 4. **testimonials.html** - Student Testimonials
- Video testimonials van studenten (Arturo, Dean)
- Geschreven testimonials
- Resultaten en success stories
- Social proof secties

### 5. **team.html** - Team Overzicht
- Teamleden presentatie (Arno, Chris, Dylan, Jason, Rousso)
- Profielen met foto's en beschrijvingen
- Expertise en achtergrond
- Contact informatie

### 6. **webinar.html** - Webinar Landing Page
- Webinar aanbieding en details
- Datum en tijd informatie
- Inschrijvingsformulier
- Value proposition
- CTA's

### 7. **bedankt.html** - Bedankt Pagina
- Bevestiging na betaling/inschrijving
- Volgende stappen informatie
- Contact opties

### 8. **footer-component.html** - Footer Component
- Herbruikbare footer component (mogelijk voor toekomstige modularisatie)

## 🛠️ Technische Stack

### Frontend
- **HTML5** - Semantische markup
- **TailwindCSS** - Via CDN, utility-first CSS framework
- **JavaScript (Vanilla)** - Geen frameworks, pure JS voor interactiviteit
- **Google Fonts** - Inter font family
- **Font Awesome 6.5.0** - Iconen via CDN

### Externe Services
- **Google Analytics** - Tracking ID: `AW-11184032010`
- **TikTok Pixel** - Pixel ID: `D3NQ08JC77UD89P2EPVG`
- **Calendly** - Voor call planning (embed integratie)

### SEO & Metadata
- Volledige Open Graph tags voor social sharing
- Twitter Card metadata
- Schema.org structured data (EducationalOrganization)
- Canonical URLs
- Geo-location metadata voor lokale SEO
- Sitemap.xml voor search engines
- Robots.txt configuratie

### PWA Features
- **manifest.json** - Progressive Web App configuratie
- Theme colors en icons
- Standalone display mode

## 🎨 Design System

### Kleuren
- **Primary Orange**: `#f88226` (crypto-orange)
- **Primary Blue**: `#4670db` (crypto-blue)
- **Background**: Dark gray (`#111827`, `#1f2937`)
- **Text**: White met verschillende opacity levels voor hiërarchie

### Typografie
- **Font Family**: Inter (Google Fonts)
- **Weights**: 300, 400, 500, 600, 700, 800, 900
- Responsive font sizes met Tailwind breakpoints

### Design Patterns
- **Dark Theme**: Consistente donkere achtergrond met lichte tekst
- **Liquid Glass Effect**: Backdrop blur effecten voor moderne UI
- **Fade-in Animations**: Scroll-triggered animaties voor elementen
- **Smooth Scroll**: Native smooth scroll behavior
- **Sticky Navigation**: Fixed header met backdrop blur
- **Sticky CTA**: Mobile bottom CTA bar die verschijnt bij scroll
- **Parallax Effects**: Op hero secties voor diepte

### Responsive Breakpoints
- Mobile-first approach
- Tailwind default breakpoints: sm (640px), md (768px), lg (1024px), xl (1280px)

## 🚀 Features

### Navigatie
- Sticky navigation bar op alle pagina's
- Mobile hamburger menu
- Desktop navigation links naar alle secties
- Logo link naar homepage
- CTA button "Plan een call" prominent geplaatst

### Interactiviteit
- Smooth scroll naar anchors
- Fade-in animaties bij scroll (Intersection Observer)
- Mobile menu toggle
- Sticky CTA bar op mobile
- Location carousel op fysieke-opleidingen pagina
- Video backgrounds op hero secties

### Conversie Elementen
- Meerdere CTA's per pagina
- Calendly embed voor directe call planning
- Social proof via testimonials
- Trust badges en certificeringen
- Duidelijke value propositions

### Performance
- CDN-based assets (Tailwind, Fonts, Icons)
- Optimized images (JPG, PNG, SVG)
- Lazy loading mogelijkheden
- Minimal JavaScript footprint

## 📁 Bestandsstructuur

```
cryptoriez/
├── index.html                    # Hoofdpagina
├── fysieke-opleidingen.html      # Fysieke opleidingen pagina
├── discord.html                  # Discord community pagina
├── testimonials.html             # Testimonials pagina
├── team.html                     # Team overzicht
├── webinar.html                  # Webinar landing page
├── bedankt.html                  # Bedankt pagina
├── footer-component.html         # Footer component
├── manifest.json                 # PWA manifest
├── sitemap.xml                   # SEO sitemap
├── robots.txt                    # Search engine config
├── README.md                     # Deze documentatie
│
├── Assets/
│   ├── cryptoriez.png            # Logo
│   ├── hero.png                  # Hero afbeelding
│   ├── fysieke_opleiding_hero.jpg # Opleiding hero
│   ├── brugge.jpg                # Locatie foto
│   ├── Gent.png                  # Locatie foto
│   ├── knokke.png                # Locatie foto
│   ├── kapellen.jpg              # Locatie foto
│   └── [andere afbeeldingen]
│
├── teamleden/                    # Team foto's
│   ├── Arno.jpg
│   ├── Chris.jpg
│   ├── Dylan.jpg
│   ├── Jason.jpg
│   └── Rousso.jpg
│
├── testimonials/                 # Testimonial media
│   ├── Arturo_placeholder.jpg
│   ├── Arturo_web.mp4
│   ├── Dean_placeholder.jpg
│   └── Dean_web.mp4
│
├── badges/                       # Certificeringen/badges
│   ├── 1.jpg
│   ├── 2.jpg
│   ├── 3.png
│   └── 4.png
│
└── animaties/                    # Lottie animaties
    └── lottie_test_cryptoriez.json
```

## 🔧 Setup & Development

### Lokale Development

1. **Clone repository** (of download bestanden)

2. **Start lokale server**:
```bash
# Python 3
python3 -m http.server 8000

# Of met Node.js (als http-server geïnstalleerd)
npx http-server -p 8000

# Of met PHP
php -S localhost:8000
```

3. **Open in browser**: `http://localhost:8000`

### Dependencies

Geen build proces of package manager nodig. Alle dependencies zijn via CDN:
- TailwindCSS: `https://cdn.tailwindcss.com`
- Google Fonts: `https://fonts.googleapis.com`
- Font Awesome: `https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/`

### Productie Checklist

- [ ] Vervang Calendly placeholder met echte embed code
- [ ] Verifieer alle externe links
- [ ] Test alle formulieren en CTA's
- [ ] Controleer analytics tracking
- [ ] Valideer SEO metadata
- [ ] Test op verschillende devices
- [ ] Optimaliseer afbeeldingen (compressie)
- [ ] Verifieer sitemap.xml en robots.txt

## 📊 Analytics & Tracking

### Google Analytics
- Tracking ID: `AW-11184032010`
- Geconfigureerd op alle pagina's
- Page view tracking automatisch

### TikTok Pixel
- Pixel ID: `D3NQ08JC77UD89P2EPVG`
- Geconfigureerd op alle pagina's
- Page view events automatisch

### Event Tracking
- CTA clicks kunnen getrackt worden via gtag events
- Form submissions kunnen getrackt worden
- Custom events kunnen toegevoegd worden waar nodig

## 🔍 SEO Features

### On-Page SEO
- Semantische HTML5 elementen
- Proper heading hierarchy (H1, H2, H3)
- Alt tags op alle afbeeldingen
- Meta descriptions op alle pagina's
- Keywords metadata
- Canonical URLs

### Structured Data
- Schema.org EducationalOrganization markup
- Address information voor lokale SEO
- Social media links in structured data

### Technical SEO
- Sitemap.xml voor crawlers
- Robots.txt configuratie
- Mobile-responsive (Google mobile-first indexing)
- Fast loading (CDN assets, optimized images)

### Local SEO
- Geo-location metadata
- Addresses voor Brugge, Kapellen, Knokke, Gent
- Local business information

## 🎯 Conversie Optimalisatie

### CTA Strategie
- Meerdere CTA's per pagina
- Sticky CTA op mobile
- Prominente "Plan een call" buttons
- Calendly direct embed voor lage friction

### Social Proof
- Video testimonials
- Geschreven testimonials
- Team presentatie voor autoriteit
- Badges en certificeringen

### User Experience
- Mobile-first design voor ad traffic
- Snelle laadtijden
- Duidelijke navigatie
- Geen afleidende elementen
- Smooth scroll en animaties voor engagement

## 📞 Calendly Integratie

Calendly wordt gebruikt voor call planning. De integratie kan op twee manieren:

1. **Inline Widget** (aanbevolen):
```html
<div class="calendly-inline-widget" data-url="https://calendly.com/your-link"></div>
<script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
```

2. **Popup Button**:
```html
<a href="https://calendly.com/your-link" onclick="Calendly.initPopupWidget({url: 'https://calendly.com/your-link'});return false;">Plan een call</a>
```

## 🚀 Deployment

De website is een static site en kan gedeployed worden op:

- **Netlify** - Drag & drop of Git integration
- **Vercel** - Git integration, automatische deployments
- **GitHub Pages** - Direct vanuit repository
- **AWS S3 + CloudFront** - Voor enterprise setup
- **Cloudflare Pages** - Snelle CDN
- **Any static hosting** - Geen server-side code nodig

### Deployment Checklist
- [ ] Update alle absolute URLs naar productie domain
- [ ] Verifieer analytics tracking werkt
- [ ] Test alle externe links
- [ ] Controleer HTTPS certificaat
- [ ] Valideer sitemap.xml bereikbaarheid
- [ ] Test mobile responsiveness
- [ ] Verifieer alle formulieren werken

## 🔄 Onderhoud & Updates

### Regelmatige Updates
- Testimonials toevoegen/updaten
- Team informatie bijwerken
- Prijzen en data updaten
- Nieuwe locaties toevoegen
- Content updates voor SEO

### Monitoring
- Google Analytics performance
- TikTok Pixel conversions
- Form submissions
- Calendly bookings
- Page speed metrics

## 📝 Notities voor AI Models

### Belangrijke Context
- Website is volledig in het Nederlands (nl-BE)
- Focus op Belgische markt (Brugge, Gent, Knokke, Kapellen)
- Crypto/trading educatie niche
- Fysieke lessen + online Discord community
- Conversie-gedreven design

### Code Structuur
- Geen build proces - direct HTML/CSS/JS
- TailwindCSS via CDN (geen config file)
- Custom JavaScript voor interactiviteit
- Inline styles voor custom effects
- Herbruikbare componenten kunnen gemaakt worden

### Styling Conventies
- Tailwind utility classes primair
- Custom CSS in `<style>` tags per pagina
- Liquid glass effects via backdrop-filter
- Fade-in classes voor animaties
- Responsive via Tailwind breakpoints

### JavaScript Patterns
- Vanilla JS, geen frameworks
- Event listeners voor interactiviteit
- Intersection Observer voor scroll animaties
- Mobile menu toggle state management
- Smooth scroll implementatie

## 📞 Contact & Support

Voor vragen over de website of updates, contacteer het Cryptoriez team via:
- Website: https://cryptoriez.be
- Instagram: @cryptoriez
- LinkedIn: Cryptoriez
- YouTube: @Cryptoriez

---

**Laatste update**: 2025-01-27
**Versie**: 2.0 (Multi-page website)
