# Cancer classification demo

This local demo trains a tabular classification model from paired CSV files and
provides a small browser UI for submitting feature rows.

**This is a research/demo project, not a medical device. Its predictions are not
diagnoses and must not be used to make healthcare decisions.**

## Dataset

Place the dataset files here:

- `backend/data/data.csv` — one row per sample, with feature names in the header.
- `backend/data/labels.csv` — one row per sample. If it has multiple columns,
  the last column is used as the label.

The files must have the same number of rows and be in the same sample order.
The dataset is not included in this scaffold.

## Run locally

1. Create a Python environment, then install backend dependencies:

   ```sh
   python -m venv .venv
   # Windows: .venv\Scripts\activate
   # macOS/Linux: source .venv/bin/activate
   pip install -r backend/requirements.txt
   ```

2. Train the model and create the example CSV:

   ```sh
   python backend/train.py
   python backend/make_sample.py
   ```

3. In one terminal, start the API:

   ```sh
   python backend/app.py
   ```

4. In another terminal, start the frontend:

   ```sh
   cd frontend
   npm install
   npm run dev
   ```

The frontend expects the API at `http://localhost:5000` through the Vite
development proxy. Upload a CSV whose headers match the feature columns in
`data.csv`. `frontend/public/sample.csv` is generated from the first feature row
in the supplied dataset.
