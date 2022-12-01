import heapq

def dijkstra(costs, start=0):
    """ダイクストラ法

    startノードを始点とし, 他のノードを終点として移動したとき, 通る辺のコストの和の最小値
    負の辺が存在する時使えない
    計算量O(E log V)

    Args:
        costs (list): グラフの隣接リスト. 2次元リスト. len(costs)=グラフのノードの総数.
                      costs[n] = n番目のノードから隣接する[(x, x番目のノードに移動するコスト), (y, y番目のノードに移動するコスト),...]

        start (int): 始点のノード. デフォルトでは0

    Returns:
        dist (list): startノードから[0番目のノードに移動するコストの最小値, 1番目のノードに移動するコストの最小値, ...]
                     dist[start] = 0
    """
    INF = 10**18
    dist = [INF] * len(costs)
    dist[start] = 0
    que = [(0, start)] #(コスト, ノード)
    visited = [False] * len(costs)

    while que:
        _, q = heapq.heappop(que) #ノードの取り出し
        visited[q] = True

        #ノードqに隣接するノードに対して最短距離を確定する
        for node, cost in costs[q]: 
            if not visited[node] and dist[q] + cost < dist[node]:
                dist[node] = dist[q] + cost
                heapq.heappush(que, (dist[node], node))

    return dist