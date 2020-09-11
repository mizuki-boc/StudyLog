# coding: utf-8

'''
実行で，git に自動コミット + index.md の目次作成
'''
import subprocess

def git_commit():
    result = subprocess.run(["git", "add", "."])
    print(result)
    result = subprocess.run(["git", "commit", "-m", "\"auto commit test\""])
    print(result)
    result = subprocess.run(["git", "push", "origin"])
    print(result)

if __name__ == '__main__':
    git_commit()
    