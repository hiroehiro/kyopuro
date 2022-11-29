class Unionfind:
    """ Unionfind

    ノードのグループ化, 同一グループに属しているかの判定
    計算量: O(α(n)) log n より早い

    """
    def __init__(self, n):
        """

        Args:
            n (int): ノードの総数
        """
        self.par = [i for i in range(n)]
        self.rank = [0]*n

    def find(self, x):
        """親が何か探す

        Args:
            x (int): 親を探したいノード番号

        Returns:
            int: 親のノード番号
        """
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        """グループの併合

        Args:
            x, y (int): 併合したいノードの番号
        """
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    def same(self, x, y):
        """同じグループに属しているか判定

        Args:
            x, y (int): 同じグループに属しているか判定したいノードの番号

        Returns:
            bool: 同じグループならTrue, そうでないならFalse 
        """
        return self.find(x) == self.find(y)