"""
Personal Reddit research script for analyzing public discussions
about SBIR (Small Business Innovation Research) and federal grants.

READ-ONLY tool. Does not post, comment, vote, or interact with users.
Aggregates public posts/comments for offline personal study.
"""

import os
import praw
from datetime import datetime

# Load credentials from environment variables (never hardcoded)
reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent="grant-research-tool/0.1 by /u/YOUR_USERNAME",
)

# Read-only mode (no write operations possible)
reddit.read_only = True

# Subreddits to research
TARGET_SUBREDDITS = [
    "Entrepreneur",
    "smallbusiness",
    "startups",
    "grants",
    "govcontracting",
    "EdTech",
]

# Search queries related to SBIR / federal grants
SEARCH_QUERIES = [
    "SBIR Phase I",
    "NSF SBIR",
    "federal grant startup",
    "non-dilutive funding",
]


def search_subreddit(subreddit_name: str, query: str, limit: int = 25):
    """Read-only search of public posts in a subreddit."""
    subreddit = reddit.subreddit(subreddit_name)
    results = []
    for submission in subreddit.search(query, limit=limit):
        results.append({
            "title": submission.title,
            "author": str(submission.author),
            "score": submission.score,
            "url": submission.url,
            "created": datetime.fromtimestamp(submission.created_utc).isoformat(),
            "selftext": submission.selftext[:500],  # Preview only
        })
    return results


def main():
    """Aggregate research data to local markdown file."""
    output = []
    for subreddit in TARGET_SUBREDDITS:
        for query in SEARCH_QUERIES:
            print(f"Searching r/{subreddit} for '{query}'...")
            results = search_subreddit(subreddit, query, limit=10)
            output.extend(results)

    # Save to local file for offline reading
    with open("research_output.md", "w") as f:
        for r in output:
            f.write(f"## {r['title']}\n")
            f.write(f"**r/{r.get('subreddit', '')}** | u/{r['author']} | "
                    f"score: {r['score']} | {r['created']}\n\n")
            f.write(f"{r['selftext']}\n\n")
            f.write(f"[Source]({r['url']})\n\n---\n\n")

    print(f"Saved {len(output)} threads to research_output.md")


if __name__ == "__main__":
    main()
