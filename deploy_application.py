import os
import shutil
ARTIFACT = "customer-service-1.0.0.zip"
DEPLOY_DIR = "deployment"
if os.path.exists(DEPLOY_DIR):
    shutil.rmtree(DEPLOY_DIR)
os.makedirs(DEPLOY_DIR)
shutil.copy(ARTIFACT, DEPLOY_DIR)
print("DEPLOYMENT PACKAGE CREATED")