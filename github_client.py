import httpx
from typing import Optional
from collections import defaultdict

GITHUB_API_URL = "https://api.github.com/users/"


class GitHubClient:
    def __init__(self):
        self.base_url = GITHUB_API_URL

    async def get_user(self, username: str) -> Optional[dict]:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}{username}")
            print("GitHub API status:", response.status_code)
            if response.status_code == 200:
                return response.json()
            return None

    async def get_repos(self, username: str) -> Optional[list]:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}{username}/repos")
            if response.status_code == 200:
                return response.json()
            return None

    async def get_language_stats(self, username: str) -> dict:
        async with httpx.AsyncClient() as client:
            repos_resp = await client.get(f"{self.base_url}{username}/repos")
            if repos_resp.status_code != 200:
                return None
            repos = repos_resp.json()

            language_totals = defaultdict(int)

            for repo in repos:
                repo_name = repo["name"]
                lang_resp = await client.get(f"{self.base_url}{username}/{repo_name}/languages")
                if lang_resp.status_code == 200:
                    langs = lang_resp.json()
                    for lang, bytes_count in langs.items():
                        language_totals[lang] += bytes_count

            total_bytes = sum(language_totals.values())
            if total_bytes == 0:
                return {}

            language_percentages = {
                lang: round((count / total_bytes) * 100, 2)
                for lang, count in language_totals.items()
            }

            return language_percentages
