from jinja2 import Environment, FileSystemLoader
import os

env = Environment(loader=FileSystemLoader(
    os.path.join(os.path.dirname(__file__), 'templates')))


def build_prompt(cv_data, preferences):
    template = env.get_template('prompt_template.txt')
    return template.render(
        user=cv_data.user,
        repos=cv_data.repos,
        language_stats=cv_data.language_stats,
        education=cv_data.education,
        work_experience=cv_data.work_experience,
        certificates=cv_data.certificates,
        preferences=preferences,
        language=preferences.get("language", "polskim")
    )
