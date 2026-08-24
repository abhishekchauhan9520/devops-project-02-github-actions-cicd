# Project 02 — Basic CI/CD Pipeline with GitHub Actions

A small, reproducible CI/CD example that validates a Python application and then builds and smoke-tests its Docker image with GitHub Actions.

## What this demonstrates

- GitHub Actions workflow automation
- Pull-request and `main` branch validation
- Python unit testing with the standard library
- Docker image creation
- Container smoke testing
- Dependency-free application packaging

## Repository structure

```text
.
├── .github/workflows/ci.yml
├── sample_app/
│   ├── __init__.py
│   └── app.py
├── tests/
│   └── test_app.py
├── Dockerfile
├── .gitignore
└── README.md
```

## Run locally

Run the tests:

```bash
python -m unittest discover -s tests -v
```

Run the application:

```bash
python -m sample_app.app
```

Build and run the container:

```bash
docker build -t devops-project-02 .
docker run --rm devops-project-02
```

Expected output:

```text
Hello, DevOps!
```

## CI/CD flow

1. GitHub Actions checks out the repository.
2. Python 3.12 is installed.
3. Unit tests run.
4. The Docker image is built only when tests pass.
5. The resulting container is executed as a smoke test.

This project intentionally keeps the application simple so the focus stays on the CI/CD workflow.
