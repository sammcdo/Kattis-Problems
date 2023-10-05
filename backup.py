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

# Delete all previous saved problems
folder = './problems'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

# Get all successful submissions
stats = kt.stats()
print(stats[0])
print(kt.problem(stats[0]["id"]))
for problem in stats:
    if problem["test_case_passed"] != problem["test_case_full"]:
        print("Not fully completed, not including", problem["name"])
    else:
        path = "./problems/"+problem["id"]
        os.mkdir(path)
        if problem["language"] not in extensions:
            print("Not found language", problem["language"], "for", problem["name"])
        else:
            print(problem["id"])
            solutionFilename = problem["id"]+extensions[problem["language"]]
            with open(path+"/"+solutionFilename, 'w') as obj:
                code = kt.get(problem["link"]+"/source/"+solutionFilename)
                code = code.content.decode()
                obj.write(code)

            try:
                p_info = kt.problem(problem["id"])[0]

                with open(path+"/"+problem["id"]+".md", 'w') as obj:
                    p_info["text"] = p_info["text"].replace("$", "**")
                    obj.write(p_info["text"])
            except Exception as e:
                print("Exception with problem", problem["id"])
                print(e)
                print()


