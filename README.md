# Reddit Grants Research Tool

Personal read-only Python script using PRAW (Python Reddit API Wrapper)
to aggregate publicly available discussions about SBIR (Small Business
Innovation Research) programs and federal grants for personal study.

## Purpose
Learn from real founder experiences shared in public Reddit threads
about navigating federal small business grants and non-dilutive funding.

## Capabilities
- READ-ONLY access to public posts and comments
- Multi-subreddit aggregation
- Local markdown output for offline reading

## What it does NOT do
- Does not post, comment, or vote
- Does not send messages to users
- Does not collect personal information beyond what is publicly visible
- Does not redistribute content commercially

## Usage
1. Set environment variables: `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`
2. Update `user_agent` in `main.py` with your Reddit username
3. Run: `python main.py`

## Built with
- [PRAW](https://github.com/praw-dev/praw) — official Python Reddit API wrapper
