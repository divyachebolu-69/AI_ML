import heapq
h = [10, 20, 15, 30, 40]
heapq.heapify(h)

heapq.heappush(h, 5)
print(h)


min = heapq.heappop(h)
print("Smallest:", min)
print(h)