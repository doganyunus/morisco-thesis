"""
Create placeholder images for the morisco-thesis portfolio.
Run once: python3 create_placeholders.py
These are replaced by real images when downloaded.
"""
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

BASE = os.path.dirname(os.path.abspath(__file__))

PALETTE = {
    "deep_ocean": (22, 32, 57),
    "cobalt": (30, 58, 95),
    "terracotta": (184, 92, 56),
    "parchment": (242, 232, 213),
    "gold": (201, 168, 76),
    "text_light": (240, 228, 204),
    "text_muted": (168, 152, 128),
}

IMAGES = [
    # Hero — wide landscape, dark
    {
        "dest": "images/hero/constantinople-1572.jpg",
        "size": (1920, 1080),
        "bg": "deep_ocean",
        "label": "HERO IMAGE",
        "desc": "Braun & Hogenberg\nByzantium Nunc Constantinopolis\n1572\n\nDownload from Wikimedia Commons:\nhttps://commons.wikimedia.org/wiki/\nFile:1572_bird%27s_eye_view_map_of_Constantinople",
        "accent": "gold",
    },
    # Maps
    {
        "dest": "images/maps/braun-hogenberg-constantinople-1572.jpg",
        "size": (1200, 800),
        "bg": "deep_ocean",
        "label": "MAP: Constantinople 1572",
        "desc": "Braun & Hogenberg\nByzantium Nunc Constantinopolis\n1572",
        "accent": "gold",
    },
    {
        "dest": "images/maps/piri-reis-mediterranean.jpg",
        "size": (1200, 800),
        "bg": "cobalt",
        "label": "MAP: Piri Reis Mediterranean",
        "desc": "Piri Reis\nEurope and the Mediterranean Sea\nc. 1525",
        "accent": "gold",
    },
    {
        "dest": "images/maps/portolan-1590.jpg",
        "size": (1200, 800),
        "bg": "cobalt",
        "label": "MAP: Portolan Chart 1590",
        "desc": "Joan Riezo\nPortolan Chart of the Mediterranean\nMessina, 1590",
        "accent": "gold",
    },
    {
        "dest": "images/maps/piri-reis-andalusia.jpg",
        "size": (800, 600),
        "bg": "deep_ocean",
        "label": "MAP: Piri Reis Andalusia",
        "desc": "Piri Reis\nCoastline of Andalusia\nKitâbü'l-Bahrîye\n16th century\nTopkapı Palace Museum Archives",
        "accent": "gold",
    },
    # Paintings
    {
        "dest": "images/paintings/mestre-denia-1613.jpg",
        "size": (1920, 1080),
        "bg": "cobalt",
        "label": "PAINTING: Expulsion at Denia",
        "desc": "Vicente Mestre\nLa Expulsión en el Puerto de Denia\n1613\nColección Bancaja, Valencia",
        "accent": "terracotta",
    },
    {
        "dest": "images/paintings/oromig-grao-valencia-1616.jpg",
        "size": (800, 500),
        "bg": "cobalt",
        "label": "PAINTING: Embarco Valencia 1616",
        "desc": "Pere Oromig\nEmbarco moriscos en el Grao de Valencia\n1616\nColección Bancaja, Valencia",
        "accent": "terracotta",
    },
    {
        "dest": "images/paintings/spy-cesare-ripa-1618.jpg",
        "size": (600, 800),
        "bg": "parchment",
        "label": "ENGRAVING: The Spy",
        "desc": "Cesare Ripa\n\"The Spy\"\nNova Iconologia\nPadova, 1618",
        "accent": "terracotta",
    },
    # Chapters
    {
        "dest": "images/chapters/alpujarras-mountains.jpg",
        "size": (800, 600),
        "bg": "deep_ocean",
        "label": "LOCATION: Alpujarras Mountains",
        "desc": "Alpujarras Mountains\nSouth of Granada\nSite of the 1568 Morisco rebellion",
        "accent": "gold",
    },
    {
        "dest": "images/chapters/algiers-harbor.jpg",
        "size": (800, 600),
        "bg": "cobalt",
        "label": "LOCATION: Algiers Harbor",
        "desc": "Port of Algiers\nOttoman beylerbeylik of Cezayir-i Garb\nPrimary base for Morisco exiles",
        "accent": "gold",
    },
    # Portraits
    {
        "dest": "images/portraits/selim-ii.jpg",
        "size": (400, 400),
        "bg": "deep_ocean",
        "label": "PORTRAIT",
        "desc": "Sultan Selim II\nr. 1566–1574\nNakkaş Osman, c. 1570\nWikimedia Commons",
        "accent": "gold",
    },
    {
        "dest": "images/portraits/sokollu-mehmed-pasha.jpg",
        "size": (400, 400),
        "bg": "deep_ocean",
        "label": "PORTRAIT",
        "desc": "Sokollu Mehmed Pasha\nGrand Vizier 1565–1579\nDominicus Custos, 1603\nWikimedia Commons",
        "accent": "gold",
    },
    {
        "dest": "images/portraits/kilij-ali-pasha.jpg",
        "size": (400, 400),
        "bg": "deep_ocean",
        "label": "PORTRAIT",
        "desc": "Kılıç Ali Pasha\nGrand Admiral 1571–1587\nNusretname miniature, 1570s\nWikimedia Commons",
        "accent": "gold",
    },
    {
        "dest": "images/portraits/philip-ii-titian.jpg",
        "size": (400, 400),
        "bg": "deep_ocean",
        "label": "PORTRAIT",
        "desc": "Philip II of Spain\nr. 1556–1598\nSchool of Titian, c. 1550s\nWikimedia Commons",
        "accent": "gold",
    },
    {
        "dest": "images/portraits/ahmad-haiari.jpg",
        "size": (400, 400),
        "bg": "cobalt",
        "label": "PORTRAIT",
        "desc": "Ahmad b. Qasim al-Hajarī\nc. 1570–1640\nNo known contemporary portrait",
        "accent": "gold",
    },
    {
        "dest": "images/portraits/aben-humeya.jpg",
        "size": (400, 400),
        "bg": "cobalt",
        "label": "PORTRAIT",
        "desc": "Aben Humeya\nd. 1569\nNo known contemporary portrait",
        "accent": "terracotta",
    },
    {
        "dest": "images/portraits/jeronimo-enriquez.jpg",
        "size": (400, 400),
        "bg": "cobalt",
        "label": "PORTRAIT",
        "desc": "Jerónimo Enríquez\nc. 1610–1615\nNo known contemporary portrait",
        "accent": "terracotta",
    },
    {
        "dest": "images/portraits/haji-ibrahim.jpg",
        "size": (400, 400),
        "bg": "cobalt",
        "label": "PORTRAIT",
        "desc": "Hajı Ibrahim Müteferrika\nfl. 1609\nNo known contemporary portrait",
        "accent": "gold",
    },
    {
        "dest": "images/portraits/yunus-dogan.jpg",
        "size": (400, 400),
        "bg": "deep_ocean",
        "label": "PHOTO",
        "desc": "Yunus Doğan\nPhD Candidate\nEuropean University Institute\nFlorence, Italy",
        "accent": "gold",
    },
]

