# 或曰

## Contents

GitHub ページで公開している [ブログ](https://blog2.issei.org/) のテキスト、
ならびに関連ツール。

## Install

### Prerequisite
* [Git](https://git-scm.com/)
* [Ruby](https://www.ruby-lang.org) 2.5 or newer
* [Bundler](https://bundler.io/)

### Retrieve the repository

```
% git clone git@github.com:isseis/isseis.github.io
% cd isseis.github.io
% cp _tools/hooks/* .git/hooks
% bundle update
```

## Start Jekyll server locally

```
% _tools/start.sh
```
Webブラウザを起動して http://localhost:4000/ にアクセス。

## Directory

| directory | contents |
| - | - |
| _tools  | オフラインで使用するツール類 |
| _tools/hooks  | Git のフックファイル（.git/hoooks にコピーして使用） |
| _tools/test   | _tools 以下のプログラムのテスト関連ファイル |

これ以外のディレクトについては [Jekyll](https://jekyllrb.com/) のドキュメントを参照。
