# umm: yoUr Mirror Manager

A toolkit to manager the fastest mirror of various tools, such as pip, npm, composer and etc.

## Table of Contents

   * [umm: yoUr Mirror Manager](#umm-your-mirror-manager)
      * [Features](#features)
      * [Installation](#installation)
      * [Usage](#usage)
         * [Show umm help](#show-umm-help)
         * [Manage pip](#manage-pip)
            * [Show umm pip help](#show-umm-pip-help)
            * [List all available mirrors of pip](#list-all-available-mirrors-of-pip)
            * [Use the given mirror for pip](#use-the-given-mirror-for-pip)
            * [Show current mirror of pip](#show-current-mirror-of-pip)
         * [Manage npm](#manage-npm)
            * [Show umm npm help](#show-umm-npm-help)
            * [List all available mirrors of npm](#list-all-available-mirrors-of-npm)
            * [Use the given mirror for npm](#use-the-given-mirror-for-npm)
            * [Show current mirror of npm](#show-current-mirror-of-npm)
      * [How to test in local](#how-to-test-in-local)

## Features

We are going to support to manage the mirror of following tools:
- [x] pip
- [x] npm
- [x] composer
- [x] homebrew
- [x] linuxbrew
- [x] golang
- [ ] docker
- [ ] ubuntu
- [ ] centos
- [ ] julia
- [ ] etc.

## Installation

```bash
pip install umm
```
## Upgrade

```bash
pip install -U umm
```

## Usage

### Show `umm` help

```bash
umm
```
or
```bash
umm --ehlp
```

Output
```
Usage: umm [OPTIONS] COMMAND [ARGS]...

  A toolkit to manager the fastest mirror of various tools, such as pip,
  npm, composer and etc.

Options:
  --help  Show this message and exit.

Commands:
  npm  Manage npm mirrors.
  pip  Manage pip mirrors.
  v    Show umm version.
```

### Manage `pip`

#### Show `umm pip` help

```bash
umm pip
```
or
```bash
umm pip --ehlp
```

Output
```
Usage: umm pip [OPTIONS] COMMAND [ARGS]...

  Manage pip mirrors.

Options:
  --help  Show this message and exit.

Commands:
  ls   List all available mirrors
  now  Show current mirror.
  use  Use the given mirror.
```

#### List all available mirrors of `pip`

```bash
umm pip ls
```

Output
```
o               https://pypi.python.org/simple/
tuna            https://pypi.tuna.tsinghua.edu.cn/simple
douban          http://pypi.douban.com/simple/
aliyun          https://mirrors.aliyun.com/pypi/simple/
ustc            https://mirrors.ustc.edu.cn/pypi/web/simple
```
#### Use the given mirror for `pip`

For example, use the **tuna** mirror.

```bash
umm pip use tuna
```

#### Show current mirror of `pip`

```bash
umm pip now
```

Output
```
tuna            https://pypi.tuna.tsinghua.edu.cn/simple
```



### Manage `npm`

#### Show `umm npm` help

```bash
umm npm
```
or
```bash
umm npm --ehlp
```

Output
```
Usage: umm npm [OPTIONS] COMMAND [ARGS]...

  Manage npm mirrors.

Options:
  --help  Show this message and exit.

Commands:
  ls   List all available mirrors.
  now  Show current using mirror.
  use  Use the given mirror.
```

#### List all available mirrors of `npm`

```bash
umm npm ls
```

Output
```
  [npm] name      url
------------------------------------------------------------
* o               https://registry.npmjs.org/
  cnpm            http://r.cnpmjs.org/
  taobao          https://registry.npm.taobao.org/
  nj              https://registry.nodejitsu.com/
  npmMirror       https://skimdb.npmjs.com/registry/
  edunpm          http://registry.enpmjs.org/
```
#### Use the given mirror for `npm`

For example, use the **tabao** mirror.

```bash
umm npm use taobao
```

#### Show current mirror of `npm`

```bash
umm npm now
```

Output
```
taobao          https://registry.npm.taobao.org/
```

## How to test

### install locally

Once your developed a while and want to test the umm, your have two ways to test:

1. install this package in your local via:

```bash
pip install --editable .
```
2. or, directly run the python file via:

```bash
python -m umm
```

### run the test

Make sure you have installed `pytest`

```bash
cd umm/
export PYTHONPATH=src
pytest
```