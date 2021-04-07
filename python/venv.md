# python 仮想環境まとめ
仮想環境に入る際によく困るのでまとめ
___

- Windows で仮想環境に入ろうとしたとき、

```
.\venv\Scripts\activate : このシステムではスクリプトの実行が無効になっているため、ファイル C:\Users\mizuk\Desktop\proje
ct\kakeibo\venv\Scripts\Activate.ps1 を読み込むことができません。詳細については、「about_Execution_Policies」(https://g
o.microsoft.com/fwlink/?LinkID=135170) を参照してください。
+ .\venv\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : セキュリティ エラー: (: ) []、PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```
こんな感じのエラーメッセージがでてきた。[Windows PowerShellでPythonの仮想環境をactivateできないときの対処法](https://toypool.hatenablog.com/entry/2019/02/08/142824)に従って解決。