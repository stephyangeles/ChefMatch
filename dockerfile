# Use the official PostgreSQL image from Docker Hub
FROM postgres:latest

# Install Python and pip
RUN apt-get update && apt-get install -y python3.12 python3-pip python3-psycopg2

# Set environment variables for PostgreSQL
ENV POSTGRES_DB=ChefMatch
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_HOST=localhost
ENV POSTGRES_PORT=5432

# Expose the default PostgreSQL port
EXPOSE 5432

# Copy Python scripts and requirements file
COPY db /db

# Install Python dependencies
RUN chmod +x /db/entry_point.sh

# Start PostgreSQL and run Python scripts
ENTRYPOINT ["/db/entry_point.sh"]