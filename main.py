from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from github_client import GitHubClient
from ai_client import AIClient
from data_model import GitHubCVData
from schemas import CVRequest, CVResponse

app = FastAPI()


class Preferences(BaseModel):
    username: str
    preferences: dict


async def fetch_github_data(username: str) -> GitHubCVData:
    client = GitHubClient()
    user = await client.get_user(username)
    repos = await client.get_repos(username)
    language_stats = await client.get_language_stats(username)
    return GitHubCVData(user, repos, language_stats)


@app.post("/generate-cv", response_model=CVResponse)
async def generate_cv(request: CVRequest):
    client = GitHubClient()
    user = await client.get_user(request.github_username)

    if not user:
        raise HTTPException(status_code=404, detail="GitHub user not found")
    repos = await client.get_repos(request.github_username)
    language_stats = await client.get_language_stats(request.github_username)
    cv_data = GitHubCVData(user, repos, language_stats)

    from prompt_builder import build_prompt
    prompt = build_prompt(cv_data, request.preferences.dict()
                          if request.preferences else {})

    ai_client = AIClient()
    cv_text = await ai_client.generate_text(prompt)

    return CVResponse(cv_text=cv_text)
