# 📊 Customer Segmentation Analysis

Customer segmentation using **K-Means Clustering** to divide mall customers into distinct groups based on their demographics and spending behavior. This analysis helps businesses target marketing campaigns more effectively.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge)

---

## ✨ Features

- **📈 K-Means Clustering** — Segments customers into optimal groups using the Elbow Method
- **📊 Multi-Parameter Analysis** — Clustering on age, annual income, and spending score
- **🎨 3D Visualization** — Interactive 3D scatter plot showing all 5 customer segments
- **📉 Elbow Method** — Automatic optimal cluster detection
- **📓 Jupyter Notebook** — Step-by-step analysis with explanations

---

## 📋 Dataset

Using the [Mall Customers Dataset](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python) from Kaggle.

| Feature | Description |
|---------|-------------|
| `CustomerID` | Unique customer identifier |
| `Gender` | Male / Female |
| `Age` | Customer age |
| `Annual Income (k$)` | Annual income in thousands |
| `Spending Score (1-100)` | Mall-assigned score based on spending behavior |

---

## 🔍 Analysis Results

The analysis identifies **5 distinct customer segments** using K-Means on Age, Annual Income, and Spending Score:

| Cluster | Profile | Marketing Strategy |
|---------|---------|-------------------|
| 1 | High Income, High Spending | Premium loyalty programs |
| 2 | High Income, Low Spending | Targeted engagement campaigns |
| 3 | Low Income, High Spending | Value deals & installment plans |
| 4 | Low Income, Low Spending | Budget-friendly promotions |
| 5 | Average across all metrics | General marketing |

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.8+ |
| **ML Algorithm** | K-Means Clustering (Scikit-learn) |
| **Visualization** | Matplotlib, Pyplot (3D) |
| **Data Processing** | Pandas, NumPy |
| **Notebook** | Jupyter Notebook |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** installed
- **Jupyter Notebook** or **JupyterLab**

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/Customer-Segmentation-using-ML.git
   cd Customer-Segmentation-using-ML
   ```

2. **Install dependencies**

   ```bash
   pip install pandas numpy scikit-learn matplotlib jupyter
   ```

3. **Run the notebook**

   ```bash
   jupyter notebook "Customer Segmentation from Marketing Data.ipynb"
   ```

### Alternative: Run as Python Script

```bash
python extract_and_run.py   # Extracts code from notebook
python run_notebook.py       # Runs the extracted script
```

---

## 📁 Project Structure

```
Customer-Segmentation-using-ML/
├── Customer Segmentation from Marketing Data.ipynb  # Main analysis notebook
├── Mall_Customers.csv                                # Dataset
├── extract_and_run.py                                # Script to extract notebook code
├── run_notebook.py                                   # Auto-generated runnable script
├── 3d_plot_5_clusters.png                            # 3D cluster visualization
├── output_figure_*.png                               # Generated analysis plots
├── Steps.jpeg                                        # Methodology diagram
└── README.md
```

---

## 📖 Methodology

1. **Data Loading** — Load and explore the Mall Customers dataset
2. **Feature Selection** — Select relevant features for clustering
3. **Elbow Method** — Determine optimal number of clusters (k)
4. **K-Means Clustering** — Apply K-Means with optimal k values
5. **Visualization** — 2D and 3D scatter plots of customer segments
6. **Interpretation** — Profile each cluster for business insights

---

## 📝 Related Article

Read the detailed analysis article on Medium: [**Customer Segmentation Using K-Means Clustering**](https://theanshul.medium.com/customer-segmentation-using-k-means-clustering-ffded3a2695)

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋‍♀️ Author

**Sujitha Kotyada** — [@sujitha-kotyada](https://github.com/sujitha-kotyada)
