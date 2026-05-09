import requests
import json
from datetime import datetime

def get_user_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 404:
        print(f"❌ User '{username}' not found!")
        return None
    return response.json()

def get_user_repos(username):
    url = f"https://api.github.com/users/{username}/repos?per_page=100&sort=updated"
    response = requests.get(url)
    return response.json()

def analyze_languages(repos):
    languages = {}
    for repo in repos:
        if repo.get("language"):
            lang = repo["language"]
            languages[lang] = languages.get(lang, 0) + 1
    return dict(sorted(languages.items(), key=lambda x: x[1], reverse=True))

def get_top_repos(repos, n=5):
    return sorted(repos, key=lambda x: x.get("stargazers_count", 0), reverse=True)[:n]

def calculate_profile_score(profile, repos):
    score = 0
    reasons = []

    if profile.get("avatar_url"):
        score += 10
        reasons.append("✅ Has profile picture (+10)")
    else:
        reasons.append("❌ No profile picture (-10)")

    if profile.get("bio"):
        score += 15
        reasons.append("✅ Has bio (+15)")
    else:
        reasons.append("❌ No bio (-15)")

    if profile.get("location"):
        score += 10
        reasons.append("✅ Has location (+10)")
    else:
        reasons.append("❌ No location (-10)")

    if profile.get("blog"):
        score += 10
        reasons.append("✅ Has website/portfolio (+10)")
    else:
        reasons.append("❌ No website (-10)")

    repo_count = len(repos)
    if repo_count >= 10:
        score += 20
        reasons.append(f"✅ Has {repo_count} repositories (+20)")
    elif repo_count >= 5:
        score += 10
        reasons.append(f"⚠️ Has {repo_count} repositories (+10)")
    else:
        reasons.append(f"❌ Only {repo_count} repositories (-0)")

    total_stars = sum(r.get("stargazers_count", 0) for r in repos)
    if total_stars >= 50:
        score += 20
        reasons.append(f"✅ {total_stars} total stars (+20)")
    elif total_stars >= 10:
        score += 10
        reasons.append(f"⚠️ {total_stars} total stars (+10)")
    else:
        reasons.append(f"❌ {total_stars} total stars (+0)")

    followers = profile.get("followers", 0)
    if followers >= 50:
        score += 15
        reasons.append(f"✅ {followers} followers (+15)")
    elif followers >= 10:
        score += 8
        reasons.append(f"⚠️ {followers} followers (+8)")
    else:
        reasons.append(f"❌ {followers} followers (+0)")

    return score, reasons

def print_report(username):
    print(f"\n🔍 Analyzing GitHub profile: @{username}")
    print("=" * 60)

    profile = get_user_profile(username)
    if not profile:
        return

    repos = get_user_repos(username)

    # Basic Info
    print(f"\n👤 NAME: {profile.get('name', 'Not set')}")
    print(f"📍 LOCATION: {profile.get('location', 'Not set')}")
    print(f"🔗 WEBSITE: {profile.get('blog', 'Not set')}")
    print(f"📝 BIO: {profile.get('bio', 'Not set')}")
    print(f"👥 FOLLOWERS: {profile.get('followers', 0)}")
    print(f"👣 FOLLOWING: {profile.get('following', 0)}")
    print(f"📦 PUBLIC REPOS: {profile.get('public_repos', 0)}")

    joined = profile.get('created_at', '')
    if joined:
        joined_date = datetime.strptime(joined, "%Y-%m-%dT%H:%M:%SZ").strftime("%B %Y")
        print(f"📅 JOINED: {joined_date}")

    # Languages
    print(f"\n💻 TOP LANGUAGES")
    print("-" * 30)
    languages = analyze_languages(repos)
    for lang, count in list(languages.items())[:5]:
        bar = "█" * count
        print(f"{lang:<15} {bar} ({count} repos)")

    # Top Repos
    print(f"\n⭐ TOP REPOSITORIES")
    print("-" * 30)
    top_repos = get_top_repos(repos)
    for repo in top_repos:
        print(f"• {repo['name']} — ⭐{repo['stargazers_count']} | 🍴{repo['forks_count']} | {repo.get('language', 'N/A')}")

    # Profile Score
    print(f"\n📊 PROFILE SCORE")
    print("-" * 30)
    score, reasons = calculate_profile_score(profile, repos)
    for reason in reasons:
        print(reason)
    print(f"\n🏆 TOTAL SCORE: {score}/100")

    if score >= 80:
        print("🔥 Excellent profile! Ready for open source.")
    elif score >= 60:
        print("👍 Good profile! A few improvements needed.")
    elif score >= 40:
        print("⚠️ Average profile. Work on the missing items.")
    else:
        print("❌ Needs significant improvement.")

def main():
    print("🐙 GITHUB PROFILE ANALYZER")
    print("=" * 60)
    username = input("Enter GitHub username to analyze: ").strip()
    print_report(username)
    print("\n✅ Analysis complete!")

if __name__ == "__main__":
    main()
