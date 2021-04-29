# Privacy Preservation Analytics
Evaluation of Google's differential privacy tool, along with the modifications made, on a real world database.

-> A basic, non-technical introduction to PPA and differential privacy: https://desfontain.es/privacy/differential-privacy-awesomeness.html

-> The tool can be found at: https://github.com/google/differential-privacy
(Only the modified wrapper is present in the repo, so the tool has to be built before cloning)

-> The differentially privacy paper can be found at:  https://arxiv.org/pdf/1909.01917.pdf

-> Tool Requirements: 

    - Linux OS

    - Bazel v.3
    
    - PostgreSQL v.11.0
    
    - Python 3.6 or higher

    Note: Fast and stable internet is absolutely necessary in order to build the tool successfully. 

-> Modifications made include:

    - Conversion of normal SQL queries to the intrinsically private queries that the tool requires
    
    - Improvement in performance overhead using a different mechanism to calculate lower and upper bounds.

-> Database.zip contains the SQL files to create the testing database.

### Working:
- To run a normal query:
    ```python3 Privacy.py <database name> "<Query without the ';' at the end>"```
- To run the test script (only works for the UBER database:
    ```python3 test_privacy.py "<test input file that has all the queries>"```
- To run the modified WWM file:
    ```python3 privacy_wwm.py <database name> "<Query without the ';' at the end>"```
- To run the string matching modified file:
    ```python3 str_privacy.py <database name> "<Query without the ';' at the end>"```

## Authors
- Adithi Satish
- Avnish Goel
- Manah Shetty
