class GithubUser:
    def __init__(self, username, full_name, bio, location, blog_url, public_repos, created_at):
        self.username = username
        self.full_name = full_name
        self.bio = bio
        self.location = location
        self.blog_url = blog_url
        self.public_repos = public_repos
        self.created_at = created_at


class GithubRepo:
    def __init__(self, name, description, language, stars, forks, created_at, is_fork):
        self.name = name
        self.description = description
        self.language = language
        self.stars = stars
        self.forks = forks
        self.created_at = created_at
        self.is_fork = is_fork


class LanguageStats:
    def __init__(self, language, percentage):
        self.language = language
        self.percentage = percentage


class Education:
    def __init__(self, school_name, field_of_study, start_date, end_date=None, description=None):
        self.school_name = school_name
        self.field_of_study = field_of_study
        self.start_date = start_date
        self.end_date = end_date
        self.description = description


class Certificate:
    def __init__(self, name, issuer, issue_date, expiration_date=None, credential_url=None):
        self.name = name
        self.issuer = issuer
        self.issue_date = issue_date
        self.expiration_date = expiration_date
        self.credential_url = credential_url


class WorkExperience:
    def __init__(self, company_name, position, start_date, end_date=None, description=None):
        self.company_name = company_name
        self.position = position
        self.start_date = start_date
        self.end_date = end_date
        self.description = description


class GitHubCVData:

    def __init__(self, user, repos, language_stats, education=None, work_experience=None, certificates=None):

        self.user = user
        self.repos = repos
        self.language_stats = language_stats
        self.education = education or []
        self.work_experience = work_experience or []
        self.certificates = certificates or []
