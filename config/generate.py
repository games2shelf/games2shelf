from pathlib import Path

template = Path("config/zensical.toml").read_text()

langs = [
    ("es", "docs/es", "site/es"),
    # ("en", "docs/en", "site/en"),
]

for lang, docs, site in langs:
    text = (
        template
        .replace("{{LANGUAGE}}", lang)
        .replace("{{DOCS_DIR}}", docs)
        .replace("{{SITE_DIR}}", site)
    )

    Path(f"zensical.{lang}.toml").write_text(text)