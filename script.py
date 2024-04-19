#!/usr/bin/python -u

import os
import sys
from subprocess import Popen, PIPE
from time import sleep

def git_checkout(branch_name):
    os.system('git checkout "%s"' % branch_name)

def git_pull(branch_name):
    os.system('git pull origin "%s"' % branch_name)

def git_merge(branch_name):
    os.system('git merge "%s"' % branch_name)

def check_changes_exist(branch_name):
    p = Popen('git diff master..%s --name-only' % branch_name, shell=True, stdout=PIPE)
    (output, _) = p.communicate()
    return bool(output)

def merge_branch_with_stag():
    print('Checking if feature branch has changes...')
    if not check_changes_exist('dev'):
        print('Error: There are no changes in the feature branch.')
        sys.exit(-1)

    print('Switching to dev branch...')
    git_checkout('dev')

    print('Merging feature branch with dev...')
    git_merge('feature')

    print('Changes merged successfully into dev.')

def merge_branch_with_master():
    print('Checking if feature branch has changes...')
    if not check_changes_exist('dev'):
        print('Error: There are no changes in the feature branch.')
        sys.exit(-1)

    print('Switching to dev branch...')
    git_checkout('dev')

    print('Merging feature branch with dev...')
    git_merge('feature')

    print('Switching to master branch...')
    git_checkout('master')

    print('Merging feature branch with master...')
    git_merge('feature')

    print('Changes merged successfully into master.')

def main():
    if len(sys.argv) != 2:
        print('Usage: script.py <action>')
        sys.exit(1)

    action = sys.argv[1]

    if action == 'stag':
        merge_branch_with_stag()
    elif action == 'master':
        merge_branch_with_master()
    else:
        print('Invalid action. Please specify "stag" or "master".')
        sys.exit(1)

if __name__ == "__main__":
    main()
