# Team project

Movie and Book ratings

## What this is

this is where you can write down the movie or book you've seen/read and rate them for other people's referal.

## How to run it

You need Python 3.10 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000 in your browser. Stop it with `Ctrl+C`.

The entries are kept in memory: after a restart the list is empty again.

## Team

<!-- One row per person: GitHub username and what you mainly take care of.
No real names: this repository is public. -->

| GitHub | Role |
|Ssedaat| reviews and fixes |
|kadirefeekinci| coding |
## How we work

<!-- How your team uses Git. For example:
- one branch per issue, named after it: `12-add-glossary`
- every pull request needs one approval from another team member
- the author merges after the approval
- every pull request adds a line to CHANGELOG.md
-->

## Sources

<!-- One entry per source, added on the day you use it:
- 2026-11-05: <title or link>, used for <what>
-->

## Use of AI

<!-- One entry per use, added on the day you use it:
- 2026-11-05: <tool>, used for <what>, checked by <how you checked the result>
"none" is a valid entry.
-->
