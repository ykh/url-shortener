build-up-master:
	docker compose up locust-master --force-recreate --remove-orphans --build

build-up-scale-workers:
ifeq ($(scale),)
	docker compose up --force-recreate --build --remove-orphans --scale locust-worker=5
else
	docker compose up --force-recreate --build --remove-orphans --scale locust-worker=$(scale)
endif

.PHONY: help build-up-master build-up-scale-workers

help:
	@echo "Available commands:"
	@echo "  build-up-master               Start the Locust master container, force recreate, remove orphans, and build."
	@echo "                                Example: make build-up-master"
	@echo ""
	@echo "  build-up-scale-workers        Start and scale the Locust worker containers, force recreate, remove orphans, and build."
	@echo "                                Default scale: 5 workers."
	@echo "                                Example: make build-up-scale-workers"
	@echo "                                Example: make build-up-scale-workers scale=3"
