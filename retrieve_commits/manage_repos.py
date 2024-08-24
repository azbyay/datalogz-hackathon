import os
import subprocess

# List of targeted repositories
targeted_repos = [
    'https://github.com/openai/gpt-3.git'
]

def run_script_in_repo(repo_url):
    script_path = 'retrieve_commits/collect_commit_data.py'
    result = subprocess.run(['python3', script_path, repo_url], capture_output=True, text=True)
    print(f"Script output for {repo_url}: {result.stdout}")

def main():
    for repo in targeted_repos:
        # if os.path.exists(os.path.join(repo, '.git')):
        print(f"Running script in {repo}")
        run_script_in_repo(repo)
        # else:
        #     print(f"{repo} is not a valid Git repository")

if __name__ == "__main__":
    main()
