## SocREval 
This is the code repository for the NAACL paper [SocREval: Large Language Models with the Socratic Method for Reference-Free Reasoning Evaluation](https://aclanthology.org/2024.findings-naacl.175.pdf)
If you use this code for your work, please cite
```
@inproceedings{he-etal-2024-socreval,
    title = "{S}oc{RE}val: Large Language Models with the Socratic Method for Reference-free Reasoning Evaluation",
    author = "He, Hangfeng  and
      Zhang, Hongming  and
      Roth, Dan",
    booktitle = "Findings of the Association for Computational Linguistics: NAACL 2024",
    year = "2024",
    publisher = "Association for Computational Linguistics",
    doi = "10.18653/v1/2024.findings-naacl.175",
    pages = "2736--2764",
}
```

## Installing dependencies
Use virtual environment tools (e.g miniconda) to install packages and run experiments\
python==3.7.10\
pip install -r requirements.txt


## Code organization
The code is organized as follows:
- Data processing
    - roscoe_data_processing.py (processing human judged datasets in ROSCOE for our experiments)
- GPT-4 for reference-free reasoning evaluation
    - gpt4_evaluation_gsm8k.py (GPT-4 on GSM8K)
    - gpt4_evaluation_esnli.py (GPT-4 on e-SNLI)
    - gpt4_evaluation_drop.py (GPT-4 on DROP)
    - gpt4_evaluation_cosmos.py (GPT-4 on Cosmos QA)
- SocREval for reference-free reasoning evaluation
    - SocREval_gsm8k.py (SocREval on GSM8K)
    - SocREval_esnli.py (SocREval on e-SNLI)
    - SocREval_drop.py (SocREval on DROP)
    - SocREval_cosmos.py (SocREval on Cosmos QA)

## Change the working path
Change the /path/to/working/dir to the path to your working directory.

## Export OPENAI API KEY
You need to export your own OpenAI API key before running experiments with [OpenAI API](https://openai.com/blog/openai-api), i.e., export OPENAI_API_KEY=$YOUR_OPENAI_API_KEY

## Data preparation 
Following the instructions in [ROSCOE code repository](https://github.com/facebookresearch/ParlAI/tree/main/projects/roscoe):
- Run [download_annotated.sh](https://github.com/facebookresearch/ParlAI/blob/main/projects/roscoe/roscoe_data/download_annotated.sh) to obtain the human judged datasets, including "roscoe/raw", "roscoe/generated", and "roscoe/annotated", and put them all under /path/to/working/dir/
- Run [restore_annotated.py](https://github.com/facebookresearch/ParlAI/blob/main/projects/roscoe/roscoe_data/restore_annotated.py) to restore the annotated files and put them under /path/to/working/dir/roscoe/restore_annotated

## Reproducing experiments
Processing the data for our experiments:
```
python roscoe_data_processing.py 
```
To reproduce the experiments for GPT-4 evaluation:
```
python gpt4_evaluation_gsm8k.py
python gpt4_evaluation_esnli.py
python gpt4_evaluation_drop.py
python gpt4_evaluation_cosmos.py
```
To reproduce the experiments for SocREval:
```
python SocREval_gsm8k.py
python SocREval_esnli.py
python SocREval_drop.py
python SocREval_cosmos.py
```
