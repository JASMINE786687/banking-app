# Banking System (Console App)

Simple console-based banking app in Python. Features:
- Deposit, Withdraw, Check Balance
- Balance persisted to `accounts.json`
- Prevents withdrawals that exceed balance

## Run locally
1. python -m venv venv
2. source venv/bin/activate  # or .\venv\Scripts\Activate.ps1 on Windows
3. pip install -r requirements.txt
4. python main.py

## Docker
Build locally:
docker build -t banking-app:local .
Run:
docker run -it -v $(pwd)/accounts.json:/app/accounts.json banking-app:local

## Files
- `main.py` : app
- `accounts.json` : data file
- `.github/workflows/docker-build.yml` : CI build

## Sample output
(attach screenshots in this repo or below)



