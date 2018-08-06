# SQL

## SELECT
```
SELECT column1, column2 from database_table
```
- データの取得。
- 全カラムの取得は`SELECT * from database_table`

## LENGTH
```
LENGTH(string)
```
- stringの長さを数値で返す。

## WHERE
```
SELECT column from database_table
    WHERE conditions
```
- 絞り込みを行う。
- 例: 今回の例では、adminのパスワードを表示したいので、`WHERE id='admin'`となる。

## SUBSTR
```
SUBSTR(string, start, length)
```
- 部分文字列をstringで返す。
- 1-indexedでスタート位置を指定する。

# コメント
` --`
- 以降に続くものをすべてコメント扱いにする。