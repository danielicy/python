# Stacks
from collections import deque
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
browsing_session.append(4)
print(browsing_session)
last = browsing_session.pop()

browsing_session[-1]  # gets last item in stack

# Queues

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()

# Tuples

point = 1, 2

point2 = (1, 2) * 3
