#!/usr/bin/env python3
"""
Word counting and reading time estimation utility for course content.

This script provides deterministic word counts and reading time estimates,
removing the need for Claude to estimate these metrics.
"""

import re
import sys
from pathlib import Path


def count_words(text: str) -> int:
    """
    Count words in text, excluding markdown syntax and code blocks.

    Args:
        text: Markdown content

    Returns:
        Word count (int)
    """
    # Remove code blocks
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'`[^`]+`', '', text)

    # Remove markdown links but keep link text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)

    # Remove markdown images
    text = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', '', text)

    # Remove HTML comments (customization markers)
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)

    # Remove markdown headers (#, ##, etc.)
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)

    # Remove emphasis markers (*, _, **, __)
    text = re.sub(r'[*_]{1,2}([^*_]+)[*_]{1,2}', r'\1', text)

    # Remove horizontal rules
    text = re.sub(r'^---+$', '', text, flags=re.MULTILINE)

    # Count words (split on whitespace)
    words = text.split()
    return len(words)


def estimate_reading_time(word_count: int, wpm: int = 200) -> dict:
    """
    Estimate reading time based on word count.

    Args:
        word_count: Number of words
        wpm: Words per minute (default 200 for technical content)

    Returns:
        Dict with minutes and seconds
    """
    total_seconds = (word_count / wpm) * 60
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)

    return {
        'minutes': minutes,
        'seconds': seconds,
        'total_seconds': int(total_seconds),
        'formatted': f"{minutes}:{seconds:02d}"
    }


def analyze_length(word_count: int) -> dict:
    """
    Analyze if content length is appropriate (300-600 words target).

    Args:
        word_count: Number of words

    Returns:
        Dict with assessment and score
    """
    if 300 <= word_count <= 600:
        score = 2
        assessment = "Optimal length"
        message = f"{word_count} words - perfect for microlearning (3-5 min)"
    elif 250 <= word_count < 300 or 600 < word_count <= 700:
        score = 1
        if word_count < 300:
            assessment = "Slightly short"
            message = f"{word_count} words - could add ~{300 - word_count} words for optimal depth"
        else:
            assessment = "Slightly long"
            message = f"{word_count} words - consider trimming ~{word_count - 600} words to reduce cognitive load"
    else:
        score = 0
        if word_count < 250:
            assessment = "Too short"
            message = f"{word_count} words - needs ~{300 - word_count} more words to feel complete"
        else:
            assessment = "Too long"
            message = f"{word_count} words - consider breaking into multiple sections or trimming {word_count - 600} words"

    return {
        'score': score,
        'assessment': assessment,
        'message': message,
        'word_count': word_count
    }


def main():
    """CLI interface for word counting."""
    if len(sys.argv) < 2:
        print("Usage: python count_words.py <file_path>")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    word_count = count_words(content)
    reading_time = estimate_reading_time(word_count)
    length_analysis = analyze_length(word_count)

    print(f"📊 CONTENT LENGTH ANALYSIS: {file_path.name}")
    print(f"\nWord Count: {word_count}")
    print(f"Reading Time: {reading_time['formatted']} ({reading_time['minutes']} min {reading_time['seconds']} sec)")
    print(f"\nLength Assessment: {length_analysis['assessment']} (Score: {length_analysis['score']}/2)")
    print(f"→ {length_analysis['message']}")


if __name__ == '__main__':
    main()
