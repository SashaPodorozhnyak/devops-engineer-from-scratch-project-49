install:
	uv sync
	
brain-games:
	uv run brain-games
	
build:
	uv build
	
package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games

brain-even:
	uv run game-even

brain-calc:
	uv run game-calc

brain-gcd:
	uv run game-gcd

brain-progression:
	uv run game-progression

brain-prime:
	uv run game-prime

play-brain-calc:
	asciinema play demo/demo_calc.cast

play-brain-even:
	asciinema play demo/demo.cast

play-brain-gcd:
	asciinema play demo/demo_gcd.cast

play-brain-progression:
	asciinema play demo/demo_progression.cast

play-brain-prime:
	asciinema play demo/demo_prime.cast
