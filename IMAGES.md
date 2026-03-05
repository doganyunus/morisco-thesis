# Image Download Reference

All images in this repository are currently **placeholder images** (dark-background labelled JPEGs).
Replace them with the real public domain images listed below before publishing.

Run `python3 download_images.py` first — if Wikimedia access is available it will download automatically.
Otherwise download manually from the URLs below and save to the listed paths.

---

## images/hero/

| File | Source image | URL |
|------|-------------|-----|
| `constantinople-1572.jpg` | Braun & Hogenberg, *Byzantium Nunc Constantinopolis* (1572) | https://commons.wikimedia.org/wiki/File:1572_bird%27s_eye_view_map_of_Constantinople_-_Byzantium_Nunc_Constantinopolis.jpg |

---

## images/maps/

| File | Source image | URL |
|------|-------------|-----|
| `braun-hogenberg-constantinople-1572.jpg` | Same as hero above — cropped detail | Same URL as hero |
| `piri-reis-mediterranean.jpg` | Piri Reis, *Europe and the Mediterranean Sea* (c. 1525) | https://commons.wikimedia.org/wiki/File:Piri_Reis_map_of_Europe_and_the_Mediterranean_Sea.jpg |
| `portolan-1590.jpg` | Joan Riezo, Portolan Chart of the Mediterranean, Messina, 1590 | https://commons.wikimedia.org/wiki/File:1590_Portolan_chart_of_the_Mediterranean_Sea_and_Europe.png |
| `piri-reis-andalusia.jpg` | Piri Reis, Coastline of Andalusia, from *Kitâbü'l-Bahrîye* | Topkapı Palace Museum Archives (TSMA) — contact museum or search digitised collections |

---

## images/paintings/

| File | Source image | URL |
|------|-------------|-----|
| `mestre-denia-1613.jpg` | Vicente Mestre, *La Expulsión en el Puerto de Denia* (1613) | https://commons.wikimedia.org/wiki/File:La_Expulsi%C3%B3n_en_el_Puerto_de_Denia._Vicente_Mostre.jpg |
| `oromig-grao-valencia-1616.jpg` | Pere Oromig, *Embarco moriscos en el Grao de Valencia* (1616) | https://commons.wikimedia.org/wiki/File:Embarco_moriscos_en_el_Grao_de_valencia.jpg |
| `spy-cesare-ripa-1618.jpg` | Cesare Ripa, *Nova Iconologia* (1618) — "The Spy" engraving | Search Wikimedia Commons: "Cesare Ripa Iconologia 1618 spy" or Internet Archive |

---

## images/portraits/

| File | Source image | URL |
|------|-------------|-----|
| `selim-ii.jpg` | Nakkaş Osman, *Sultan Selim II with two servants* (c. 1570) | https://commons.wikimedia.org/wiki/File:Sultan_Selim_II_with_2_servants.jpg |
| `sokollu-mehmed-pasha.jpg` | Dominicus Custos after Fontana, *Sokollu Mehmed Pasha* (1603) | https://commons.wikimedia.org/wiki/File:Mehmed_Sokolovi%C4%87_(ca_1505-1579).png |
| `kilij-ali-pasha.jpg` | Miniature from *Nusretname* (1570s) showing Kılıç Ali Pasha | https://commons.wikimedia.org/wiki/File:Lala_Mustafa_Pa%C5%9Fa_ve_K%C4%B1l%C4%B1%C3%A7_Ali_Pa%C5%9Fa.JPG |
| `philip-ii-titian.jpg` | School of Titian, *Philip II of Spain* (c. 1550s) | https://commons.wikimedia.org/wiki/File:Philip_II,_King_of_Spain_(by_Titian%27s_school).jpg |
| `ahmad-haiari.jpg` | No known contemporary portrait. Use parchment texture or leave placeholder. | — |
| `aben-humeya.jpg` | No known contemporary portrait. Use parchment texture or leave placeholder. | — |
| `jeronimo-enriquez.jpg` | No known contemporary portrait. Use parchment texture or leave placeholder. | — |
| `haji-ibrahim.jpg` | No known contemporary portrait. Use parchment texture or leave placeholder. | — |
| `yunus-dogan.jpg` | Personal photograph of Yunus Doğan — replace with actual photo. | — |

---

## images/chapters/

| File | Source image | Suggested search |
|------|-------------|------------------|
| `alpujarras-mountains.jpg` | Landscape photo of the Alpujarras — use CC0 photo | Unsplash or Wikimedia Commons: "Alpujarras mountains Granada" |
| `algiers-harbor.jpg` | Historical view of Algiers harbor | Wikimedia Commons: "Port of Algiers" — several 19th-century lithographs available |

---

## Quick curl download (if running on a machine with Wikimedia access)

```bash
cd morisco-thesis
# Hero / Constantinople map
curl -L "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/1572_bird%27s_eye_view_map_of_Constantinople_-_Byzantium_Nunc_Constantinopolis.jpg/1920px-1572_bird%27s_eye_view_map_of_Constantinople_-_Byzantium_Nunc_Constantinopolis.jpg" -o images/hero/constantinople-1572.jpg
cp images/hero/constantinople-1572.jpg images/maps/braun-hogenberg-constantinople-1572.jpg
# Piri Reis Mediterranean
curl -L "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Piri_Reis_map_of_Europe_and_the_Mediterranean_Sea.jpg/1200px-Piri_Reis_map_of_Europe_and_the_Mediterranean_Sea.jpg" -o images/maps/piri-reis-mediterranean.jpg
# Portolan 1590
curl -L "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/1590_Portolan_chart_of_the_Mediterranean_Sea_and_Europe.png/1200px-1590_Portolan_chart_of_the_Mediterranean_Sea_and_Europe.png" -o images/maps/portolan-1590.jpg
# Mestre Denia
curl -L "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/La_Expulsi%C3%B3n_en_el_Puerto_de_Denia._Vicente_Mostre.jpg/1920px-La_Expulsi%C3%B3n_en_el_Puerto_de_Denia._Vicente_Mostre.jpg" -o images/paintings/mestre-denia-1613.jpg
# Oromig Valencia
curl -L "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Embarco_moriscos_en_el_Grao_de_valencia.jpg/1024px-Embarco_moriscos_en_el_Grao_de_valencia.jpg" -o images/paintings/oromig-grao-valencia-1616.jpg
# Sultan Selim II
curl -L "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Sultan_Selim_II_with_2_servants.jpg/400px-Sultan_Selim_II_with_2_servants.jpg" -o images/portraits/selim-ii.jpg
# Sokollu Mehmed Pasha
curl -L "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Mehmed_Sokolovi%C4%87_%28ca_1505-1579%29.png/400px-Mehmed_Sokolovi%C4%87_%28ca_1505-1579%29.png" -o images/portraits/sokollu-mehmed-pasha.jpg
# Kılıç Ali Pasha
curl -L "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Lala_Mustafa_Pa%C5%9Fa_ve_K%C4%B1l%C4%B1%C3%A7_Ali_Pa%C5%9Fa.JPG/400px-Lala_Mustafa_Pa%C5%9Fa_ve_K%C4%B1l%C4%B1%C3%A7_Ali_Pa%C5%9Fa.JPG" -o images/portraits/kilij-ali-pasha.jpg
# Philip II
curl -L "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Philip_II%2C_King_of_Spain_%28by_Titian%27s_school%29.jpg/400px-Philip_II%2C_King_of_Spain_%28by_Titian%27s_school%29.jpg" -o images/portraits/philip-ii-titian.jpg
```
