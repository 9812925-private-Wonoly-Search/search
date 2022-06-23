# Django Starter

## Setup

-   Clone the repository.

-   Change in to the directory.

```sh
cd search
```

-   Copy the `.env` file.

```sh
cp .env.example .env
```

-   Create secret key for Django. And copy the generated string to `APP_SECRET_KEY` in `.env` file.

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

## Usage

-   Install Python packages with `pipenv install <package>` command and remove with `pipenv uninstall <package>`.

-   Install `dev` only packages with `pipenv install <package> --dev`.

-   Run `pipenv lock -r > requirements.txt` every time there is a change in `Pipfile`

-   You need to rebuild the Docker with `docker build .` when a new package is added in `Pipfile`

## Development

-   Start the Docker.

```bash
docker-compose up -d
```

-   Stop the Docker.

```bash
docker-compose stop
```
