# Course 02 – Practical Machine Learning 

In this course, the **Ford Car Price Prediction** Project demonstrates a modular and autonomous ML workflow covering practical supervised and unsupervised learning. The focus is on end-to-end machine learning, including data preprocessing, model creation, evaluation, and automated reporting. From this point onward, all phases and courses follow the same project-focused approach, building real-world projects on the solid foundations established in earlier phases.

---

## 📁 Project Structure

```text
project-ford-car-price/
├── data/            → Input datasets (CSV format)
├── models/          → Saved trained models
├── results/         → Evaluation reports and visualizations (PDF and PNG)
├── src/             → Modular code components for each pipeline step
├── main.py          → Entry point to run the entire workflow
└── requirements.txt → Python dependencies
```
---

## 🛠 Features

### Modular Workflow
The machine learning pipeline is organized into separate, reusable modules for clarity and maintainability:

- **Data Loading & Preprocessing**
- **Feature Engineering**
- **Model Creation & Training**
- **Evaluation & Scoring**
- **Automated Report Generation**

#### Autonomous Execution
Running `main.py` executes the entire workflow from start to finish automatically.

#### Flexible Datasets
Compatible with the provided Ford car dataset or any other CSV file with a similar structure.

##### Automated Reporting
Generates PDF reports containing evaluation metrics, visualizations, and performance summaries.

##### Reproducibility
All preprocessing, model training, and evaluation steps are fully reproducible, ensuring consistent results.

---

## 📊 Outputs

- **Trained Models:** All models are saved in the `models/` directory.  
- **Evaluation Results:** Metrics and scores are recorded in `results/evaluation-results.csv`.  
- **Comprehensive Report:** A detailed PDF report summarizing the project is available at `results/ford-project-report.pdf`.  

---

## ⚡ Project Highlights

- Modular codebase designed for scalability and maintainability.  
- Fully autonomous workflow for experimenting with different datasets.  
- Provides practical, hands-on insight into real-world ML pipelines.