# Pokemon API

## Prerequirements

- MongoDB with "pokemon" database and "pokemons" collection
- create .env file

## Get started

1. Clone repo and enter it

`git clone https://github.com/Tvister7/pokemon-api && cd 'pokemon-api'`

2. Start :)

### Via docker

- `make run`

### Via poetry

- `poetry install`

- `make launch`

## Usage

### Swagger

1. Go to app swagger at [localhost:9000](http://localhost:9000/docs)
2. Run queries

### Curl

1. Info endpoint

curl -X 'GET' \
  '<http://localhost:9000/v1/pokemon/chansey>' \
  -H 'accept: application/json'

2. HP endpoint

curl -X 'GET' \
  '<http://localhost:9000/v1/pokemon/hp-filter/250>' \
  -H 'accept: application/json'
