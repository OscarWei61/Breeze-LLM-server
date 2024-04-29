# Breeze-LLM-server
Utilizing FastAPI and the Breeze LLM model, an LLM endpoint has been developed to enable users to swiftly deploy a Breeze LLM model on server.

# Model information

Huggingface : https://huggingface.co/YC-Chen/Breeze-7B-Instruct-v1_0-GGUF

# How to install

Install Anaconda (If you have already installed Anaconda, please jump to next step.)
```Shell Script
# 1.Download Anaconda
wget -P /tmp https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
# 2.Install Anaconda
bash /tmp/Anaconda3-2020.02-Linux-x86_64.sh
```
 
Run the following command to set up the environment:  
```Shell Script
# git clone
git clone https://github.com/OscarWei61/Breeze-LLM-server.git
cd Breeze-LLM-server
```
_Note: Using Python 3.7 may encounter errors, whereas Python 3.9 works smoothly. Default install python 3.9 version._
```Shell Script
# 2.Run env setup script
# default to install ctransformers with no GPU acceleration.
conda create --name Breeze --file ./requirements.txt
```
<details>
<summary>
If you want to install ctransformers with CUDA GPU acceleration, you need to uninstall ctransform and replace with:
</summary>

```Shell Script
pip install ctransformers[cuda]
```
</details>

# How to run the program
```Shell Script
# 1.Activate Conda env
conda activate Breeze
python main.py
```
Reminder: Before closing the connection with the server, make sure to stop the server by pressing Ctrl+C. If necessary, use the "kill" command to stop the FastAPI server.