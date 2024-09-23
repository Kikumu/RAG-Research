# parametric model is a pre-trained seq-2-seq model
# parametric just means same architecture or something
# non-parametric  - data used i,.e wikipedia

"""
 so we need:
1) a pretrained Query Encoder + Document Index
2) Pre trained seq2seq model
"""

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')


