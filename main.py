from pathlib import Path

ENTRY = "You will ship the bug you laughed at in review."

def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY, encoding="utf-8")
    assert len(ENTRY) <= 120
    print(ENTRY)

if __name__ == "__main__":
    main()
