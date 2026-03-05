"""Download public domain historical images from Wikimedia Commons.
Run once: python3 download_images.py
Images save into the images/ subdirectories.
Uses Special:FilePath redirects — no API key needed.
"""
import urllib.request
import urllib.error
import urllib.parse
import os
import time

BASE = os.path.dirname(os.path.abspath(__file__))

# Browser-like User-Agent — Wikimedia requires a descriptive UA
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; MoriscoThesisBot/1.0; "
        "academic portfolio project; +https://github.com/doganyunus/morisco-thesis)"
    )
}

def download(dest_path, url):
    """Download a single file. Skip if already a real image (> 100 KB)."""
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 100_000:
        print(f"  Already exists: {os.path.basename(dest_path)}")
        return True

    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
        with open(dest_path, "wb") as f:
            f.write(data)
        print(f"  ✓ {os.path.basename(dest_path)} ({len(data)//1024} KB)")
        return True
    except Exception as e:
        print(f"  ✗ {os.path.basename(dest_path)}: {e}")
        return False


def wikimedia_url(filename):
    """Build a Special:FilePath URL that redirects to the full-size image."""
    return f"https://commons.wikimedia.org/wiki/Special:FilePath/{urllib.parse.quote(filename)}"


IMAGES = [
    # ── Hero ──────────────────────────────────────────────────────────────
    {
        "dest": "images/hero/constantinople-1572.jpg",
        "url": wikimedia_url("Byzantium_Nunc_Constantinopolis.jpg"),
    },
    # ── Maps ──────────────────────────────────────────────────────────────
    {
        "dest": "images/maps/braun-hogenberg-constantinople-1572.jpg",
        "url": wikimedia_url("Byzantium_Nunc_Constantinopolis.jpg"),
    },
    {
        "dest": "images/maps/piri-reis-andalusia.jpg",
        "url": wikimedia_url("Piri_reis_map_detail_of_spain_and_north_africa.jpg"),
    },
    {
        "dest": "images/maps/piri-reis-mediterranean.jpg",
        "url": wikimedia_url("Piri_Reis_map_of_Europe_and_the_Mediterranean_Sea.jpg"),
    },
    {
        "dest": "images/maps/portolan-1590.jpg",
        "url": wikimedia_url("Joan_Riezo_Portolan_chart_1590.jpg"),
    },
    # ── Paintings ─────────────────────────────────────────────────────────
    {
        "dest": "images/paintings/mestre-denia-1613.jpg",
        "url": wikimedia_url("La_Expulsión_en_el_Puerto_de_Denia._Vicente_Mostre.jpg"),
    },
    {
        "dest": "images/paintings/oromig-grao-valencia-1616.jpg",
        "url": wikimedia_url("Embarco_moriscos_en_el_Grao_de_valencia.jpg"),
    },
    {
        "dest": "images/paintings/spy-cesare-ripa-1618.jpg",
        "url": wikimedia_url("Cesare_Ripa_-_Iconologia_-_1603_-_page_460.jpg"),
    },
    # ── Portraits ─────────────────────────────────────────────────────────
    {
        "dest": "images/portraits/selim-ii.jpg",
        "url": wikimedia_url("Sultan_Selim_II_with_2_servants.jpg"),
    },
    {
        "dest": "images/portraits/sokollu-mehmed-pasha.jpg",
        "url": wikimedia_url("Mehmed_Sokolović_(ca_1505-1579).png"),
    },
    {
        "dest": "images/portraits/kilij-ali-pasha.jpg",
        "url": wikimedia_url("Lala_Mustafa_Paşa_ve_Kılıç_Ali_Paşa.JPG"),
    },
    {
        "dest": "images/portraits/philip-ii-titian.jpg",
        "url": wikimedia_url("Philip_II,_King_of_Spain_(by_Titian's_school).jpg"),
    },
    # ── Chapters (atmospheric) ────────────────────────────────────────────
    {
        "dest": "images/chapters/alpujarras-mountains.jpg",
        "url": wikimedia_url("Sierra_Nevada_desde_el_Llano_de_la_Perdiz_2.jpg"),
    },
    {
        "dest": "images/chapters/algiers-harbor.jpg",
        "url": wikimedia_url("Algiers_-_View_from_the_harbour_(6975413310).jpg"),
    },
]


if __name__ == "__main__":
    print("Downloading public domain images from Wikimedia Commons...\n")
    ok, fail = 0, 0
    for item in IMAGES:
        dest = os.path.join(BASE, item["dest"])
        print(f"→ {item['dest']}")
        if download(dest, item["url"]):
            ok += 1
        else:
            fail += 1
        time.sleep(1)

    print(f"\nDone: {ok} downloaded, {fail} failed.")
    if fail:
        print(
            "\nFor any failed images, download manually from Wikimedia Commons\n"
            "and place the file in the correct images/ subdirectory."
        )
