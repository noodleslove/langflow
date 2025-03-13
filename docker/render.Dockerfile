FROM --platform=linux/amd64 noodleslove/langflow:latest

ENTRYPOINT ["python", "-m", "langflow", "run"]
