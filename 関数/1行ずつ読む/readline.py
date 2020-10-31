'''
readline : 一行ずつ読み込む
'''

row_no = 0
file_ob = open('関数/1行ずつ読む/sample.txt', 'r')
while True:
  line = file_ob.readline()
  if line:
    row_no += 1
    print(row_no, ":", line)
  else:
    break