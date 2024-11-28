# Инструкции по запуску микросервиса

Каждая инструкция выполняется из директории репозитория mle-sprint3-completed
Если необходимо перейти в поддиректорию, напишите соотвесвтующую команду

## 1. FastAPI микросервис в виртуальном окружение

Чтобы запустить микросервис необходимо по порядку выполнить следующие команды:

```python
# команды создания виртуального окружения
# и установки необходимых библиотек в него
cd mle-project-sprint-3-v001/services
source .project3-venv/bin/activate
pip install -r requirements.txt


# команда перехода в директорию
cd ml_service

# команда запуска сервиса с помощью uvicorn
uvicorn app:app --reload --port 8081 --host 0.0.0.0 
```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:8081/api/flat/?flat_id=123459' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "building_id": 12327,
  "floor": 7,
  "kitchen_area": 10,
  "living_area": 70,
  "rooms": 3,
  "is_apartment": false,
  "studio": false,
  "total_area": 85,
  "build_year": 2020,
  "building_type_int": 4,
  "latitude": 55.0,
  "longitude": 37.0,
  "ceiling_height": 3.0,
  "flats_count": 120,
  "floors_total": 20,
  "has_elevator": true,
  "new_building": true
}'
```

## 2. FastAPI микросервис в Docker-контейнере

```bash
# команда перехода в нужную директорию
cd mle-project-sprint-3-v001/services
source .project3-venv/bin/activate

# команда для запуска микросервиса в режиме docker compose
docker image build . --file Dockerfile_ml_service --tag fastapi
docker container run --publish 8081:8081 --env-file .env --volume=./models:/models fastapi

```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:8081/api/flat/?flat_id=1239' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "building_id": 2024,
  "floor": 9,
  "kitchen_area": 6,
  "living_area": 40,
  "rooms": 2,
  "is_apartment": false,
  "studio": false,
  "total_area": 60,
  "build_year": 1987,
  "building_type_int": 3,
  "latitude": 55.1,
  "longitude": 37.1,
  "ceiling_height": 2.5,
  "flats_count": 240,
  "floors_total": 9,
  "has_elevator": false,
  "new_building": false
}'
```

## 3. Docker compose для микросервиса и системы моониторинга

```bash
# команда перехода в нужную директорию

# команда для запуска микросервиса в режиме docker compose

```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:
```

## 4. Скрипт симуляции нагрузки
Скрипт генерирует <...> запросов в течение <...> секунд ...

```
# команды необходимые для запуска скрипта
...
```

Адреса сервисов:
- микросервис: http://localhost:<port>
- Prometheus: ...
- Grafana: ...