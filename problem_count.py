
exercise_cnt = []
problem_cnt = []
total = 0
total_chapter_number = 4
chapter_names = ["Smooth Manifolds", "Smooth Maps", "Tangent Vectors", "Submersions and Immersions"]
for ch in range(1, total_chapter_number + 1):
    fobj = open("chapter" + str(ch) + ".tex", "r")
    excnt = 0
    prcnt = 0
    for line in fobj:
        if "begin{customexer" in line:
            excnt += 1
        if "begin{customprob" in line:
            prcnt += 1
    exercise_cnt.append(excnt)
    problem_cnt.append(prcnt)
    total += excnt + prcnt

print("Total number of problems + exercises that I have worked on: %d" % total)
print


for ch in range(1, total_chapter_number + 1):
    print("Chapter %d: %-30s | %2d exercises, %2d problems" % (ch, chapter_names[ch - 1], exercise_cnt[ch - 1], problem_cnt[ch - 1]))

print
print("# = exercise, $ = problem")

for ch in range(1, total_chapter_number + 1):
    bar = ''
    for i in range(exercise_cnt[ch - 1]):
        bar += '#'
    for i in range(problem_cnt[ch - 1]):
        bar += '$'
    print("Chapter " + str(ch) + ": " + bar)

