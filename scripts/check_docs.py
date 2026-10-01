"""Check this repository's simple inline Markdown links and requirement coverage.

Uses only the Python standard library. Does not fetch external URLs, validate
fragments, evaluate examples, or establish management conformance.
"""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
INLINE_LINK = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")
REQUIREMENT = re.compile(r"\bTSM-\d{3}\b")
DEFINITION = re.compile(r"^## (TSM-\d{3})\b", re.MULTILINE)
MATRIX_ROW = re.compile(r"^\| (TSM-\d{3}) \|", re.MULTILINE)


def prose(markdown: str) -> str:
    """Exclude fenced examples, which can contain illustrative paths or text."""
    result = []
    fence = None
    for line in markdown.splitlines():
        stripped = line.lstrip()
        marker = re.match(r"(`{3,}|~{3,})", stripped)
        if fence is None and marker:
            fence = marker.group(1)
            continue
        if fence is not None:
            if re.fullmatch(re.escape(fence[0]) + "{" + str(len(fence)) + r",}\s*", stripped):
                fence = None
            continue
        result.append(line)
    return "\n".join(result)


def check(root: Path) -> list[str]:
    errors = []
    documents = {}
    for path in sorted(root.rglob("*.md")):
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        try:
            documents[path] = prose(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError) as error:
            errors.append(f"{path.relative_to(root)}: cannot read UTF-8: {error}")

    spec = root / "docs/SPECIFICATION-v0.1.md"
    matrix = root / "docs/CONFORMANCE-MATRIX.md"
    for required in (root / "README.md", root / "docs/README.md", spec, matrix):
        if required not in documents:
            errors.append(f"Missing document: {required.relative_to(root)}")

    definitions = DEFINITION.findall(documents.get(spec, ""))
    known = set(definitions)
    if not definitions:
        errors.append("Specification defines no requirements")
    if len(known) != len(definitions):
        errors.append("Specification contains duplicate requirement definitions")
    rows = MATRIX_ROW.findall(documents.get(matrix, ""))
    if len(rows) != len(set(rows)):
        errors.append("Conformance matrix contains duplicate requirement rows")
    if set(rows) != known:
        errors.append(f"Conformance coverage differs: {sorted(set(rows) ^ known)}")

    for path, content in documents.items():
        label = path.relative_to(root)
        for requirement in sorted(set(REQUIREMENT.findall(content)) - known):
            errors.append(f"{label}: undefined requirement {requirement}")
        if path != spec and DEFINITION.search(content):
            errors.append(f"{label}: requirement definitions belong in the specification")
        for match in INLINE_LINK.finditer(content):
            target = match.group(1).strip()
            if not target:
                errors.append(f"{label}: empty link target")
                continue
            if target.startswith("<"):
                if ">" not in target:
                    errors.append(f"{label}: malformed link target: {target}")
                    continue
                target = target[1:target.index(">")]
            else:
                target = target.split()[0]
            try:
                url = urlsplit(target)
            except ValueError:
                errors.append(f"{label}: malformed URL: {target}")
                continue
            if url.scheme or url.netloc or not url.path:
                continue
            resolved = (path.parent / unquote(url.path)).resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                errors.append(f"{label}: link leaves the repository: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{label}: missing local target: {target}")
    return errors


if __name__ == "__main__":
    failures = check(ROOT)
    if failures:
        print("Documentation checks failed:")
        for failure in failures:
            print(f"- {failure}")
        sys.exit(1)
    print("Documentation checks passed: local file links and requirement references/coverage.")
    print("External URLs, fragments, runtime behavior, and conformance were not assessed.")
