from pydantic import BaseModel, Field
from typing import List, Optional, Literal


class UserPreferences(BaseModel):
    style: Literal["modern", "classic", "minimal"] = "modern"
    language: Literal["en", "pl"] = "en"
    tone: Literal["formal", "casual"] = "formal"

    include_repos: bool = True
    max_repos: Optional[int] = 3
    filter_by_language: Optional[List[str]] = None

    include_profile_bio: bool = True
    include_top_languages: bool = True
    include_repo_stats: bool = False


class CVRequest(BaseModel):
    github_username: str = Field(..., example="janedoe")
    preferences: Optional[UserPreferences] = UserPreferences()


class CVResponse(BaseModel):
    cv_text: str
