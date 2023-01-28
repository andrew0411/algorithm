'''
que 생성 -- que = PriorityQueue()
원소 추가 -- que.put()
원소 삭제 -- que.get() : 가장 작은 원소를 que에서 제거함과 동시에 return (리스트 pop 같은 느낌)
정렬 기준 -- que.get()[1]

que.qsize() : que의 크기 반환
que.empty() : que가 비었으면 true
que.full()  : que가 다 찼으면 true
'''

'''
heapq

## 힙 기초
heap = []

heappush(heap, 원소) : 첫번째 인자는 원소를 추가할 대상 리스트, 두번째는 추가할 원소
heappop(heap) : 가장 작은 원소를 삭제한 후에 그 값을 리턴
heap[0] : 최솟값을 삭제하지 않고 얻는 방법
heapify(heap) : 리스트를 힙 구조로 만드는 것

## 힙 정렬
def heap_sort(nums):
    heap = []
    heappush(heap, num)

    sorted = []
    while heap:
        sorted.append(heappop(heap))
    return sorted

## 힙 n번째 최소/최대
- scratch
def nth_smallest(nums, n):
    heap = []
    for num in nums:
        heappush(heap, num)

    nth_min = None
    for _ in range(n):
        nth_min = heappop(heap)
    return nth_min

- scratch + heapify
def nth_smallest(nums, n):
    heapify(nums)

    nth_min = None
    for _ in range(n):
        nth_min = heappop(nums)
    
    return nth_min

- nsmallest() 함수
주어진 리스트에서 가장 작은 n개의 값을 담은 리스트를 반환

from heapq import nsmallest

nsmallest(3, [리스트])[-1]

최댓값은 nlargest() 함수

++++++
time complexity는 n개의 원소들 중에서 t 번째를 찾는 것이면 O(n x log(t))
'''