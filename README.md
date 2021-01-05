Text Data Dashboard
==============================

## 超絶シンプルなテキストデータのダッシュボードツール

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

* [Text Data Dashboard]
	* [Install](#requirements)
	* [Usage](#how-to-run)
	* [Organization](#organization)
    * [Acknowledgements](#acknowledgements)

<!-- /code_chunk_output -->

## Install
`pip install text-data-dashboard`

## Usage
```
from textdatadashboard import TextDataDashboard

df = pd.read_csv("./text.csv")

tdd = TextDataDashboard()
df = tdd.transform(df)
tdd.create_dashboard(df)
```

## Organization

  ```
  python-data-science-notebooks/
    ├── Makefile            <- Makefile with commands like `make data` or `make train`
    ├── README.md           <- The top-level README for developers using this project.
    │
    ├── text-data-bashboard/
    │   └── text_data_dashboard.py
    │ 
    └── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
                              generated with `pip freeze > requirements.txt`
  ```
  
## Acknowledgements

## License
This project is licensed under the MIT License. See  LICENSE for more details
