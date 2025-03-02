#!/bin/bash

# Start PostgreSQL in the background
docker-entrypoint.sh postgres &

# Wait for PostgreSQL to start
until pg_isready -h localhost -U $POSTGRES_USER -d $POSTGRES_DB; do
  echo "Waiting for PostgreSQL to start..."
  sleep 1
done

# Run Python scripts
echo "Running Python scripts..."
cd /
python3 /db/database/creation.py
python3 /db/database/tables_creation.py

# Keep the container running
tail -f /dev/null