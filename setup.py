from setuptools import setup, find_packages

setup(
    name = 'simplefeatureselection',
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests',
    version = '0.0.2',
    license='MIT',
    description = 'Simple Tab Feature Selection',
    author = 'fukasawat',
    author_email = 'tatsuya.fukasawa1024@gmail.com',
    url = 'https://github.com/fukasawat78/simple-feature-selection',
    keywords = [
        'feature selection',
        'feature engineering',
        'tabular data'
    ],
    install_requires=[
        'category-encoders>=2.2.2',
        'scikit-learn>=0.23.2',
        'Boruta>=0.3'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],

)