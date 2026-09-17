#!/usr/bin/env python3
"""Vygeneruje .ics se směnami pro Juriho podle rozpisu ZÁŘÍ 2026.

R = ranní směna, D = denní směna, N = noční směna (přechází přes půlnoc do dalšího dne).
Časy směn se mění na jednom místě – v konstantách RANO, DEN a NOC.
"""
from datetime import datetime, timedelta

YEAR, MONTH = 2026, 9

RANO = ("06:00", "15:00")  # začátek, konec ranní směny
DEN = ("06:00", "18:00")   # začátek, konec denní směny
NOC = ("18:00", "06:00")   # začátek, konec noční směny (konec je následující den)

# den v měsíci -> typ směny
SMENY = {
    1: "D", 3: "D", 4: "R", 7: "N", 8: "N",
    11: "D", 12: "D", 13: "D", 14: "D",
    16: "N", 17: "N", 21: "N", 22: "N",
    25: "N", 26: "N", 27: "N", 30: "D",
}

NÁZVY = {"R": "Ranní směna", "D": "Denní směna", "N": "Noční směna"}
ČASY = {"R": RANO, "D": DEN, "N": NOC}

VTIMEZONE = """BEGIN:VTIMEZONE
TZID:Europe/Prague
X-LIC-LOCATION:Europe/Prague
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE"""


def stamp(d: datetime) -> str:
    return d.strftime("%Y%m%dT%H%M%S")


def main() -> None:
    now = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Juri smeny//Zari 2026//CS",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:Juri – směny",
        "X-WR-TIMEZONE:Europe/Prague",
        VTIMEZONE,
    ]

    for den in sorted(SMENY):
        typ = SMENY[den]
        zacatek_h, konec_h = ČASY[typ]
        start = datetime(YEAR, MONTH, den, *map(int, zacatek_h.split(":")))
        pres_pulnoc = typ == "N"
        konec_den = (start + timedelta(days=1)).date() if pres_pulnoc else start.date()
        end = datetime(konec_den.year, konec_den.month, konec_den.day,
                       *map(int, konec_h.split(":")))
        lines += [
            "BEGIN:VEVENT",
            f"UID:juri-{YEAR}{MONTH:02d}{den:02d}-{typ.lower()}@rozpis",
            f"DTSTAMP:{now}",
            f"DTSTART;TZID=Europe/Prague:{stamp(start)}",
            f"DTEND;TZID=Europe/Prague:{stamp(end)}",
            f"SUMMARY:{NÁZVY[typ]}",
            "DESCRIPTION:Rozpis směn ZÁŘÍ 2026 – sloupec Juri",
            "TRANSP:OPAQUE",
            "END:VEVENT",
        ]

    lines.append("END:VCALENDAR")
    with open("juri-zari-2026.ics", "w", encoding="utf-8", newline="") as f:
        f.write("\r\n".join(lines) + "\r\n")
    print(f"Hotovo: {len(SMENY)} směn")


if __name__ == "__main__":
    main()
