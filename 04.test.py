import os
print(os.environ)
print (os.environ.get('USER'))

import dotenv
from dotenv import load_dotenv
load_dotenv()
import os
token = os.environ.get("api-token")