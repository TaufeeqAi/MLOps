# MLOps Project - End to End Machine Learning Pipeline

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![MLflow](https://img.shields.io/badge/MLflow-Latest-blue)](https://mlflow.org/)
[![DagsHub](https://img.shields.io/badge/DagsHub-Enabled-green)](https://dagshub.com/)

## 🎯 Project Overview

This project implements a complete end-to-end Machine Learning pipeline following MLOps best practices. It includes data ingestion, validation, transformation, model training, and evaluation using MLflow and DagsHub for experiment tracking and model registry <mcreference link="https://instatus.com/blog/mlops-playbook" index="1">1</mcreference>.

## 🚀 Features

- Automated ML Pipeline with modular components
- Data validation and quality checks
- Feature engineering and preprocessing
- Model training and hyperparameter tuning
- Experiment tracking with MLflow
- Model versioning and registry
- Continuous Integration/Deployment ready

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd MLOps
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📋 Project Structure

```
MLOps/
├── config/           # Configuration files
├── src/MLOps/        # Source code
│   ├── components/   # Pipeline components
│   ├── config/      # Configuration utilities
│   ├── constants/   # Project constants
│   ├── entity/      # Data models/schemas
│   ├── pipeline/    # Training pipelines
│   └── utils/       # Utility functions
├── research/         # Jupyter notebooks for experimentation
├── templates/        # HTML templates
├── mlruns/          # MLflow experiment tracking
└── tests/           # Unit tests
```

## 🔄 MLOps Pipeline Workflow

1. **Data Ingestion**
   - Raw data collection and storage
   - Data versioning and cataloging

2. **Data Validation**
   - Schema validation
   - Data quality checks
   - Data drift detection

3. **Data Transformation**
   - Feature engineering
   - Data preprocessing
   - Feature scaling and encoding

4. **Model Training**
   - Algorithm selection
   - Hyperparameter tuning
   - Cross-validation

5. **Model Evaluation**
   - Performance metrics tracking
   - Model validation
   - MLflow experiment logging

## 🔧 Configuration

The project uses three main configuration files:

1. `config.yaml`: Main configuration parameters
2. `schema.yaml`: Data schema definition
3. `params.yaml`: Model hyperparameters

## 📊 Experiment Tracking

All experiments are tracked using MLflow and synchronized with DagsHub. Access the experiment tracking UI at:
```
http://localhost:5000
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request <mcreference link="https://www.welcometothejungle.com/en/articles/btc-readme-documentation-best-practices" index="2">2</mcreference>.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- MLflow for experiment tracking
- DagsHub for model registry
- All contributors to this project