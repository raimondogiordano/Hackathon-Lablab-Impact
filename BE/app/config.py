from dotenv import load_dotenv
import os

load_dotenv()
    
db_url=os.environ['DB_URL']
openai_key=os.environ['OPENAI_API_KEY']
api_prefix=os.environ['API_PREFIX']
base_folder_path=os.environ['BASE_FOLDER_PATH']

url_config={
    "dev":"http://localhost:8000/",
    "prod":"https://archiveye.hr/",
}
base_url=url_config[os.environ['ENV']]

sources={
    "local":base_url+"archive/",
    "sp":""
}