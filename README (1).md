![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)
![GitHub API](https://img.shields.io/badge/GitHub-API-181717?logo=github&logoColor=white)
![CLI](https://img.shields.io/badge/CLI-Tool-black?logo=windowsterminal&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

# 🐙 GitHub Profile Analyzer

> A Python CLI tool that analyzes any GitHub profile and generates a detailed report — top languages, best repositories, followers, and an overall profile score out of 100.

## ✨ Features

- 👤 Complete profile overview (bio, location, followers)
- 💻 Top programming languages used across all repos
- ⭐ Top repositories ranked by stars
- 📊 Profile score out of 100 with detailed breakdown
- 💡 Actionable suggestions to improve your profile
- 🚀 Works with any public GitHub username

## 📋 Prerequisites

- Python 3.9+

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/Git-Ninja-afk/github-profile-analyzer.git
cd github-profile-analyzer

# Install dependencies
pip install -r requirements.txt

# Run the analyzer
python analyzer.py
```

## 🎮 Usage

```bash
🐙 GITHUB PROFILE ANALYZER
============================================================
Enter GitHub username to analyze: Git-Ninja-afk

🔍 Analyzing GitHub profile: @Git-Ninja-afk
============================================================

👤 NAME: Bosco
📍 LOCATION: New Delhi, India
📝 BIO: CS @ DTU | Python • TypeScript | Open Source
👥 FOLLOWERS: 12
📦 PUBLIC REPOS: 5

💻 TOP LANGUAGES
------------------------------
Python          ████ (4 repos)
TypeScript      ██ (2 repos)

⭐ TOP REPOSITORIES
------------------------------
• Finguard — ⭐5 | 🍴2 | TypeScript
• SDG-Gamification — ⭐3 | 🍴1 | Python

📊 PROFILE SCORE
------------------------------
✅ Has profile picture (+10)
✅ Has bio (+15)
✅ Has location (+10)
❌ No website (-10)

🏆 TOTAL SCORE: 72/100
👍 Good profile! A few improvements needed.
```

## 📁 Project Structure

```
github-profile-analyzer/
├── analyzer.py       # Main application
├── requirements.txt  # Dependencies
├── .gitignore        # Git ignore rules
└── README.md         # Documentation
```

## 🗺️ Roadmap

- [ ] Export report as PDF
- [ ] Compare two GitHub profiles
- [ ] Contribution graph analysis
- [ ] GitHub Actions integration

## 👨‍💻 About

Built to practice Python, REST API integration, and data analysis using the GitHub API.

## 📜 License

MIT License
