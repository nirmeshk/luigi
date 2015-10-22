#!/bin/sh
# To enable this hook, copy it into .git/hooks/pre-commit in your project's workspace
# or use the reinstall-git-hook-everywhere.sh script
# found at https://gist.github.com/jfuerth/43570af79947eec68581 and extended for DigitalOcean credentials

if git rev-parse --verify HEAD >/dev/null 2>&1
then
    against=HEAD
else
    # Initial commit: diff against an empty tree object
    against=4b825dc642cb6eb9a060e54bf8d69288fbee4904
fi

if git diff --cached $against | grep '^+.*AKIA'
then
    cat <<\EOF
Error: Detected AWS secret key in this commit.

If you are absolutely sure you haven't just committed an AWS secret
key, commit again with the --no-verify option.
EOF
    exit 1
fi

if git diff --cached $against | grep -E -2 '^\+MII[0-9A-Za-z+/]{20}'
then
    cat <<\EOF
Error: Detected PEM formatted key material in this commit.

If you are absolutely sure you haven't just committed a secret
key, commit again with the --no-verify option.
EOF
    exit 1
fi

if git diff --cached $against | grep -E -2 '^\+[ \t]*puts[( ]'
then
  cat <<\EOF
Error: Found a new puts in this changeset!

If you actually mean to commit a raw puts (rather than a logger statement)
then commit again with the --no-verify option.
EOF
  exit 1
fi


if git diff --cached $against | grep -E -2 '\+.*Bearer [0-9A-Za-z]{64}'
then
  cat <<\EOF
  Error: Detected potential Digital ocean key commit

  If you are absolutely sure you haven't just committed a digital ocean secret
  key, commit again with the --no-verify option.
EOF
  exit 1
fi
