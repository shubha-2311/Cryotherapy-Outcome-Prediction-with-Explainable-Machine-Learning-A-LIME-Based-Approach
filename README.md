# Cryotherapy Outcome Prediction with Explainable Machine Learning

This repository contains the dataset and source code associated with the
research paper:

**"Cryotherapy Outcome Prediction with Explainable Machine Learning: A
LIME-Based Approach"**

The work investigates machine-learning-based prediction of cryotherapy
treatment outcomes for cutaneous warts and combines model evaluation,
multi-criteria decision making using TOPSIS, and explainable AI using
LIME.

## Paper

**Conference:** 23rd OITS International Conference on Information
Technology (OCIT 2025)\
**Proceedings:** OCIT 2025, pp. 75--80\
**DOI:** 10.1109/OCIT66168.2025.11400212\
**IEEE Xplore:** https://ieeexplore.ieee.org/document/11400212

### Authors

-   Soumya Chatterjee
-   Shubhadeep Sarkar
-   Debrup Chatterjee
-   Sarbajit Manna
-   Tapas Si

## Repository Contents

The repository is intentionally lightweight and contains the dataset and
five code files used in the study.

``` text
.
├── datasets
  ├── Cryotherapy.xlsx
├── SVM.ipynb
├── RandomForest.ipynb
├── MLP_LIME.ipynb
├── kNN_LIME.ipynb
├── TOPSIS.py
└── README.md
```

### 1. `Cryotherapy.xlsx`

The dataset contains **90 patient records** and the following seven
variables:

  Feature                 Description
  ----------------------- ---------------------------------
  `sex`                   Patient sex
  `age`                   Patient age
  `Time`                  Treatment-related time variable
  `Number_of_Warts`       Number of warts
  `Type`                  Wart type
  `Area`                  Wart area
  `Result_of_Treatment`   Target treatment outcome

`Result_of_Treatment` is used as the binary classification target.

## Methods

Four machine-learning classifiers are implemented:

-   **Random Forest (RF)**
-   **Support Vector Machine (SVM)**
-   **Multi-Layer Perceptron (MLP)**
-   **K-Nearest Neighbors (kNN)**

The experimental workflow consists of:

1.  Loading the cryotherapy dataset.
2.  Separating the patient features from the treatment-outcome target.
3.  Standardizing the input features.
4.  Performing randomized hyperparameter search.
5.  Evaluating the models using **10-fold cross-validation**.
6.  Computing multiple classification metrics.
7.  Applying **TOPSIS** to obtain a multi-criteria comparison of the
    four classifiers.
8.  Applying **LIME** to provide local explanations for individual
    predictions.

## Evaluation Metrics

The experiments evaluate the classifiers using:

-   Accuracy
-   Recall (Sensitivity)
-   Specificity
-   Precision
-   F1-score
-   G-Mean
-   False Positive Rate (FPR)
-   Matthews Correlation Coefficient (MCC)
-   Cohen's Kappa

The notebooks also record training accuracy and CPU training time.

## Model Results

The mean performance values obtained from the 10-fold evaluation are
summarized below.

  --------------------------------------------------------------------------------------------------
  Model      Accuracy   Recall   Specificity   Precision   F1-score   G-Mean FPR (%) MCC (%)   Kappa
                  (%)      (%)           (%)         (%)        (%)      (%)                     (%)
  -------- ---------- -------- ------------- ----------- ---------- -------- ------- ------- -------
  SVM           88.89    89.33         91.33       92.64      89.48    89.31    8.67   80.34   77.57

  Random        94.45    92.00         97.50       98.33      94.37    94.29    2.50   90.23   89.02
  Forest                                                                                     

  kNN           90.00    86.50         93.00       93.83      89.20    89.21    7.00   80.78   79.37

  MLP           93.33    93.33         93.00       95.14      93.40    92.44    7.00   87.35   85.73
  --------------------------------------------------------------------------------------------------

The reported results are the mean values across the 10-fold evaluation.

## TOPSIS

`TOPSIS.py` implements the Technique for Order Preference by Similarity
to Ideal Solution (TOPSIS) to compare the four classifiers across
multiple evaluation criteria.

The implementation:

-   normalizes the metric values,
-   treats **FPR as a cost criterion**,
-   treats the remaining metrics as benefit criteria,
-   assigns equal weights to the criteria,
-   calculates the distance from the ideal and negative-ideal solutions,
    and
-   computes the TOPSIS closeness coefficient.

The resulting TOPSIS score is used to obtain the model ordering.

## LIME Explainability

LIME (Local Interpretable Model-Agnostic Explanations) is used in the
notebooks to explain individual predictions.

The LIME experiments demonstrate how individual patient-level feature
values contribute to the prediction made by the trained classifier. The
notebooks include explanations for examples from both predicted classes.

LIME is used to make the predictions more interpretable rather than
treating the classifier as a completely black-box model.

## Running the Code

### Requirements

A Python environment with the following packages is recommended:

``` bash
pip install numpy pandas scikit-learn scipy matplotlib openpyxl lime jupyter
```

### Run the notebooks

Start Jupyter Notebook:

``` bash
jupyter notebook
```

Then open the required notebook:

``` text
SVM.ipynb
RandomForest.ipynb
MLP_LIME.ipynb
kNN_LIME.ipynb
```

Make sure `Cryotherapy.xlsx` is in the same directory as the notebooks.

### Run TOPSIS

The TOPSIS implementation can be executed using:

``` bash
python TOPSIS.py
```

## Reproducibility Notes

The experiments use fixed random seeds in the model-selection and
cross-validation procedures where specified in the code. The notebooks
perform randomized hyperparameter search followed by 10-fold
cross-validation using the selected hyperparameters.

Because the dataset is relatively small, the reported cross-validation
results should be interpreted as experimental results on this dataset
and not as a substitute for external clinical validation.

## Research Workflow

``` text
                Cryotherapy Dataset
                        │
                        ▼
              Feature Preprocessing
                        │
                        ▼
          Randomized Hyperparameter Search
                        │
                        ▼
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
       SVM             RF              kNN / MLP
        │               │               │
        └───────────────┼───────────────┘
                        ▼
                10-Fold Evaluation
                        │
                        ▼
        Multiple Classification Metrics
                        │
                        ▼
                     TOPSIS
                        │
                        ▼
             Multi-Criteria Comparison
                        │
                        ▼
                      LIME
                        │
                        ▼
             Local Prediction Explanation
```

## Citation

If you use this dataset, code, or methodology in your research, please
cite the associated paper:

> S. Chatterjee, S. Sarkar, D. Chatterjee, S. Manna, and T. Si,
> "Cryotherapy Outcome Prediction with Explainable Machine Learning: A
> LIME-Based Approach," *Proceedings of the 23rd OITS International
> Conference on Information Technology (OCIT 2025)*, pp. 75--80, 2025.
> DOI: 10.1109/OCIT66168.2025.11400212.

## Disclaimer

This repository is provided for **research and educational purposes**.
The models are intended to demonstrate machine-learning approaches for
predicting cryotherapy treatment outcomes and should not be used as a
standalone clinical decision-making system.

## Keywords

`Cryotherapy` · `Cutaneous Warts` · `Machine Learning` ·
`Explainable AI` · `LIME` · `Random Forest` · `SVM` · `MLP` · `kNN` ·
`TOPSIS` · `Medical AI` · `Clinical Decision Support`
