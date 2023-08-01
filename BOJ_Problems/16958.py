from itertools import combinations as C
import sys

input = lambda : sys.stdin.readline().rstrip()

n, tp_time = map(int, input().split())

coordinates_of_cities, special_city_numbers = [None], set()
for node in range(1, n + 1):
    is_special_city, x, y = map(int, input().split())
    coordinates_of_cities.append((x, y))
    if is_special_city:
        special_city_numbers.add(node)

INF = int(1e9)
floyd_table = [[INF] * (n+1) for _ in range(n+1)]
for city_number, other_city_number in C(range(1, n + 1), 2):
    city_x, city_y = coordinates_of_cities[city_number]
    other_city_x, other_city_y = coordinates_of_cities[other_city_number]

    taxi_time = abs(city_x - other_city_x) + abs(city_y - other_city_y)

    if (          city_number in special_city_numbers
        and other_city_number in special_city_numbers
        and taxi_time >= tp_time
        ):
        floyd_table[city_number][other_city_number] = tp_time
        floyd_table[other_city_number][city_number] = tp_time
    else:
        floyd_table[city_number][other_city_number] = taxi_time
        floyd_table[other_city_number][city_number] = taxi_time

for center in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if floyd_table[i][j] > floyd_table[i][center] + floyd_table[center][j]:
                floyd_table[i][j] = floyd_table[i][center] + floyd_table[center][j]

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(floyd_table[a][b])



"""C++ code"""
# #include <iostream>
# #include <vector>
# #include <set>

# using namespace std;

# const int INF = 1e9;

# int main() {
#     int n, tp_time;
#     cin >> n >> tp_time;

#     vector<pair<int, int>> coordinates_of_cities(n+1);
#     set<int> special_city_numbers;

#     for (int node = 1; node <= n; node++) {
#         int is_special_city, x, y;
#         cin >> is_special_city >> x >> y;
#         coordinates_of_cities[node] = make_pair(x, y);
#         if (is_special_city) special_city_numbers.insert(node);
#     }

#     vector<vector<int>> connections(n+1, vector<int>(n+1));
#     for (int city_number = 1; city_number <= n; city_number++) {
#         for (int other_city_number = city_number + 1; other_city_number <= n; other_city_number++) {
#             if (city_number == other_city_number) {
#                 continue;
#             }

#             int city_x = coordinates_of_cities[city_number].first;
#             int city_y = coordinates_of_cities[city_number].second;
#             int other_city_x = coordinates_of_cities[other_city_number].first;
#             int other_city_y = coordinates_of_cities[other_city_number].second;

#             int taxi_time = abs(city_x - other_city_x) + abs(city_y - other_city_y);

#             if (special_city_numbers.count(city_number) && special_city_numbers.count(other_city_number) && taxi_time >= tp_time) {
#                 connections[city_number][other_city_number] = tp_time;
#                 connections[other_city_number][city_number] = tp_time;
#             }
#             else {
#                 connections[city_number][other_city_number] = taxi_time;
#                 connections[other_city_number][city_number] = taxi_time;
#             }
#         }
#     }

#     vector<vector<int>> floyd_table(n+1, vector<int>(n+1));

#     for (int i = 1; i <= n; i++) {
#         for (int j = 1; j <= n; j++) {
#             if (i == j) floyd_table[i][j] = 0;
#             else floyd_table[i][j] = connections[i][j];
#         }
#     }

#     for (int center = 1; center <= n; center++) {
#         for (int i = 1; i <= n; i++) {
#             for (int j = 1; j <= n; j++) {
#                 floyd_table[i][j] = min(floyd_table[i][j], floyd_table[i][center] + floyd_table[center][j]);
#             }
#         }
#     }

#     int num_queries;
#     cin >> num_queries;
#     for (int q = 0; q < num_queries; q++) {
#         int a, b;
#         cin >> a >> b;
#         cout << floyd_table[a][b] << "\n";
#     }

#     return 0;
# }
