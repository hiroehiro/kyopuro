def bellmanford(edge, V, start=0):
    """ベルマンフォード法

    startノードを始点とし, 他のノードを終点として移動したとき, 通る辺のコストの和の最小値
    負辺が存在しても使える
    計算量: O(EV)

    Args:
        edge (list): ノードAからノードBに行くコストがXの時[A, B, X]. これを全ての辺についてまとめたリスト
        V (int): ノード総数
        start (int, optional): 始点のノード. Defaults to 0.

    Returns:
        list or -1: 負の閉路が存在しないとき
                        startノードから[0番目のノードに移動するコストの最小値, 1番目のノードに移動するコストの最小値, ...]
                        dist[start] = 0
                    負の閉路が存在するとき
                        -1
    """
    INF = 1<<60
    dist = [INF] * V
    dist[start] = 0

    for i in range(V):
        for from_node, to_node, cost  in edge:

            if dist[from_node] + cost < dist[to_node]:
                dist[to_node] = dist[from_node] + cost

                # V回目にも更新があったら負の閉路が存在する
                if i == V-1:
                    return -1

    return dist