def make_placeholder(dest, size, bg_key, label, desc, accent_key):
    path = os.path.join(BASE, dest)
    if os.path.exists(path) and os.path.getsize(path) > 50000:
        print(f"  Skipping (real image exists): {dest}")
        return

    os.makedirs(os.path.dirname(path), exist_ok=True)
    w, h = size
    bg_color = PALETTE[bg_key]
    accent_color = PALETTE[accent_key]
    text_color = PALETTE["text_light"] if bg_key != "parchment" else PALETTE["deep_ocean"]
    muted_color = PALETTE["text_muted"] if bg_key != "parchment" else (120, 100, 80)

    img = Image.new("RGB", (w, h), bg_color)
    draw = ImageDraw.Draw(img)

    # Draw decorative border
    border = 3
    draw.rectangle([border, border, w - border - 1, h - border - 1],
                   outline=accent_color, width=border)

    # Draw corner accents
    corner = 20
    for cx, cy, dx, dy in [(border, border, 1, 1), (w - border - 1, border, -1, 1),
                           (border, h - border - 1, 1, -1), (w - border - 1, h - border - 1, -1, -1)]:
        draw.line([(cx, cy), (cx + dx * corner, cy)], fill=accent_color, width=2)
        draw.line([(cx, cy), (cx, cy + dy * corner)], fill=accent_color, width=2)

    # Draw center diamond
    cx_center, cy_center = w // 2, h // 2
    diamond_size = min(w, h) // 12
    draw.polygon([
        (cx_center, cy_center - diamond_size),
        (cx_center + diamond_size, cy_center),
        (cx_center, cy_center + diamond_size),
        (cx_center - diamond_size, cy_center)
    ], outline=accent_color, width=2)

    # Draw label at top
    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", max(14, h // 25))
        font_small = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", max(11, h // 35))
    except:
        font_large = ImageFont.load_default()
        font_small = font_large

    label_y = h // 5
    bbox = draw.textbbox((0, 0), label, font=font_large)
    lw = bbox[2] - bbox[0]
    draw.text(((w - lw) // 2, label_y), label, fill=accent_color, font=font_large)

    # Horizontal rule
    rule_y = label_y + (bbox[3] - bbox[1]) + 16
    draw.line([(w // 4, rule_y), (3 * w // 4, rule_y)], fill=accent_color, width=1)

    # Draw description lines
    desc_y = rule_y + 20
    lines = desc.split('\n')
    line_h = max(16, h // 28)
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font_small)
        lw = bbox[2] - bbox[0]
        draw.text(((w - lw) // 2, desc_y), line, fill=muted_color, font=font_small)
        desc_y += line_h + 3

    # Save
    mode = "RGB"
    img.save(path, "JPEG", quality=82, optimize=True)
    print(f"  ✓ Created placeholder: {dest} ({w}×{h})")

if __name__ == "__main__":
    print("Creating placeholder images...\n")
    for item in IMAGES:
        make_placeholder(
            item["dest"], item["size"], item["bg"],
            item["label"], item["desc"], item["accent"]
        )
    print("\nDone. Replace these placeholders with real images using download_images.py")
    print("or manually downloading from the URLs listed in IMAGES.md")
