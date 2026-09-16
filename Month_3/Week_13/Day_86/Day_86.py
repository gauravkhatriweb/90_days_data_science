"""
Day 86 — Finding structure without labels
==========================================
K-MEANS ALWAYS RETURNS AN ANSWER. That is its main danger.
It will cluster PURE NOISE into k tidy groups and report a result.

Exercise 3 is the lesson. Exercise 9 is what turns a picture into evidence.
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

rng = np.random.default_rng(42)


# 1 -- obviously clustered data. Plot assignments and centres.
def ex_01(n=600):
    centres = np.array([[0, 0], [6, 6], [0, 7]])
    X = np.vstack([c + rng.normal(0, 1, (n // 3, 2)) for c in centres])
    km = KMeans(n_clusters=3, n_init=10, random_state=0).fit(X)
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(X[:, 0], X[:, 1], c=km.labels_, s=8)
    ax.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], marker="X", s=200)
    ax.set_title("k-means on data that genuinely has three clusters")
    return X


# 2 -- ELBOW and SILHOUETTE for k = 2..10. DO THEY AGREE?
#      elbow suggests k = ____   silhouette suggests k = ____
#      WHAT WOULD I DO IF THEY DISAGREED?
def ex_02(X):
    ks = range(2, 11)
    inertia, sil = [], []
    for k in ks:
        km = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X)
        inertia.append(km.inertia_)
        sil.append(silhouette_score(X, km.labels_))
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
    axes[0].plot(list(ks), inertia, "o-"); axes[0].set_title("Elbow — look for the bend")
    axes[1].plot(list(ks), sil, "s-");     axes[1].set_title("Silhouette — higher is better")
    for ax in axes: ax.set_xlabel("k")
    fig.tight_layout()
    print(f"  best silhouette at k = {list(ks)[int(np.argmax(sil))]}")


# =============================================================================
# 3 -- THE LESSON. k-means on PURE UNIFORM NOISE, k=4.
#      It produces four tidy clusters. It always will.
#      HOW WOULD I HAVE KNOWN, WITHOUT KNOWING THE TRUTH?
# =============================================================================
def ex_03(n=800):
    X = rng.uniform(0, 10, (n, 2))                 # no structure whatsoever
    km = KMeans(n_clusters=4, n_init=10, random_state=0).fit(X)
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(X[:, 0], X[:, 1], c=km.labels_, s=8)
    ax.set_title("Pure uniform noise. Four 'clusters'. k-means never says no.")
    print(f"  silhouette on pure noise: {silhouette_score(X, km.labels_):.4f}")
    print("  a low silhouette is the hint -- but it still returned an answer.")


# 4 -- THE ASSUMPTION FAILURES: elongated, unequal sizes, unequal densities.
#      WATCH IT GET EACH ONE WRONG.
def ex_04(): pass


# 5 -- unscaled vs scaled clustering. ARE THEY THE SAME CLUSTERING?
#      WHY MUST I SCALE?  (Day 65 -- Euclidean distance)
def ex_05(n=500):
    spend = rng.normal(5000, 1500, n)
    age = rng.normal(35, 8, n)
    X = np.column_stack([spend, age])
    raw = KMeans(4, n_init=10, random_state=0).fit_predict(X)
    scaled = KMeans(4, n_init=10, random_state=0).fit_predict(StandardScaler().fit_transform(X))
    agreement = (raw == scaled).mean()
    print(f"  label agreement raw vs scaled: {agreement:.2%}")
    print("  unscaled, the clustering is essentially just 'spend'.")


# 6 -- PCA to 2D for VISUALISATION. Colour by cluster.
def ex_06(): pass


# 7 -- PCA-then-k-means vs k-means on raw features. SAME GROUPS?
def ex_07(): pass


# 8 -- CLUSTER OLIST CUSTOMERS on RFM. Compare with Day 62's RULE-BASED segments.
#      WHICH IS MORE USEFUL TO A BUSINESS, AND WHY?
#      (a shop owner can act on "high value, gone quiet".
#       Can they act on "cluster 3"?)
def ex_08(): pass


# =============================================================================
# 9 -- THE HONEST CHECK.
#      For each cluster, compute a business metric that was NOT used
#      in the clustering. DO THE CLUSTERS DIFFER ON IT?
#
#      metric used for validation:
#      cluster 0: ____   cluster 1: ____   cluster 2: ____   cluster 3: ____
#
#      IF THEY DO NOT DIFFER, THE CLUSTERS MAY BE AN ARTEFACT, NOT A FINDING.
#
#      Almost nobody does this exercise. It is what turns a picture into evidence.
# =============================================================================
def ex_09(): pass


# MINI ASSESSMENT -- 5 minutes
#   "Segment our customers with machine learning."
#     three questions I would ask FIRST:
#       1.
#       2.
#       3.
#     the method I would try:
#     HOW I WOULD KNOW WHETHER THE SEGMENTS ARE REAL:


if __name__ == "__main__":
    X = ex_01()
    print("--- ex_02 choosing k ---");        ex_02(X)
    print("--- ex_03 PURE NOISE ---");        ex_03()
    print("--- ex_05 scaling ---");           ex_05()
    plt.show()
