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
---

# Devlog — Day 4

## Goal  
Upgrade the rhyme engine from exact suffix matching to similarity-based scoring.

## What I Built  
- Implemented `rhyme_score(p1, p2)`  
- Designed sliding-window phoneme alignment  
- Enabled relaxed rhyme detection (≥ 2 phoneme matches)  
- Built `get_similar_rhymes(word)`  
- Kept exact rhyme engine (v1) intact alongside similarity engine (v2)

## Key Concepts Learned  
- Difference between strict suffix matching and relaxed alignment  
- Sliding window comparison for sequence similarity  
- Handling variable-length phoneme segments  
- Separating scoring logic from threshold logic  

## Problems Faced  
- Incorrect suffix alignment (e.g., smoke vs stoked mismatch)  
- Overcomplicated index logic  
- Confusion between strict vs relaxed rhyme rules  

## Solutions Implemented  
- Rewrote scoring using sliding-window alignment  
- Debugged phoneme trimming using manual inspection  
- Refactored scoring to return numeric values instead of boolean  

## Outcome  
The engine now supports:
- Exact rhyme detection  
- Similarity-based phonetic matching  
- Threshold-driven rhyme scoring  

Core phonetic engine layer completed.


---

# Devlog — Day 5

## Goal  
Move from word-level rhyme lookup to line-level rhyme detection.

## What I Built  
- Implemented `analyze_line(line)`  
- Normalized and tokenized input text  
- Extracted rhyme segments for each word  
- Properly handled multiple pronunciations  
- Compared word pairs using similarity scoring  
- Returned rhyming word pairs within a line  

### Example

Input:
"I smoke fire while the mic gets stoked"

Output:
{('smoke', 'stoked')}

## Key Concepts Learned  
- Managing multi-pronunciation dictionary structures  
- Pairwise comparison logic (O(k²) for line words)  
- Proper dictionary-to-list conversion for indexed comparison  
- Early-exit optimization during pronunciation matching  

## Problems Faced  
- Overwriting pronunciations instead of storing multiple  
- Incorrect dictionary iteration logic  
- Handling missing stress cases  

## Solutions Implemented  
- Stored trimmed phoneme segments as lists per word  
- Converted dictionary items to list for controlled indexing  
- Added stress-index validation guards  

## Outcome  
The engine now supports:
- Word-level rhyme lookup  
- Similarity-based rhyme scoring  
- Internal rhyme detection within a line  

Project has transitioned from a rhyme lookup tool to a functional rhyme analysis system.

---

# Devlog — Day 6

## Goal  
Move from pair-based rhyme detection to structured rhyme grouping within a line.

## What I Built  
- Designed and implemented `rhyme_section(p1, p2)` to extract the actual matched phoneme segment between two words.
- Shifted grouping logic from pair connectivity to shared phonetic overlap.
- Used matched phoneme segment (e.g., `"IH1 L"`) as a grouping key.
- Built clustering logic inside `analyze_line(line)` using a dictionary:
  - Key → matched rhyme segment  
  - Value → set of words sharing that segment
- Returned structured rhyme clusters instead of raw pairs.

## Example

- Input: "Chin checker chinchilla till it was filler"
- Output:
[['chinchilla', 'till', 'filler']]
- Instead of:
{('chinchilla','till'), ('chinchilla','filler'), ('till','filler')}


## Key Concepts Learned  
- Difference between pair-based grouping and segment-based clustering  
- Why phonetic overlap is a better grouping key than graph traversal for rhyme detection  
- Importance of returning structured data instead of intermediate representations  
- Using dictionary keys derived from computed phoneme segments  

## Problems Faced  
- Initially storing phoneme segments instead of words in clusters  
- Forgetting to initialize dictionary keys before appending  
- Redundant calls to `rhyme_score` and `rhyme_section`  
- Handling multiple pronunciations cleanly  

## Solutions Implemented  
- Modified `rhyme_section` to return the best matched phoneme segment  
- Used `" ".join(segment)` as cluster key  
- Stored grouped words in sets to avoid duplicates  
- Converted final dictionary values into list format for clean output  

## Outcome  
The engine now supports:
- Word-level rhyme lookup  
- Similarity-based scoring  
- Line-level rhyme detection  
- Structured rhyme grouping based on shared phonetic segments  

Project has evolved from detecting rhyme pairs to producing meaningful rhyme clusters suitable for highlighting and UI integration.

