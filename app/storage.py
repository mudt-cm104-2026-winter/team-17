"""Where the entries are kept.

For now: a Python list in memory. Simple, and it forgets everything when
the app restarts. That is fine for this stage.

The rest of the app only uses the functions below. Later in the semester
this file can be replaced by one that keeps the entries somewhere else.
As long as the function names stay the same, main.py does not change.
"""

_entries = []
_next_id = 1


def all_entries():
    """Return a copy of all entries, oldest first."""
    return list(_entries)


def add_entry(thing, person):
    """Store a new entry and return it."""
    global _next_id
    entry = {"id": _next_id, "thing": thing, "person": person}
    _entries.append(entry)
    _next_id += 1
    return entry


def remove_entry(entry_id):
    """Remove an entry by its ID; return whether an entry was found."""
    for index, entry in enumerate(_entries):
        if entry["id"] == entry_id:
            del _entries[index]
            return True
    return False


def sorted_entries(sort_by="title"):
    """Return entries sorted by title or rating without changing stored order."""
    entries = all_entries()
    if sort_by == "rating_asc":
        entries.sort(key=lambda entry: _rating_sort_key(entry["person"]))
    elif sort_by == "rating_desc":
        entries.sort(
            key=lambda entry: _rating_sort_key(entry["person"], descending=True)
        )
    else:
        entries.sort(key=lambda entry: entry["thing"].casefold())
    return entries


def _rating_sort_key(value, descending=False):
    try:
        rating = float(value)
    except (TypeError, ValueError):
        return (1, str(value).casefold())
    return (0, -rating if descending else rating)
