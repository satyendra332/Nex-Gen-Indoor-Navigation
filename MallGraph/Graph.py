import string
import random

import networkx as nx

from DBMS import datahandler

class MallGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_location(self, name, x, y, z):
        self.graph.add_node(name, pos=(int(x), int(y), int(z)))

    def add_connection(self, node1, node2):
        self.graph.add_edge(node1, node2)

    def find_shortest_path(self, start, destination):
        shortest_path_nodes = nx.dijkstra_path(self.graph, start, destination)
        shortest_path_coordinates = [tuple(self.graph.nodes[node]['pos']) for node in shortest_path_nodes]
        return shortest_path_coordinates

class MakeGraph:
    def __init__(self):
        self.data = datahandler.read_user()
        self.mall = MallGraph()

class MakeGraph:
    def __init__(self):
        self.data = datahandler.read_user()
        self.mall = MallGraph()

    def create_connections(self):
        for i in self.data:
            print(i)
            coordinates = eval(i[3])
            self.mall.add_location(str(i[1]), coordinates[0], coordinates[1], coordinates[2])
        self.mall.add_connection("RU Events 1", "RU Office Room")

        self.mall.add_connection("Shakesmart", "RU Office Room")

        self.mall.add_connection("Subway", "Shakesmart")
        self.mall.add_connection("Subway", "Carrer Connection Center")
        self.mall.add_connection("Carrer Connection Center", "Reitz Union Hotel Desk")
        self.mall.add_connection("Reitz Union Hotel Desk", "RU Office 2")

        self.mall.add_connection("Reitz Union Hotel Desk", "Restroom")
        self.mall.add_connection("Restroom", "Game Room")
        self.mall.add_connection("Restroom", "Sitting Area")
        self.mall.add_connection("Help Desk", "Sitting Area")
        self.mall.add_connection("Help Desk", "Subway")
        
        self.mall.add_connection("Sitting Area", "Entrance")

        self.mall.add_connection("Movie Theather", "RU Events 1")
        
        self.mall.add_connection("Movie Theather", "RU Events 2")
        self.mall.add_connection("Entrance", "RU Events 3")
        self.mall.add_connection("RU Events 2", "RU Events 3")

    def find_path(self, start, destination):
        shortest_path = self.mall.find_shortest_path(start, destination)
        return shortest_path
    
    def calculate_average_time(self, start, destination, average_speed):
        shortest_path = self.find_path(start, destination)
        total_distance = 0
        for i in range(len(shortest_path) - 1):
            current_pos = shortest_path[i]
            next_pos = shortest_path[i + 1]
            distance = ((next_pos[0] - current_pos[0]) ** 2 +
                        (next_pos[1] - current_pos[1]) ** 2 +
                        (next_pos[2] - current_pos[2]) ** 2) ** 0.5
            total_distance += distance

        average_time = total_distance / average_speed
        return average_time

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    generated_strings = set()

    while True:
        random_string = ''.join(random.choice(characters) for _ in range(length))
        if random_string not in generated_strings:
            generated_strings.add(random_string)
            return random_string