# poc-uwas

## How to install

1. Clone this repository

```
git clone git@github.com:thomasperrein/poc-uwas.git
```

2. Install python on your device

```
brew install python
```

3. Install globally poetry on your device (pipx required)

```
pipx install poetry
```

4. Then run the following

```
cd poc-uwas
python3 -m venv .venv # create a virtual env
source .venv/bin/activate
poetry install
```

5. Add secrets in a .env file, ask me for the secrets

```
cp .env.example .env
```

6. To launch

```
python <name_of_pipeline.py>
dlt pipeline <name_of_pipeline> show
```

7. To launch dbt

```
cd dbt
dbt run
```
