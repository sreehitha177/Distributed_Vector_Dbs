# Project Plan – Multi-Step Search for Vector Databases (Using FAISS)

## Goal

The goal of this project is to build and test a basic multi-step search system for distributed vector search using FAISS. The idea is to split the data across several machines or partitions, then search them in steps to improve accuracy (recall) while keeping the search fast.

---

## What Is Multi-Step Search?
Instead of searching the entire dataset at once, we:
- Step 1: Use a clustering method (Random/KMeans) to choose the most relevant data partitions for a query.
- Step 2: Search only those selected partitions using FAISS (HNSW index).
- Step 3: Combine the results from those partitions and return the final top matches.
  
## Steps

### Step 1: Single-Host
- Build and run the search system on one computer (or node).
- Measure how long searches take and how accurate the results are.

### Step 2: Split the Data and Use Multiple Machines
- Divide the data into smaller parts and run the search on different machines or processes.
- Two types of splitting:
  - **Random splitting**: Divide the data equally into parts.
  - **K-Means Clustering**.
- Send the query to each part and combine the results.
- Measure time and accuracy again.

### Step 3: Try a Multi-Step Search
- Instead of sending the query to all parts, first identify the parts most likely to have good results.
- Search only those parts.

---

## Building Components

### Step 1: Single-Host Search (Baseline)
- Build a full FAISS index (HNSW) on one machine.
- Run queries and record recall, latency, and number of distance computations.
- This gives a baseline to compare against.
### Step 2: Simple Distributed Search with Partitioning
- Split the dataset randomly across multiple machines or partitions.
- Build a separate HNSW index on each partition.
- Send the query to all partitions or top-k partitions (multi-step).
- Merge results from each partition and evaluate recall and latency.
### Step 3: Explore More Efficient Search
- Try to improve step 2 using smarter partition selection (e.g., based on routing or query-to-centroid distance).
- Evaluate if fewer partitions can be searched while maintaining recall.

---

## Experiments I Will Try

- Split data into 2, 4, or 8 parts.
- Try searching:
  - All parts (simple setup)
  - Only selected parts (multi-step)
- Measure:
  - **Recall**: How many correct results we find.
  - **Latency**: How long each search takes.
  - **Work done**: Number of calculations or steps.

---

## Setup

- **Library**: FAISS
- **Dataset**: 
- **Machines**: Swarm Cluster 
- **Index type**: HNSW 

---

## Potential Research Questions


- How much faster is the search with multiple machines?
- How does recall improve with additional search steps?
- What is the latency/throughput penalty incurred with each step?
- Does dividing the data affect result accuracy?
- Can I get good results by searching only a few parts?


