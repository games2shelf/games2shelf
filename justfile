set shell := ["bash", "-cu"]

# Generate configuration files
generate:
    python config/generate.py

# Serve Spanish documentation
serve: generate
    zensical serve --config-file zensical.es.toml

# Build Spanish documentation
build: generate
    zensical build --config-file zensical.es.toml
