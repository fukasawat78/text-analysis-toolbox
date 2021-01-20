Text Analysis ToolBox
==============================

## テキストデータ分析つーる(作成中)

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

* [Text Analysis ToolBox]
	* [Install](#requirements)
	* [Usage](#how-to-run)
	* [Organization](#organization)
    * [Acknowledgements](#acknowledgements)

<!-- /code_chunk_output -->

## Install
`pip install text-analysis-toolbox`

## Usage
```
from text_analysis_toolbox import TextAnalysisToolBox

df = pd.read_csv("./text.csv")

tdd = TextAnalysisToolBox()
```

## Organization

  ```
  python-data-science-notebooks/
    ├── Makefile            <- Makefile with commands like `make data` or `make train`
    ├── README.md           <- The top-level README for developers using this project.
    │
    ├── text-analysis-toolbox/
    │ 
    └── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
                              generated with `pip freeze > requirements.txt`
  ```
  
## Acknowledgements

## License
This project is licensed under the MIT License. See  LICENSE for more details
