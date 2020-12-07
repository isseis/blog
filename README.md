# 或曰

## Contents

[ブログ](https://blog2.issei.org/) のテキスト、
ならびに関連ツール跡地。

2020年12月にサイト構築ツールを [Hugo](https://gohugo.io/) に変更し、
リポジトリを https://github.com/isseis/blog-hugo に移動しました。

## Install

### Prerequisite
* [Git](https://git-scm.com/)
* [Ruby](https://www.ruby-lang.org) 2.5 or newer
* [Bundler](https://bundler.io/)

### Retrieve the repository

```
% git clone git@github.com:isseis/blog.git
% cd blog
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
| \_tools  | オフラインで使用するツール類 |
| \_tools/hooks  | Git のフックファイル（.git/hoooks にコピーして使用） |
| \_tools/test   | \_tools 以下のプログラムのテスト関連ファイル |

これ以外のディレクトについては [Jekyll](https://jekyllrb.com/) のドキュメントを参照。
