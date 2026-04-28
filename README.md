# Cursor SQL Agent

## Development setup

Install the native ODBC runtime and SQL Server driver:

```sh
sudo apt-get update
sudo apt-get install -y python3.12-venv unixodbc odbcinst
curl -fsSL -o /tmp/packages-microsoft-prod.deb https://packages.microsoft.com/config/ubuntu/24.04/packages-microsoft-prod.deb
sudo dpkg -i /tmp/packages-microsoft-prod.deb
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18
```

Create a virtual environment and install Python dependencies:

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

Load database settings before running queries:

```sh
set -a
. ./.env.example
set +a
```

## How to run queries

Use:

```sh
python sql_runner/run_query.py "SELECT TOP 10 * FROM viewCabBooking"
```

## Rules

- ONLY SELECT queries allowed
- No INSERT / UPDATE / DELETE
- Limit results to small sets
