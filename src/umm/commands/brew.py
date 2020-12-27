from click import echo

from .base import MirrorCommand
from .. import C
from ..utils import run_cmd, set_locale, make_export_env, store_env_variable, is_mac

# https://mirrors.tuna.tsinghua.edu.cn/help/homebrew/
# https://frankindev.com/2020/05/15/replace-homebrew-source/

# git -C "$(brew --repo)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git

# git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git
# git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask.git
# git -C "$(brew --repo homebrew/cask-fonts)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask-fonts.git
# git -C "$(brew --repo homebrew/cask-drivers)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask-drivers.git
# git -C "$(brew --repo homebrew/cask-versions)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask-versions.git

REPOS_MAC = [
    ('', 'brew'),
    ('homebrew/core', 'homebrew-core'),
    ('homebrew/cask', 'homebrew-cask'),
    ('homebrew/bottles', 'homebrew-bottles'),
    ('homebrew/cask-fonts', 'homebrew-cask-fonts'),
    ('homebrew/cask-drivers', 'homebrew-cask-drivers'),
    ('homebrew/cask-versions', 'homebrew-cask-versions'),
]

REPOS_LINUX = [
    ('', 'brew'),
    ('homebrew/core', 'linuxbrew-core'),  # not same
    ('homebrew/bottles', 'linuxbrew-bottles'),  # not same
]


def _make_cmd(repo, url=None):
    cmd = 'git -C $(brew --repo %s) remote get-url origin ' % repo
    if url is not None:
        cmd = 'git -C $(brew --repo %s) remote set-url origin "%s"' % (repo, url)
    return cmd


class Brew(MirrorCommand):
    NAME = 'brew'

    def current_mirror_name(self):
        # get $(brew --repo) remote url
        cmd = _make_cmd(REPOS_MAC[0][0])
        is_ok, url = run_cmd(cmd)
        default = 'o'
        for k in self.mirror:
            if self.mirror[k] in url:
                default = k
                break
        return default

    def cmd_use(self, mirror_name, is_local=False):
        if mirror_name not in self.mirror:
            return echo(C.INVALID_MIRROR_NAME)

        # update remote url
        base_url = self.mirror[mirror_name]
        git_urls = {}

        repos = REPOS_MAC if is_mac() else REPOS_LINUX

        for repo, project_name in repos:
            git_url = '%s%s.git' % (base_url, project_name)
            git_urls[repo] = git_url
            cmd = _make_cmd(repo, git_url)
            is_ok, out = run_cmd(cmd)


        # update envs
        store_env_variable('HOMEBREW_BREW_GIT_REMOTE', git_urls[''])
        if mirror_name == 'o':
            if is_mac():
                bottle_url = 'https://homebrew.bintray.com/'
            else:  # for linux
                bottle_url = 'https://linuxbrew.bintray.com/'
        else:
            bottle_url = git_urls['homebrew/bottles']
        store_env_variable('HOMEBREW_BOTTLE_DOMAIN', bottle_url)


cli = Brew()

if __name__ == '__main__':
    set_locale()
    # cli()

    print(cli.current_mirror_name())
    cmd = make_export_env('ABC', 123)
    print(cmd, run_cmd(cmd))

    cli.cmd_use('tuna')
