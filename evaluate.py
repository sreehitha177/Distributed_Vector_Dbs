def recall_at_k(I, gt, k=10):
    correct = 0
    for i in range(len(I)):
        correct += np.isin(gt[i, :k], I[i, :k]).sum()
    return correct / (len(I) * k)

recall = recall_at_k(I, gt, k=10)
print(f"Recall@{k}: {recall:.4f}")


for ef in [32, 64, 128, 256]:
    index.hnsw.efSearch = ef
    D, I = index.search(xq, k)
    r = recall_at_k(I, gt, k)
    print(f"efSearch={ef} -> Recall@{k}: {r:.4f}")


import time

start = time.time()
D, I = index.search(xq, k)
end = time.time()

latency_per_query_ms = (end - start) / len(xq) * 1000
print(f"Avg Latency per query: {latency_per_query_ms:.2f} ms")

