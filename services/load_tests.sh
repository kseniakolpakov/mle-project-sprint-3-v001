##!/bin/bash

# URL вашего сервиса
URL="http://localhost:8081/api/flat/"

# Количество запросов
REQUESTS=100

# Функция для генерации случайных чисел в диапазоне
random_number() {
    shuf -i $1-$2 -n 1
}

# Цикл для отправки запросов
for ((i=1; i<=$REQUESTS; i++))
do
    # Генерация случайных параметров
    building_id=$(random_number 1 1000)
    floor=$(random_number 1 50)
    kitchen_area=$(random_number 5 30)
    living_area=$(random_number 20 100)
    rooms=$(random_number 1 5)
    total_area=$(random_number 30 150)
    build_year=$(random_number 1950 2023)
    ceiling_height=$(random_number 2 4)
    flats_count=$(random_number 10 500)
    floors_total=$(random_number 5 50)
    latitude=$(awk -v min=54.0 -v max=56.0 'BEGIN{srand(); print min+rand()*(max-min)}')
    longitude=$(awk -v min=36.0 -v max=38.0 'BEGIN{srand(); print min+rand()*(max-min)}')

    # Формирование JSON с рандомными значениями
    DATA=$(cat <<EOF
{
    "flat_id": "$RANDOM",
    "model_params": {
        "building_id": $building_id,
        "floor": $floor,
        "kitchen_area": $kitchen_area,
        "living_area": $living_area,
        "rooms": $rooms,
        "is_apartment": true,
        "studio": false,
        "total_area": $total_area,
        "build_year": $build_year,
        "building_type_int": 1,
        "latitude": $latitude,
        "longitude": $longitude,
        "ceiling_height": $ceiling_height,
        "flats_count": $flats_count,
        "floors_total": $floors_total,
        "has_elevator": true,
        "new_building": false
    }
}
EOF
)

    echo "Sending request $i"
    curl -X POST -H "Content-Type: application/json" -d "$DATA" $URL &
done

wait
echo "Load test completed."