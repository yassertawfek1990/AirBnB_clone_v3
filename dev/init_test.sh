#!/usr/bin/env bash
# sd
pep8 . && python3 -m unittest discover -v ./tests/ \
    && ./dev/w3c_validator.py \
        $(find ./web_static -maxdepth 1 -name "*.html" -type f ! -name "4*") \
    && ./dev/w3c_validator.py \
	$(find ./web_static/styles -maxdepth 1 -name "*.css" -type f)

ret_val=$?

> ./dev/file.json

py3clean .

exit "$ret_val"
