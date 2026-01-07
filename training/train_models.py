import pandas as pd
import time
import os
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import root_mean_squared_error,mean_squared_error
from sklearn.model_selection import RandomizedSearchCV
from training.train_utils import DATA_FILE_PATH,MODEL_DIR,MODEL_PATH

df = (
    pd
    .read_csv(DATA_FILE_PATH)
    .drop_duplicates()
    .drop(columns=['name','model','edition'])
    )

X = df.drop(columns='selling_price')
y = df['selling_price']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

numeric_cols = X_train.select_dtypes(include='number').columns.tolist()
categorical_cols = X_train.select_dtypes(include='O').columns.tolist()

numeric_pip = Pipeline(steps=[
    ('imputer',SimpleImputer(strategy='median')),
    ('scaler',StandardScaler())

])

categorical_pip = Pipeline(steps=[
    ('imputer',SimpleImputer(strategy='constant',fill_value='missing')),
    ('encoder',OneHotEncoder(handle_unknown='ignore',sparse_output=False))
])

preprocessor = ColumnTransformer(transformers=[
    ('num',numeric_pip,numeric_cols),
    ('cat',categorical_pip,categorical_cols)
])

preprocessor.fit_transform(X_train)

xgb = XGBRegressor(
    n_estimators=500,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="reg:squarederror",
    tree_method="hist",   # 🔥 GPU
    device="cuda",
    random_state=42
)

xgb_model = Pipeline(steps=[
    ("pre", preprocessor),
    ("reg", xgb)
])

start = time.perf_counter()
xgb_model.fit(X_train, y_train)
xgb_train_time = time.perf_counter() - start

print(f"XGBoost GPU Training Time: {xgb_train_time:.2f} seconds")

os.makedirs(MODEL_DIR,exist_ok=True)
joblib.dump(xgb_model,MODEL_PATH)