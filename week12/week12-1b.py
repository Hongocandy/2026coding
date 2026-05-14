#week12-1b.py 841.
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        def helper(now):
            for k in rooms[now]: #函式呼叫函示的版本 也能進行DFS
                if k not in visited:
                    visited.add(k)
                    helper(k)
        visited.add(0)
        helper(0)
        return len(rooms)==len(visited)