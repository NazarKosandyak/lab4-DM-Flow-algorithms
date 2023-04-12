import queue

def read_input_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        n = int(lines[0])
        graph = []
        for i in range(1, n+1):
            row = list(map(int, lines[i].split()))
            graph.append(row)
        return n, graph

def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    q = queue.Queue()
    q.put(s)
    visited[s] = True
    while not q.empty():
        u = q.get()
        for v in range(len(graph)):
            if visited[v] == False and graph[u][v] > 0:
                q.put(v)
                visited[v] = True
                parent[v] = u
                if v == t:
                    return True
    return False

def ford_fulkerson(file_path, s, t):
    n, graph = read_input_file(file_path)
    parent = [-1] * n
    max_flow = 0
    while bfs(graph, s, t, parent):
        path_flow = float("Inf")
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = u
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u
        max_flow += path_flow
    return max_flow

max_flow = ford_fulkerson("input.txt", 0, 7)
print("Максимальний потік:", max_flow)
