# coding: utf-8

'''
実行で，git に自動コミット + index.md の目次作成
'''
import codecs
import datetime
import os
import subprocess
import pathlib
import glob

TREE_TXT_FILE="index.md"

def auto_commit(commit_message=datetime.datetime.now().strftime("%Y/%m/%d") + " " + datetime.datetime.now().strftime("%X")):
    result = subprocess.run(["git", "add", "."])
    print(result)
    commit_message = "AUTO COMMIT AT: " + commit_message
    result = subprocess.run(["git", "commit", "-m", commit_message])
    print(result)
    result = subprocess.run(["git", "push", "origin"])
    print(result)
    print(commit_message)

def tree(path, layer=0, is_last=False, indent_current='　'):

    if not pathlib.Path(path).is_absolute():
        path = str(pathlib.Path(path).resolve())

    # カレントディレクトリの表示
    current = path.split('/')[::-1][0]
    if layer == 0:
        print(current, sep="\n", file=codecs.open(TREE_TXT_FILE, 'a', 'utf-8'))
    else:
        branch = '└' if is_last else '├'
        print('{indent}{branch}{dirname}'.format(indent=indent_current, branch=branch, dirname=current), sep="\n", file=codecs.open(TREE_TXT_FILE, 'a', 'utf-8'))

    # 下の階層のパスを取得
    paths = [p for p in glob.glob(path+'/*') if os.path.isdir(p) or os.path.isfile(p)]
    def is_last_path(i):
        return i == len(paths)-1

    # 再帰的に表示
    for i, p in enumerate(paths):
        indent_lower = indent_current
        if layer != 0:
            indent_lower += '　　' if is_last else '│　'

        if os.path.isfile(p):
            branch = '└' if is_last_path(i) else '├'
            # +9 は StudyLog/ の 9文字分差し引く意味
            print('{indent}{branch}[{filename}]({link})'.format(indent=indent_lower, branch=branch, filename=p.split('/')[::-1][0], link=p[p.find("StudyLog/")+9:]), sep="\n", file=codecs.open(TREE_TXT_FILE, 'a', 'utf-8'))
        if os.path.isdir(p):
            tree(p, layer=layer+1, is_last=is_last_path(i), indent_current=indent_lower)

if __name__ == '__main__':
    # クリアする
    f = open(TREE_TXT_FILE, "w")
    f.write("## 目次\n")
    f.close()
    # 書き込む
    tree(path=os.path.dirname(os.path.abspath(__file__)))

    auto_commit()
