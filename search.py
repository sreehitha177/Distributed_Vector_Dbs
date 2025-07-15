import numpy as np
import faiss
import time

xq = np.load('dataset/bigann_query.npy')
gt = np.load('dataset/bigann_label_10M.npy')

# Normalize if you used cosine similarity
xq = xq / np.linalg.norm(xq, axis=1, keepdims=True)

print("Query shape:", xq.shape)

# Load the index
index = faiss.read_index("faiss_hnsw_10M.index")

# Search parameters
index.hnsw.efSearch = 128  # You can sweep this
k = 10

# Time and search
start = time.time()
D, I = index.search(xq, k)
end = time.time()

latency_ms = (end - start) / len(xq) * 1000
print(f"Avg Latency per query: {latency_ms:.2f} ms")

# Compute Recall@10
def recall_at_k(I, gt, k=10):
    correct = 0
    for i in range(len(I)):
        correct += np.isin(gt[i, :k], I[i, :k]).sum()
    return correct / (len(I) * k)


recall = recall_at_k(I, gt, k)
print(f"Recall@{k}: {recall:.4f}")



for ef in [32, 64, 128, 256, 512]:
    index.hnsw.efSearch = ef
    start = time.time()
    D, I = index.search(xq, 10)
    end = time.time()
    latency = (end - start) / len(xq) * 1000
    recall = recall_at_k(I, gt)
    print(f"efSearch={ef:<3} -> Recall@10: {recall:.4f}, Latency: {latency:.2f} ms")

