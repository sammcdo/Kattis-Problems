import heapq


for i in range(int(input())):
    input()
    g, m = map(int, input().split())

    g_ppl = [int(i) for i in input().split()]
    m_ppl = [int(i) for i in input().split()]

    heapq.heapify(g_ppl)
    heapq.heapify(m_ppl)

    while len(g_ppl) > 0 and len(m_ppl) > 0:
        if g_ppl[0] < m_ppl[0]:
            heapq.heappop(g_ppl)
        else:
            heapq.heappop(m_ppl)
    
    if len(g_ppl):
        print("Godzilla")
    else:
        print("MechaGodzilla")