install:
		poetry install

#brain-games:
#		poetry run brain-games

# TODO find out the way to run game with option to choose game type

brain-even:
		poetry run brain-games brain-even

brain-calc:
		poetry run brain-games brain-calc

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl

lint:
		poetry run flake8 brain_games