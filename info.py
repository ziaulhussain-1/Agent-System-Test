"""Print the repository name and today's date."""

from datetime import date
from pathlib import Path


def main():
    repo_name = Path(__file__).resolve().parent.name
    print(f"Repository: {repo_name}")
    print(f"Date: {date.today().isoformat()}")


if __name__ == "__main__":
    main()
