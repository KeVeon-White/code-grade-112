VERSION = $(shell grep -m 1 version pyproject.toml | tr -s ' ' | tr -d '"' | tr -d "'" | cut -d' ' -f3)

cg112:
	pyinstaller -y -p src/cg112/ --copy-metadata cg112 --name "cg112_v$(VERSION)" --specpath dist/ src/cg112/__main__.py

clean:
	rm -rf build
