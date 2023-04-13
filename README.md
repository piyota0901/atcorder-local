# atcorder-local
AtCoderのローカル環境リポジトリ
[参考にした記事](https://zenn.dev/dri_cro_6663/scraps/064296ba53e0d6)
## Tools
---
- poetry
- online-judge-tools
- atcorder-cli

## Setting
---
```powershell
$pyenv install 3.10.8
$.env\Script\activate
$poetry init
$poetry install
$poetry add online-judge-tools
```

```powershell
$oj login https://atcoder.jp

$npx acc login
```

## online-judge-tools
---

- 問題のダウンロード
    ```powershell
    npx acc new <問題ID> --template python
    ```

- テスト実行
    ```powershell
    cd xxx/a
    oj t -c "python3 main.py"
    ```

- 提出
    ```powershell
    cd xxx/a
    npx acc submit # ← --template pythonで作成したもの
    npx acc submit ./main.py # ← --template pythonを使用しなかったもの
    ```