## heroku デプロイ時にユニコードエラーが表示される際の解決方法
プッシュしようとすると、以下のようなエラーコードが表示される
```
Enumerating objects: 1864, done.
Counting objects: 100% (1864/1864), done.
Delta compression using up to 16 threads
Compressing objects: 100% (1832/1832), done.
Writing objects: 100% (1864/1864), 6.64 MiB | 2.57 MiB/s, done.
Total 1864 (delta 284), reused 0 (delta 0), pack-reused 0
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Building on the Heroku-20 stack
remote: -----> Using buildpack: heroku/python
remote: -----> Python app detected
remote: Traceback (most recent call last):
remote:   File "/tmp/codon/tmp/buildpacks/0f40890b54a617ec2334fac0439a123c6a0c1136/vendor/runtime-fixer", line 8, in <module>
remote:     r = f.read().strip()
remote:   File "/usr/lib/python3.8/codecs.py", line 322, in decode
remote:     (result, consumed) = self._buffer_decode(data, self.errors, final)
remote: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid 
start byte
remote: /tmp/codon/tmp/buildpacks/0f40890b54a617ec2334fac0439a123c6a0c1136/bin/steps/python: line 5: warning: command substitution: ignored null byte in input
remote: ) is not available for this stack (heroku-20).
remote:  !     Aborting.  More info: https://devcenter.heroku.com/articles/python-support
remote:  !     Push rejected, failed to compile Python app.
remote:
remote:  !     Push failed
remote:
remote:
To https://git.heroku.com/discord-apexinfo-bot.git
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/discord-apexinfo-bot.git'
```
VScode 内の右下のエンコード(?)選択のとこが utf-16 になってた。utf-8 に変更でデプロイ成功。