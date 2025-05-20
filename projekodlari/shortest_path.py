import osmnx as ox
import networkx as nx
from geopy.distance import geodesic
import folium

def calculate_shortest_path_and_map(origin, destination, filename="map.html"):
    """
    OpenStreetMap verisiyle A noktasından B noktasına en kısa yolu bulur ve harita olarak kaydeder.

    Parameters:
    origin: tuple -> (lat, lon) formatında başlangıç noktası
    destination: tuple -> (lat, lon) formatında varış noktası
    filename: str -> Oluşturulacak HTML dosyasının adı (varsayılan: map.html)

    Returns:
    distance_km: float -> En kısa yolun kilometre cinsinden uzunluğu
    """
    G = ox.graph_from_place("Hacettepe Üniversitesi Beytepe Kampüsü, Ankara, Türkiye", network_type='walk')


    orig_node = ox.distance.nearest_nodes(G, origin[1], origin[0])
    dest_node = ox.distance.nearest_nodes(G, destination[1], destination[0])

    route = nx.shortest_path(G, orig_node, dest_node, weight='length')

    route_coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in route]

    distance_km = round(sum(geodesic(route_coords[i], route_coords[i+1]).km for i in range(len(route_coords)-1)), 2)

    m = folium.Map(location=origin, zoom_start=14)
    folium.PolyLine(route_coords, color="blue", weight=5, opacity=0.7).add_to(m)
    folium.Marker(location=origin, popup="Başlangıç").add_to(m)
    folium.Marker(location=destination, popup="Varış").add_to(m)

    mid_point = route_coords[len(route_coords)//2]
    folium.Marker(mid_point, popup=f"Mesafe: {distance_km} km", icon=folium.Icon(color="green")).add_to(m)

    m.save(filename)

    return distance_km


if __name__ == "__main__":
    origin = (39.86570, 32.73369)       # Geomatik Mühendisliği Binası (Hacettepe)
    destination = (39.87081, 32.73482)  # Beytepe Kampüs Kütüphane
    distance = calculate_shortest_path_and_map(origin, destination)
    print(f"Geomatik Binası → Kütüphane en kısa mesafe: {distance} km")
