"""Two Lines to Your Past Self — entry generator (stdlib only)."""
from pathlib import Path

ENTRY = (
    "Don't cancel the interview on that rainy Tuesday morning just because you felt unready.\n"
    "You got the job anyway \u2014 and it decided where you would live for the next three years."
)

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
