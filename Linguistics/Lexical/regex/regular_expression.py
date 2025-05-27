import re

# Define a dictionary of named regular expressions
regex_patterns = {
    "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "phone": r"\+?\d{1,3}?[-.\s]?\(?\d{2,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{3,4}",
    "url": r"https?://(?:www\.)?[a-zA-Z0-9./_-]+",
    "ipv4": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    "date": r"\b\d{2}-\d{2}-\d{4}\b",
    "postal_code": r"\b\d{5}(?:-\d{4})?\b",  # US-style
    "word": r"\b\w+\b",
}

if __name__ == '__main__':
    text = "Contact us at hello@example.com or visit https://openai.com on 27-05-2025."

    email_matches = re.findall(regex_patterns["email"], text)
    url_matches = re.findall(regex_patterns["url"], text)
    date_matches = re.findall(regex_patterns["date"], text)

    print("Emails:", email_matches)
    print("URLs:", url_matches)
    print("Dates:", date_matches)

