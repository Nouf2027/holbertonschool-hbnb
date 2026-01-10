#!/usr/bin/env bash
set -euo pipefail

BASE="${BASE:-http://127.0.0.1:5000}"
OUTDIR="reports"
mkdir -p "$OUTDIR"

python3 -c "import urllib.request as u; u.urlopen('$BASE/api/v1/', timeout=3); print('server_ok')" >/dev/null 2>&1 || {
  echo "Server is not reachable at $BASE. Start the API first, then run again."
  exit 1
}

./task6_curl.sh

python3 -m unittest discover -s tests -p "test_*.py" -v | tee "$OUTDIR/unittest.log"

cat <<EOF2 > TESTING_REPORT.md
# Task 6 - Testing & Validation Report

## Environment
- Base URL: $BASE

## Swagger Verification
- Endpoint: $BASE/api/v1/
- Evidence: reports/swagger.txt

## Manual Tests (cURL)
- Script: task6_curl.sh
- Logs: reports/curl.log
- Individual outputs: reports/*.txt

## Automated Tests (unittest)
- Command: python3 -m unittest discover -s tests -p "test_*.py" -v
- Log: reports/unittest.log

## Notes
- The success flow is executed only if a valid user_id can be obtained; otherwise it is skipped.
EOF2
