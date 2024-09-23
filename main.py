# parametric model is a pre-trained seq-2-seq model
# parametric just means same architecture or something
# non-parametric  - data used i,.e wikipedia

"""
 so we need:
1) a pretrained Query Encoder + Document Index
2) Pre trained seq2seq model
"""

from sentence_transformers import SentenceTransformer
from dataloader.pdf_loader import retrieve_data
import numpy as np
import faiss

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
doc_embeddings = model.encode(retrieve_data("domain_retrieval"))
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

index.add(np.array(doc_embeddings))

# Save the index for future use (optional)
faiss.write_index(index, "document_index.faiss")
