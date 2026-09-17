# Rozpis směn – Juri

`juri-zari-2026.ics` – 17 směn ze sloupce **Juri** v rozpisu ZÁŘÍ 2026.

| Typ | Čas | Dny v září |
|---|---|---|
| **R** – ranní | 6:00–15:00 | 4. |
| **D** – denní | 6:00–18:00 | 1., 3., 11., 12., 13., 14., 30. |
| **N** – noční | 18:00–6:00 (do dalšího dne) | 7., 8., 16., 17., 21., 22., 25., 26., 27. |

Časové pásmo Europe/Prague.

## Import do Apple Calendar

**Mac** – Kalendář → Soubor → Importovat… → vyber `.ics` → zvol kalendář.

**iPhone** – soubor nejdřív ulož do Souborů (Sdílet → Uložit do Souborů),
pak ho v aplikaci Soubory otevři klepnutím → Kalendář nabídne „Přidat vše".
Alternativa: poslat si `.ics` mailem a klepnout na přílohu v Mailu.

Soubor záměrně neobsahuje `METHOD:PUBLISH` ani `X-WR-CALNAME` – s nimi
Apple Calendar část importů spolkne bez dotazu, kam se má uložit.

## Změna časů směn
Uprav konstanty `RANO`, `DEN` a `NOC` v `generate_juri.py`, pak spusť `python3 generate_juri.py`.
