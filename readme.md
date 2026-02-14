# Rhyme AI

Phoneme-based rhyme detection and flow analysis engine built using the CMU Pronouncing Dictionary.  
Designed to analyze lyrical structure, detect rhyme patterns, and evaluate rhythmic flow in songs.

---

## Core Features

- Stress-based rhyme extraction (using phoneme stress markers)
- Multiple pronunciation handling (CMUdict variants)
- Automatic rhymes highlighting
- Clean modular architecture for scalability
- Git version-controlled development workflow

---

## Rhyme Types Supported / Planned

The engine is designed to detect and analyze:

### 1. Perfect Rhyme
Exact phoneme match from the last stressed vowel onward  
Example: *cat – hat – bat*

### 2. Identical Rhyme
Exact phoneme match including onset  
Example: *leave – leave*

### 3. Slant (Near) Rhyme
Partial phoneme similarity  
Example: *made – wait*

### 4. Multisyllabic Rhyme
Matching across multiple syllables  
Example: *overseas – total ease*

### 5. Internal Rhyme
Rhymes occurring within the same lyrical line.

### 6. End Rhyme
Rhymes occurring at the end of lyrical lines.

### 7. Assonance
Similarity in vowel sounds  
Example: *light – time*

### 8. Consonance
Repetition of consonant sounds  
Example: *blank – think*

---

## Tech Stack

- Python  
- CMU Pronouncing Dictionary (CMUdict)  
- Phoneme-based stress modeling  
- Git & GitHub  

---

## Future Work

- Rhyme strength scoring system
- Flow similarity detection between songs
- Stress pattern comparison across lyrics
- Flow-based music recommendation model
- Automatic rhyme highlighting in lyrics
- Music / rap generation support
- Performance optimization & caching

---

## Long-Term Vision

To build a flow-aware lyrical intelligence engine capable of:

- Detecting complex rhyme schemes
- Quantifying lyrical density
- Comparing artist flow styles
- Supporting AI-assisted music creation
