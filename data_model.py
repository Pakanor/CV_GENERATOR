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


class GitHubCVData:

    def __init__(self, user, repos, language_stats):
        self.user = user
        self.repos = repos
        self.language_stats = language_stats
