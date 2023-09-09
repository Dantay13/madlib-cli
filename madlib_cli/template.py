import re


def parse_template(text):
    parts = re.findall(r"{(.*?)}", text)
    stripped_text = re.sub(r"{(.*?)}", "{}", text)
    return stripped_text, tuple(parts)


def merge(template, words):
    return template.format(*words)
