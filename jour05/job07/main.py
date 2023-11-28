def change(note: list) -> list:
    for k in range(len(note)):
        if note[k] > 40:
            if note[k] % 5 >= 3:
                note[k] += 5 - (note[k] % 5)
    return note


notes = [10, 39, 41, 83, 82, 86]
print(f"Notes de départ: {notes}")
print(f"Notes arrangées: {change(notes)}")