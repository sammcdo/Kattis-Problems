import os

from autokattis import Kattis
from dotenv import load_dotenv
import shutil

load_dotenv(".env")

extensions = {
    "Python 3": ".py",
    "C++": ".cpp",
}

# Log in to kattis
kt = Kattis(os.environ.get("K_USER"), os.environ.get("K_PASS"))

probs = kt.problems()
print(probs[0])

for i in probs:
    id = i["link"].split("/")[-1]
    print(id)
    if id == "busskortet":
        print("\t\tfound")
        print(i)