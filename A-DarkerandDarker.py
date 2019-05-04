import copy

x,y = list(map(int, input().split()))
input_mark = []
total_count = 0

for i in range(x):
  input_mark.append(list(input()))

input_mark_bk = copy.deepcopy(input_mark)

while True:
  black_row_index = []
  all_black_row_nums = 0
  for i in range(x):
    # '#'が存在する行のインデックスを取得しておく
    if '#' in input_mark[i]:
      black_row_index.append(i)
    if '.' not in input_mark[i]:
      all_black_row_nums += 1
  # 全ての値が'#'だったら終了
  if all_black_row_nums == x:
    print(total_count)
    exit()
  for i in black_row_index:
    # '#'が存在する列のインデックスを取得しておく
    black_col_index = [k for k, x in enumerate(input_mark_bk[i]) if x == '#']
    for j in black_col_index:
      # 値が'#'だったら上下左右の値を'#'に変更(ここには無駄があるが改善方法思いつかず...)
      if input_mark_bk[i][j] == '#':
        # i=0の時はi-1は操作対象外
        if i != 0:
          input_mark[i-1][j] = '#'
        # i=x-1の時はi+1は操作対象外
        if i != x-1:
          input_mark[i+1][j] = '#'
        # j=0の時はj-1は操作対象外
        if j != 0:
          input_mark[i][j-1] = '#'
        # j=y-1の時はj+1は操作対象外
        if j != y-1:
          input_mark[i][j+1] = '#'
  total_count+=1
  input_mark_bk = copy.deepcopy(input_mark)   

