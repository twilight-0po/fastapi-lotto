f = open('student_name.txt', 'r', encoding='utf-8')
file_contents = f.read()
print("=" * 5 + "받는 사람 명단" + "=" * 5)
print (file_contents)
f.close()

receiver = input("상품 받는 사람 학번: ")

file = open("student_name.txt", "r", encoding='utf-8')
replacement = ""
for line in file:
    line = line.strip()
    if receiver in line:
        line = ""
        replacement = replacement + line
    else:
        replacement = replacement + line + "\n"

file.close()
# opening the file in write mode
fout = open("student_name.txt", "w", encoding='utf-8')
fout.write(replacement)
fout.close()

f = open('student_name.txt', 'r', encoding='utf-8')
file_contents = f.read()
print("=" * 5 + "받는 사람 명단" + "=" * 5)
print (file_contents)
f.close()