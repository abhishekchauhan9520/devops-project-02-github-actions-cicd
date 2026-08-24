"""Minimal application used to demonstrate GitHub Actions CI/CD."""


def build_message(name: str = "DevOps") -> str:
    """Return a deterministic greeting for testing and CI demos."""
    name = name.strip() or "DevOps"
    return f"Hello, {name}!"


def main() -> None:
    print(build_message())


if __name__ == "__main__":
    main()
