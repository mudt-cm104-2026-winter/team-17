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
| Ssedaat | reviews and fixes |
| kadirefeekinci | coding |
| jonnyt296-cmd | Coding and testing |

## How we work


- Every piece of work starts as an issue. Our issues belong to three epics (Recommendations, Sorting and search, Docs) and are tracked on the project board with the columns Todo, In Progress and Done.
- We never commit directly to `main`, because it is protected. Each issue gets its own branch, named after the work, for example `rename-to-rating` or `add-delete-button`.
- Every pull request says what changed and why, and closes its issue with `closes #n`.
- Every pull request needs one approval from the other team member. The reviewer runs the app locally, comments on specific lines, and uses "Request changes" when something has to be fixed. The author fixes it on the same branch, and the reviewer approves again.
- The author merges only after the approval is shown on the pull request.
- If a branch conflicts with `main`, we merge `main` into the branch, solve the conflict on our laptops, and push again.
- Commit messages say what changed, and we keep commits small.
- Every pull request adds one line to `CHANGELOG.md`.

## Sources

<!-- One entry per source, added on the day you use it:
- 2026-11-05: <title or link>, used for <what>
-->

## Use of AI


2026-11-25: Claude, used for adding features, checked by running the application.
2026-11-25: Claude, guidance for git terminal codes, checked by reviewing the github repositories
