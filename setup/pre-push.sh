set -e
set -o pipefail
tox -e flake8
tox -e py27-nonhdfs | grep "^TOTAL \s*[0-9]*\s*[0-9]*\s*[0-9]*%.*$" | awk '$4 < 68 {print "Code Coverage less than 68, rejecting push"; exit 1}'
