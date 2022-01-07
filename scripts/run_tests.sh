export PYTHONPATH=.
export environment=development

pytest --disable-pytest-warnings
coverage report -m
coverage run --source app -m pytest
coverage html
coverage xml -o htmlcov/coverage.xml

rm .github/images/coverage.svg
coverage-badge -o .github/images/coverage.svg

unset PYTHONPATH
unset environment
