import heapq


def solution(operations):
    heap = []
    for oper in operations:
        a = oper.split()
        if a[0] == 'I':
            num = int(a[1])
            heapq.heappush(heap, num)

        else:
            if len(heap) == 0:
                pass
            elif a[1] == '1':
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
            elif a[1] == '-1':
                heapq.heappop(heap)

    if heap:
        heap = heapq.nlargest(len(heap), heap)
        return [heap[0], heap[-1]]
    else:
        return [0, 0]


print(solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
