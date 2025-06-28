import re
import requests

DOCKERFILE_PATH = "Dockerfile"
PYTHON_VERSION_PREFIX = "3.12"

def get_latest_patch_version(prefix):
    url = "https://www.python.org/ftp/python/"
    resp = requests.get(url)
    versions = re.findall(r'href="(\d+\.\d+\.\d+)/"', resp.text)
    patch_versions = [v for v in versions if v.startswith(prefix)]
    patch_versions.sort(key=lambda s: list(map(int, s.split('.'))))
    return patch_versions[-1] if patch_versions else None

def update_dockerfile(latest_version):
    with open(DOCKERFILE_PATH, "r") as f:
        content = f.read()
    new_content = re.sub(
        r'ENV PYTHON_VERSION=3\.12\.\d+',
        f'ENV PYTHON_VERSION={latest_version}',
        content
    )
    with open(DOCKERFILE_PATH, "w") as f:
        f.write(new_content)

if __name__ == "__main__":
    latest = get_latest_patch_version(PYTHON_VERSION_PREFIX)
    if not latest:
        print("Could not find latest Python 3.12 patch version.")
        exit(1)
    update_dockerfile(latest)
    print(f"Updated Dockerfile to Python {latest}")