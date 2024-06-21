# Utilizing SBERL (LLM) in downstream task (Classification)

In this example, the goal is to perform a classification task on the AG News dataset, where we utilize the title to classify the news.<br />
The dataset is available in [HuggingFace](https://huggingface.co/datasets/contemmcm/ag_news), and the following file "[datasetEDA.ipynb](https://github.com/ahmadhatahet/llm-practical-applications/blob/master/SBERTClassification/datasetEDA.ipynb)" perform a quick EDA, where random 250,000 instances out of 1.24M are selected, then a cut of 20% as a test split.

### Example of the Data
| Category | Title |
| -------- | ----- |
| Sci/Tech | Medis Tech misses chance to market power pack |
| Sports | Swiss sack gold medal rider |
| Sports |Pats accused of spying on Jets' signals (AP) |


## Methods Utilized
1. [SBERT+customLayers.ipynb](https://github.com/ahmadhatahet/llm-practical-applications/blob/master/SBERTClassification/SBERT%2BcustomLayers.ipynb) where the information is passed to SBERT, then extract the [CLS] to capture the semantic information. Then the information is represented in 756 dimension vector, which we pass to a couple of neural network layers to perform the classification task.

1. [EmbeddingModel+KNeighborModel.ipynb](https://github.com/ahmadhatahet/llm-practical-applications/blob/master/SBERTClassification/EmbeddingModel%2BKNeighborModel.ipynb) where a combination of embedding model and KNeighbor model are utilized to train an classifier.

