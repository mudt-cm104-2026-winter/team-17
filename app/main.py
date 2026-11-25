"""Things to bring: the starting point of your team project.

This is an example. Replace the topic with your own: change the fields,
the texts and the page. Grow it one pull request at a time.

What happens where:
- main.py      the web part: which address shows what (the "routes")
- storage.py   where the entries are kept
- templates/   the HTML page
- static/      the stylesheet
"""

from pathlib import Path

from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import storage

HERE = Path(__file__).parent

app = FastAPI(title="Movie and Books ratings")
app.mount("/static", StaticFiles(directory=HERE / "static"), name="static")
templates = Jinja2Templates(directory=HERE / "templates")
SORT_OPTIONS = ("title", "rating_asc", "rating_desc")


def valid_sort(sort):
    return sort if sort in SORT_OPTIONS else "title"


@app.get("/")
def show_list(request: Request, sort: str = "title"):
    """The start page: the form and all entries."""
    sort = valid_sort(sort)
    return templates.TemplateResponse(
        request,
        "index.html",
        {"entries": storage.sorted_entries(sort), "sort": sort},
    )


@app.post("/add")
def add(thing: str = Form(...), rating: str = Form(...)):
    """The form on the start page sends its fields here."""
    storage.add_entry(thing=thing.strip(), rating=rating.strip())
    # Back to the start page. 303 tells the browser: load it with GET.
    return RedirectResponse("/", status_code=303)


@app.get("/edit/{entry_id}")
def edit_form(request: Request, entry_id: int, sort: str = "title"):
    """Show the form for editing an existing rating."""
    entry = storage.entry_by_id(entry_id)
    if entry is None:
        raise HTTPException(status_code=404, detail="Rating not found")
    sort = valid_sort(sort)
    return templates.TemplateResponse(
        request, "edit.html", {"entry": entry, "sort": sort}
    )


@app.post("/edit/{entry_id}")
def edit(
    entry_id: int,
    thing: str = Form(...),
    rating: str = Form(...),
    sort: str = Form("title"),
):
    """Update an existing rating and return to the current sort order."""
    if not storage.update_entry(entry_id, thing.strip(), rating.strip()):
        raise HTTPException(status_code=404, detail="Rating not found")
    return RedirectResponse(f"/?sort={valid_sort(sort)}", status_code=303)


@app.post("/remove")
def remove(entry_id: int = Form(...), sort: str = Form("title")):
    """Remove an entry and return to the current sort order."""
    if not storage.remove_entry(entry_id):
        raise HTTPException(status_code=404, detail="Rating not found")
    return RedirectResponse(f"/?sort={valid_sort(sort)}", status_code=303)
