import os

from autokattis import Kattis
from dotenv import load_dotenv
import shutil

load_dotenv(".env")

desc = """
These are problems I have solved on [Kattis](https://open.kattis.com)
while preparing for competitive programming competitions.

"""

table = """
<table>
<thead>
<td>Name</td>
<td>Difficulty</td>
<td>Link</td>
</thead>
<tbody>
"""

tableFormat = """
<tr>
<td>{name}</td>
<td>{difficulty}</td>
<td>{link}</td>
</tr>
"""

tableEnd = """
</tbody>
</table>
"""

# Log in to kattis
kt = Kattis(os.environ.get("K_USER"), os.environ.get("K_PASS"))

with open("README.md", 'w') as obj:
    obj.write("# King-McD Kattis Problems\n")

    obj.write(desc)

    kt.plot_problems(filepath="plot.png", show_partial=False)
    obj.write("### Problem Difficulty\n")

    obj.write("![](plot.png)")

    problems = kt.problems(show_partial=False)

    obj.write(table)
    problems.sort(key=lambda x: x["difficulty"])
    hard = []
    s = 0
    for p in problems:
        s += p["difficulty"]
        if p["difficulty"] >= 5.5:
            hard.append(p)
        # p["name"] = p["name"].decode('utf-8')
        obj.write(tableFormat.format(**p))
    
    s /= len(problems)

print("TOTAL NUMBER OF HARD PROBLEMS:", len(hard))
print("AVERAGE PROBLEM DIFFICULTY:", s)

