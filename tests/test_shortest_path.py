import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from projekodlari.shortest_path import calculate_shortest_path_and_map


def test_shortest_path_output():
    origin = (39.86570, 32.73369)       # Geomatik Mühendisliği Binası (Hacette>
    destination = (39.87081, 32.73482)  # Beytepe Kütüphane

    distance = calculate_shortest_path_and_map(origin, destination, filename="test_map.html")

    assert isinstance(distance, float)        # Mesafe float olmalı
    assert distance > 0                       # Pozitif bir değer olmalı
    assert os.path.exists("test_map.html")    # HTML dosyası oluşturulmuş olmalı
