FROM noodleslove/langflow:latest

# Install PostgreSQL dependencies
USER root
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    libpq5 \
    libpq-dev \
    postgresql-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER user
ENV LANGFLOW_HOST=0.0.0.0
ENV LANGFLOW_PORT=7860
ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT ["python", "-m", "langflow", "run"]
