import numpy as np

xb = np.load('dataset/bigann_data_10M.npy')      
xq = np.load('dataset/bigann_query.npy')        
gt = np.load('dataset/bigann_label_10M.npy')     

print("Base shape:", xb.shape)
print("Query shape:", xq.shape)
print("GT shape:", gt.shape)


def normalize(v):
    return v / np.linalg.norm(v, axis=1, keepdims=True)

xb = normalize(xb)
xq = normalize(xq)


import faiss

d = xb.shape[1]
M = 32
efConstruction = 200

index = faiss.IndexHNSWFlat(d, M, faiss.METRIC_INNER_PRODUCT)
index.hnsw.efConstruction = efConstruction
index.hnsw.efSearch = 64  # Start small; increase later for better recall

print("Adding vectors to index...")
index.add(xb)
print("Total indexed:", index.ntotal)



faiss.write_index(index, "faiss_hnsw_10M.index")
print("Index saved to faiss_hnsw_10M.index")

