#
import random

projects = ["Project A", "Project B", "Project C", "Project D"]
project = random.choice(projects)

with open("log.txt", "a", encoding="utf-8") as f:
    f.write(f"Dự án được chọn: {project}\n")

print("Đã ghi vào log:", project)

--02--05--07--08--10--11--12--18--21--22--25--27--31--03--05--07--10
