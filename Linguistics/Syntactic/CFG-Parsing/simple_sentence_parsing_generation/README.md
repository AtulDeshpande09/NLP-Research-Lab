# CFG-Based NLP Parser & Sentence Generator

## Introduction
This project is a **Context-Free Grammar (CFG) based NLP parser and generator** designed to analyze and construct grammatically correct English sentences. Unlike traditional dependency parsers, this system is built from scratch using **Recursive Descent Parsing (RDP)**, enabling both sentence validation and structured sentence generation.

## Features
- **CFG-Based Parsing:** Validates sentence structures based on defined grammar rules.
- **Support for All Tenses:** Covers present, past, and future tenses.
- **Recursive Descent Implementation:** Hand-crafted parsing logic without relying on external libraries.
- **Potential for Sentence Generation:** Future scope includes CFG-driven text synthesis.

## Why This Project?
In Natural Language Processing (NLP), CFG serves as a fundamental concept for syntactic analysis. While modern parsers like Stanford NLP and spaCy focus on statistical approaches, rule-based methods like CFG still play a critical role in **linguistic validation, low-resource language processing, and hybrid NLP models**.

## Usage
### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd <repo-folder>
```
### 2. Run the Parser
```sh
python parser.py "A cat sees a mouse"
```
Output:
```
Word to parse ---> A
Word to parse ---> cat
Parsed noun part!!
Word to parse ---> sees
Word to parse ---> a
Word to parse ---> mouse
Parsed verb part!!
Sentence Parsed Successfully!!
```

## Future Work
- **Sentence Generation:** CFG-based structured text generation.
- **Multi-Language Support:** Expansion to other languages (e.g., Marathi, Hindi).
- **Probabilistic CFG (PCFG):** Assigning probabilities to grammar rules for better sentence modeling.

## Contributing
We welcome contributions! Feel free to open an issue or submit a pull request.

## License
This project is open-source under the MIT License.

