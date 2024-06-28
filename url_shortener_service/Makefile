build-up:
	docker compose up --force-recreate --remove-orphans --build

build-up-detached:
	docker compose up --force-recreate --remove-orphans --build --detached

build-up-app:
	docker compose up app --force-recreate --remove-orphans --build

build-up-app-detached:
	docker compose up app --force-recreate --remove-orphans --build --detached

build-up-db:
	docker compose up db_app --force-recreate --remove-orphans --build

build-up-db-detached:
	docker compose up db_app --force-recreate --remove-orphans --build --detached

build-up-redis:
	docker compose up redis --force-recreate --remove-orphans --build

build-up-redis-detached:
	docker compose up redis --force-recreate --remove-orphans --build --detached

build-up-adminer:
	docker compose up adminer --force-recreate --remove-orphans --build

build-up-adminer-detached:
	docker compose up adminer --force-recreate --remove-orphans --build --detached

scale-app:
ifeq ($(scale),)
	docker compose up app --force-recreate --remove-orphans --scale app=2
else
	docker compose up app --force-recreate --remove-orphans --scale app=$(scale)
endif

scale-app-detached:
ifeq ($(scale),)
	docker compose up app --force-recreate --remove-orphans --detached --scale app=2
else
	docker compose up app --force-recreate --remove-orphans --detached --scale app=$(scale)
endif

tests-unit:
	@docker compose run --rm app \
		sh -c "python -m unittest \
		discover \
			--top-level-directory "./app" \
			--start-directory ./app/tests/unit_tests \
			--pattern test_*.py \
			--verbose"

tests-integration:
	@docker compose run --rm app \
		sh -c "python -m unittest \
		discover \
			--top-level-directory "./app" \
			--start-directory ./app/tests/integration_tests \
			--pattern test_*.py \
			--verbose"


.PHONY: help build-up build-up-detached build-up-app build-up-app-detached build-up-db build-up-db-detached build-up-redis build-up-redis-detached build-up-adminer build-up-adminer-detached scale-app scale-app-detached tests-unit tests-integration

help:
	@echo "Available commands:"
	@echo "  build-up                     Start the Docker containers, force recreate, remove orphans, and build."
	@echo "                               Example: make build-up"
	@echo ""
	@echo "  build-up-detached            Start the Docker containers in detached mode, force recreate, remove orphans, and build."
	@echo "                               Example: make build-up-detached"
	@echo ""
	@echo "  build-up-app                 Start the app container, force recreate, remove orphans, and build."
	@echo "                               Example: make build-up-app"
	@echo ""
	@echo "  build-up-app-detached        Start the app container in detached mode, force recreate, remove orphans, and build."
	@echo "                               Example: make build-up-app-detached"
	@echo ""
	@echo "  build-up-db                  Start the db_app container, force recreate, remove orphans, and build."
	@echo "                               Example: make build-up-db"
	@echo ""
	@echo "  build-up-db-detached         Start the db_app container in detached mode, force recreate, remove orphans, and build."
	@echo "                               Example: make build-up-db-detached"
	@echo ""
	@echo "  build-up-redis               Start the redis container, force recreate, remove orphans, and build."
	@echo "                               Example: make build-up-redis"
	@echo ""
	@echo "  build-up-redis-detached      Start the redis container in detached mode, force recreate, remove orphans, and build."
	@echo "                               Example: make build-up-redis-detached"
	@echo ""
	@echo "  build-up-adminer             Start the adminer container, force recreate, remove orphans, and build."
	@echo "                               Example: make build-up-adminer"
	@echo ""
	@echo "  build-up-adminer-detached    Start the adminer container in detached mode, force recreate, remove orphans, and build."
	@echo "                               Example: make build-up-adminer-detached"
	@echo ""
	@echo "  scale-app                    Scale the app service to the specified number of instances (default: 2)."
	@echo "                               Example: make scale-app"
	@echo "                               Example: make scale-app scale=3"
	@echo ""
	@echo "  scale-app-detached           Scale the app service to the specified number of instances in detached mode (default: 2)."
	@echo "                               Example: make scale-app-detached"
	@echo "                               Example: make scale-app-detached scale=3"
	@echo ""
	@echo "  tests-unit                   Run unit tests inside the app container."
	@echo "                               Example: make tests-unit"
	@echo ""
	@echo "  tests-integration            Run integration tests inside the app container."
	@echo "                               Example: make tests-integration"
