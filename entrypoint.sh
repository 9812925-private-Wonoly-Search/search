#!/usr/bin/env sh

# Publish static assets.
python src/manage.py collectstatic --no-input


# Auto migrate database.
if [ "$APP_AUTO_MIGRATE" = "true" ]; then
    python src/manage.py migrate;
else
    echo "Auto migration is disabled.";
fi


# Run Gunicorn web server.
if [ "$GUNICORN_AUTO_RELOAD" = "true" ]; then
    echo "Gunicorn reload is enabled."
    gunicorn $GUNICORN_APP --chdir ./src --bind "$GUNICORN_HOST:$GUNICORN_PORT" --workers "$GUNICORN_WORKER" --reload;
else
    echo "Gunicorn reload is disabled."
    gunicorn $GUNICORN_APP --chdir ./src --bind "$GUNICORN_HOST:$GUNICORN_PORT" --workers "$GUNICORN_WORKER";
fi
