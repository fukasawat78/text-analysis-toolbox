Text Data Dashboard
==============================

## 超絶シンプルなテキストデータのダッシュボードツールです。

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

* [Text Data Dashboard]
	* [Requirements](#requirements)
	* [Usage](#how-to-run)
	* [Organization](#organization)
    * [Acknowledgements](#acknowledgements)

<!-- /code_chunk_output -->

## Install
`pip install simplefeatureselection`

## Usage
```
from simplefeatureselection import SimpleFeatureSelection
sfs = SimpleFeature Selection()

df_selected, y = sfs.fit_transform(X, y)
```

## Organization

  ```
  python-data-science-notebooks/
    ├── Makefile            <- Makefile with commands like `make data` or `make train`
    ├── README.md           <- The top-level README for developers using this project.
    │
    ├── simplefeatureselction/
    │   └── simplefeature
    │ 
    └── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
                              generated with `pip freeze > requirements.txt`
  ```
  
## Acknowledgements

## License
This project is licensed under the MIT License. See  LICENSE for more details