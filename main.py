#!/usr/bin/env python3

import re

text = """
Contact us at support@company.com or sales@shop.org.
Visit our websites: https://www.company.com, http://blog.shop.org/page.
Call us at (555) 123-4567 or 555-987-6543.
Our products cost $19.99, $1,234.50, and $99.
"""
patterns = {
    "emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "urls": r"https?://[^\s,]+",
    "phone_numbers": r"(\(\d{3}\)\s*|\d{3}-)\d{3}-\d{4}",
    "currency": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
}

for name, pattern in patterns.items():
    matches = re.findall(pattern, text)
    print(f"{name}: {matches}")
