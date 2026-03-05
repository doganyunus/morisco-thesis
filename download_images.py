"""Download public domain historical images from Wikimedia Commons.
Run once: python3 download_images.py
Images save into the images/ subdirectories.
"""
import urllib.request
import urllib.error
import os
import time

BASE = os.path.dirname(os.path.abspath(__file__))

WIKIMEDIA_API = "https://commons.wikimedia.org/w/api.php"

def get_wikimedia_url(filename):
    """Resolve a Wikimedia Commons file name to its direct download URL."""
    url = (
        f"{WIKIMEDIA_API}?action=query&titles=File:{urllib.parse.quote(filename)}"
        f"&prop=imageinfo&iiprop=url&format=json"
    )
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            import json
            data = json.loads(resp.read())
            pages = data.get("query", {}).get("pages", {})
            for page in pages.values():
                info = page.get("imageinfo", [])
                if info:
                    return info[0]["url"]
    except Exception as e:
        print(f"  API error for {filename}: {e}")
    return None

def download(dest_path, url=None, wikimedia_filename=None, headers=None):
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 5000:
        print(f"  Already exists: {os.path.basename(dest_path)}")
        return True

    if wikimedia_filename and not url:
        url = get_wikimedia_url(wikimedia_filename)

    if not url:
        print(f"  No URL resolved for {os.path.basename(dest_path)}")
        return False

    req = urllib.request.Request(url, headers={
        "User-Agent": "MoriscoThesisBot/1.0 (academic portfolio; https://github.com/doganyunus/morisco-thesis)",
        **(headers or {})
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
            with open(dest_path, "wb") as f:
                f.write(data)
        print(f"  ✓ {os.path.basename(dest_path)} ({len(data)//1024} KB)")
        return True
    except Exception as e:
        print(f"  ✗ {os.path.basename(dest_path)}: {e}")
        return False

import urllib.parse

IMAGES = [
    # Hero
    {
        "dest": "images/hero/constantinople-1572.jpg",
        "wikimedia": "1572_bird's_eye_view_map_of_Constantinople_-_Byzantium_Nunc_Constantinopolis.jpg"
    },
    # Maps
    {
        "dest": "images/maps/braun-hogenberg-constantinople-1572.jpg",
        "wikimedia": "1572_bird's_eye_view_map_of_Constantinople_-_Byzantium_Nunc_Constantinopolis.jpg"
    },
    {
        "dest": "images/maps/piri-reis-mediterranean.jpg",
        "wikimedia": "Piri_Reis_map_of_Europe_and_the_Mediterranean_Sea.jpg"
    },
    {
        "dest": "images/maps/portolan-1590.jpg",
        "wikimedia": "1590_Portolan_chart_of_the_Mediterranean_Sea_and_Europe.png"
    },
    # Paintings
    {
        "dest": "images/paintings/mestre-denia-1613.jpg",
        "wikimedia": "La_Expulsión_en_el_Puerto_de_Denia._Vicente_Mostre.jpg"
    },
    {
        "dest": "images/paintings/oromig-grao-valencia-1616.jpg",
        "wikimedia": "Embarco_moriscos_en_el_Grao_de_valencia.jpg"
    },
    # Portraits
    {
        "dest": "images/portraits/selim-ii.jpg",
        "wikimedia": "Sultan_Selim_II_with_2_servants.jpg"
    },
    {
        "dest": "images/portraits/sokollu-mehmed-pasha.jpg",
        "wikimedia": "Mehmed_Sokolović_(ca_1505-1579).png"
    },
    {
        "dest": "images/portraits/kilij-ali-pasha.jpg",
        "wikimedia": "Lala_Mustafa_Paşa_ve_Kılıç_Ali_Paşa.JPG"
    },
    {
        "dest": "images/portraits/philip-ii-titian.jpg",
        "wikimedia": "Philip_II,_King_of_Spain_(by_Titian's_school).jpg"
    },
]

if __name__ == "__main__":
    print("Downloading public domain images from Wikimedia Commons...\n")
    ok = 0
    fail = 0
    for item in IMAGES:
        dest = os.path.join(BASE, item["dest"])
        print(f"→ {item['dest']}")
        success = download(
            dest,
            url=item.get("url"),
            wikimedia_filename=item.get("wikimedia")
        )
        if success:
            ok += 1
        else:
            fail += 1
        time.sleep(0.5)

    print(f"\nDone: {ok} downloaded, {fail} failed.")
    if fail:
        print("For failed images, download manually from Wikimedia Commons and place in the images/ directories.")
