class Solution(object):
    def find(self, x, id):
        root = x
        while root != id[root]:
            root = id[root]
        while x != root:
            next = id[x]
            id[x] = root
            x = next
        return root
    def isConnected(self, x, y, parent):
        return find(x, parent) == find(y, parent)
            
    def union(self, x, y, num_friends, parent, sz):
        print("here")
        root1 = find(x, parent)
        root2 = find(y, parent)
        if root1 == root2: return num_friends
        if sz[root1] < sz[root2]:
            sz[root2] += sz[root1]
            parent[root1] = root2
            
        else:
            sz[root1] += sz[root2]
            parent[root2] = root1
        num_friends-=1
        return num_friends

    def findCircleNum(self, M):
            """
            :type M: List[List[int]]
            :rtype: int
            """
            num_friends = len(M[0])
            parent = {i: i for i in range(num_friends)}
            counter = 0
            size = {i: 1 for i in range(num_friends)}
            for x in range(len(M)):
                for y in range(x+1, len(M[0])):
                    if M[x][y] == 1:
                        num_friends = union(x,y,num_friends, parent, size)
            return num_friends

print(findCircleNum([[1,1,1],[1,1,1],[1,1,1]]))