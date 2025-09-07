"""
You are given an array of CPU tasks tasks, where tasks[i] is an uppercase
english character from A to Z. You are also given an integer n.

Each CPU cycle allows the completion of a single task, and tasks may be
completed in any order.

The only constraint is that identical tasks must be separated by at least n CPU
cycles, to cooldown the CPU.

Return the minimum number of CPU cycles required to complete all tasks.
"""
from collections import deque
from collections import Counter
import heapq


class Solution:
    """
    The idea to solve this problem is to keep track of the most frequent tasks remaining to
    be processed at any time in a max-heap. Then, through an auxiliary queue, we keep track 
    of all tasks that need to cooldown before being able to be processed again.
    When a previously cooled down tasks is ready to be executed, then it is added back
    to the max heap.
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreq = Counter(tasks)
        maxHeap = [-freq for freq in taskFreq.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while q or maxHeap:
            time += 1

            # if all tasks are currently wating to cooldown, then we can skip ahead in time
            # until the first available task
            if not maxHeap:
                time = q[0][1]
            else:
                freq = -heapq.heappop(maxHeap) - 1
                nextTime = time + n

                if freq > 0:
                    q.append((freq, nextTime))

            # if nex task's cooldown has terminated, then add it back to the max heap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, -q.popleft()[0])

        return time
