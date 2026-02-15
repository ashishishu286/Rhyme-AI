# Development Log

---

## Day 1 – CMU Dictionary Loader Implementation

### Objective
Build a function to load and parse the CMU Pronouncing Dictionary into a structured Python dictionary for further phoneme-based rhyme analysis.

---

### Problems Faced

- Initially implemented manual string parsing using `for` loops because I was not familiar with Python’s `split()` function.
- Discovered that the CMU dictionary contains multiple pronunciations for certain words (e.g., `read`, `read(1)`, `read(2)`), which required handling pronunciation variants properly.
- Attempted to manually detect and remove pronunciation markers like `(1)` using conditional checks and iteration.
- Used loops to extract phonemes instead of list slicing (`parts[1:]`).

---

### Solutions Implemented

- Replaced manual parsing logic with Python’s built-in `split()` method for cleaner and more efficient string handling.
- Normalized words using:
  ```python
  word = parts[0].split("(")[0].lower()

---
## Day 2 – Rhyme Extraction Engine & Git Workflow Setup

### Objective
Implement stress-based rhyme extraction logic using CMU phoneme data and establish a clean Git/GitHub workflow for the project.

---

### Work Completed

- Implemented rhyme clustering based on the last stressed vowel in phoneme sequences.
- Used reverse iteration to locate the final stressed vowel (`1` or `2`).
- Generated rhyme keys using:

    phoneme_key = "".join(parts[ind:])

- Structured rhyme dictionary mapping rhyme keys → list of words.
- Ensured support for multiple pronunciations per word.
- Set up Git repository and pushed project to GitHub.

---

### Problems Faced

- Misunderstood the nested structure of the CMU dictionary (list of pronunciations per word).
- Encountered `AttributeError: 'list' object has no attribute 'endswith'` due to incorrect depth handling.
- Accidentally committed unnecessary files (`.idea/`, `__pycache__/`, `cmudict.dict`) to the repository.
- Confusion regarding branch naming (`master` vs `main`) and detached HEAD state.

---

### Solutions Implemented

- Added an inner loop to correctly iterate over each pronunciation list.
- Debugged structure by inspecting data types before applying string methods.
- Created a proper `.gitignore` file and removed unwanted tracked files using:

    git rm --cached

- Renamed branch from `master` to `main`.
- Configured GitHub authentication and successfully pushed clean repository.

---

### Lessons Learned

- Understanding data structure hierarchy is critical in NLP tasks.
- Many runtime errors stem from incorrect assumptions about data shape.
- Clean version control practices are essential for professional development.
- Setting up Git properly early prevents long-term project clutter.
- Engineering includes tooling discipline, not just writing code.

---

### Outcome

- Functional stress-based rhyme indexing engine.
- Clean project structure with version control.
- Public GitHub repository reflecting structured development progress.

