FROM python:3.11-alpine

WORKDIR /action_workspace

COPY greet_visitor.py .

ENTRYPOINT ["python", "greet_visitor.py"]
