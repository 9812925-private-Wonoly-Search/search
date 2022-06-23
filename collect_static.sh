#!/usr/bin/env sh

# Publish static assets.
cd jstoolchain
npm run-script build
cd ..

python src/manage.py collectstatic --no-input