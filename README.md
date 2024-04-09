# IITK at SemEval-2024 Task 4: MULTILINGUAL DETECTION OF PERSUASION TECHNIQUES IN MEMES

The following repository contains the source code for our submission in the [Task 4 of SemEval-2024](https://propaganda.math.unipd.it/semeval2024task4/). The link to the [paper](http://arxiv.org/abs/2404.04520)

## Table of Contents
- [Directory Structure](#directory-structure)
- [Running](#running)
  - [HypEmo-Task1 - Training and Inference](#hypEmo-task1---training-and-inference)
  - [HypEmo-Task2 - Training and Inference](#hypEmo-task2---training-and-inference)
  - [CDP - Training and Inference](#cdp---training-and-inference)
- [Our Models:](#our-models)
  - [Drive Directory Structure](#drive-directory-structure)
- [Code Reference](#code-reference)



## Directory Structure

```bash
IITK-SemEval-2024-Task-4-Persuation-Techniques/
├── HypEmo-Task1
│   ├── Hypemo
│   │   ├── data
│   │   ├── exp
│   │   ├── label_tree
│   │   └── train_label_embedding.py
│   ├── Merged_test_for_HypEmo_Task1.csv
│   ├── Results-Creation-Translation-HypEmo-Task1.ipynb
├── Hypemo-Task2
│   ├── Hypemo
│   │   ├── data
│   │   ├── exp
│   │   ├── label_tree
│   │   └── train_label_embedding.py
│   ├── Merged_test_for_HypEmo_Task2b.csv
│   ├── Results-Creation-Translation-HypEmo-Task2b.ipynb
├── Fine-Grained-Emotion
│   ├── FineGrained-Emotion-Prediciton-Using-Definitions-new
│   │   ├── ckpt
│   │   ├── config
│   │   ├── data
│   │   └── run_def_nsp-mlm.py
│   ├── Merged_test_for_CDP_2a.csv
│   ├── Merged_test_for_CDP_Task1.csv
│   ├── Results-Creation-Translation-CDP-Task1.ipynb
│   └── Results-Creation-Translation-CDP-Task2a.ipynb
├── README.md
└── Data-Creation-Techniques
    ├── CLIP-embeddings.ipynb
    ├── Training-Creation-Translation-HypEmo-2b.ipynb
    ├── Training-Creation-Translation-CDP-Task1.ipynb
    ├── Training-Creation-Translation-CDP-Task2b.ipynb
    └── Training-Creation-Translation-HypEmo-Task2b.ipynb
```

- `HypEmo-Task1/`
    - For training using HypEmo only and generating predictions for task-1.
- `HypEmo-Task2/`
    - For training using HypEmo only and generating predictions for task-2 using CLIP embeddings.
- `Fine-Grained-Emotion/`
    - Consists of codes utilised for CDP in Task-1 and Task-2.
- `Data-Creation-Techniques/`
    - `CLIP-embeddings.ipynb`
        - To create CLIP embeddings for the training and testing dataset
    - `Training-Creation-Translation-HypEmo-2b.ipynb`
        - To create training and testing dataset for HypEmo Task 2a
    - `Training-Creation-Translation-CDP-Task1.ipynb`
        - To create training and testing dataset for CDP Task 1
    - `Training-Creation-Translation-CDP-Task2b.ipynb`
        - To create training and testing dataset for CDP Task 2b
    - `Training-Creation-Translation-HypEmo-Task2b.ipynb`
        - To create training and testing dataset for HypEmo Task 2a
  


## Running

### HypEmo-Task1 - Training and Inference

- Using `python train.py` to generate the softmax predictions.
- Generate the predictions using `Results-Creation-Translation-HypEmo-Task1.ipynb` for task1.

### HypEmo-Task2 - Training and Inference

- Using `python train.py` to generate the softmax predictions.
- Generate the predictions using `Results-Creation-Translation-HypEmo-Task2b.ipynb` for task 2a.

### CDP - Training and Inference
- Using `python run_def_nsp-mlm.py --taxonomy subtask_nsp-mlm_0.3.json` to generate the predictions for task1.
- Using `python run_def_nsp-mlm.py --taxonomy subtask_nsp-mlm_0.4.json` to generate the predictions for task2a.
- Generate the predictions using `Results-Creation-Translation-CDP-Task1.ipynb` for task1.
- Generate the predictions using `Results-Creation-Translation-CDP-Task2a.ipynb` for task2a.


## Our Models: 
The models trained and used for submission can be found below:
https://1drv.ms/f/s!AuBOJ2hW9GimhZsGvBc6Y_JrXf5Xtg?e=Nwtyar


### Drive Directory Structure

```bash
Drive/
├── Models
│   ├── HypEmo-Task1
│   ├── HypEmo-Task2
│   └── Fine-Grained-Emotion
└── Submitted_files
    ├── Sub-Task 1
    ├── Sub-Task 2
```

- `Models/`
    - Consists of the trained models.

- `Submitted-files/`
    - Consists of the submitted files.


## Code Reference
https://github.com/dinobby/HypEmo

https://github.com/Exploration-Lab/FineGrained-Emotion-Prediciton-Using-Definitions
