from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import date


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


class EducationItem(BaseModel):
    school_name: str
    degree: Optional[str] = None
    field_of_study: Optional[str] = None
    start_date: str
    end_date: Optional[str] = None
    description: Optional[str] = None


class WorkExperienceItem(BaseModel):
    position: str
    company_name: str
    start_date: str
    end_date: Optional[str] = None
    description: Optional[str] = None


class CertificateItem(BaseModel):
    name: str
    issuer: Optional[str] = None
    date_obtained: Optional[str] = None
    description: Optional[str] = None


class CVRequest(BaseModel):
    github_username: str = Field(..., example="janedoe")
    preferences: Optional[UserPreferences] = UserPreferences()

    education: Optional[List[EducationItem]] = [
        EducationItem(
            school_name="",
            degree="",
            field_of_study="",
            start_date="",
            end_date="",
            description=""
        )
    ]
    work_experience: Optional[List[WorkExperienceItem]] = [
        WorkExperienceItem(
            position="",
            company_name="",
            start_date="",
            end_date="",
            description=""
        )
    ]
    certificates: Optional[List[CertificateItem]] = [
        CertificateItem(
            name="",
            issuer="",
            date_obtained="",
            description=""
        )
    ]


class CVResponse(BaseModel):
    cv_text: str
