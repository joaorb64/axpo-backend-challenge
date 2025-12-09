# Productionalised challenge repository

## Strategy

### Initial steps (2h)

- Forked, removed other challenge types from the repository
- Started by taking an overall look and removing all unused functions
- Joined different files that were doing the same things (example: there were places with more than one "utils" files)
- Removed duplicated routes and organized tags
- Added a proper health check, removed pong and the web server dependencies
- Started separating files into directories based on domain (assets, measurements, signals)
- Organized directories based on the `Netflix/dispatch` format
- Made everything work and run with Docker

### Refactoring (4h)

- Made the concept of schemas and models clearly separated
  - Made all using pydantic models and classes based on SQLAlchemy
  - Most files became really small or were completely removed
  - Queries became simpler since most of the logic is handled by the DB
  - Generated docs also get the benefit of having well defined schemas instead of plain json responses
- Added a database (PostreSQL)
  - Created a script to populate the databases with all data from the json/csv files
- Reworked settings to be more straightforward

### Final touches (30min)

- Wrote documentation

### Beyond what was done

My feeling is that I only touched the surface if we're thinking of a big project. But of course, would take more time.

These are things I'd do next to make this project more productionalized:

- Better organize dev/prod environments with their own separated DBs
- Better organize logging: add files to initialize and handle logging in a unified way (using default python logging)
- Add database migration handling (Alembic)
- Add observability:
  - Services to track stats and post them to the DB
  - Grafana for data visualization
- Add tests
- Add CI/CD using Github Actions
  - Would make more sense after having deployment and test flows

## Running

### Start the application

`docker compose up`

### Seed database

This script inserts data from the json/csv files into the database

`docker compose run --rm api python app/seed.py`
