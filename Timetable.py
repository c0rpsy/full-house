timetable = [
    ("09:00-10:00", {"Lokaal": "b.3.301", "Presentatie": "Presentatie 1"}),
    ("10:00-11:00", {"Lokaal": "b.3.302", "Presentatie": "Presentatie 2"}),
    ("11:00-12:00", {"Lokaal": "b.3.303", "Presentatie": "Presentatie 3"}),
    ("12:00-12:30", {"Lokaal": "Centrale Hal", "Presentatie": "Pauze"}),
    ("12:30-13:30", {"Lokaal": "b.3.304", "Presentatie": "Presentatie 4"}),
    ("12:30-13:30", {"Lokaal": "b.3.305", "Presentatie": "Presentatie 5"}),
    ("13:30-14:30", {"Lokaal": "b.3.306", "Presentatie": "Presentatie 6"}),
    ("13:30-14:30", {"Lokaal": "b.3.307", "Presentatie": "Presentatie 7"}),
    ("14:30-15:00", {"Lokaal": "b.3.308", "Presentatie": "Presentatie 8"}),
    ("14:30-15:00", {"Lokaal": "b.3.309", "Presentatie": "Presentatie 9"}),
    ("15:00-15:00", {"Lokaal": "b.3.310", "Presentatie": "Presentatie 10"})
]

# Toon het tijdschema
print("Tijdschema voor presentaties op Zuyd Hogeschool:")
print("{:<15} {:<15} {:<20}".format("Tijdslot", "Lokaal", "Presentatie"))
print("="*50)

for entry in timetable:
    tijdslot, gegevens = entry
    print("{:<15} {:<15} {:<20}".format(tijdslot, gegevens["Lokaal"], gegevens["Presentatie"]))






