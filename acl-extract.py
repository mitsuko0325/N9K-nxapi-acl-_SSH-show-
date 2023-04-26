# show runから、行数指定for line in lines[54:98321]:でip access-list関連のConfigだけを抜く
# ACLだけのConfigあるなら不要


# ファイルの読み込み
with open('config.txt', 'r') as f:
    lines = f.readlines()

# ファイルの書き込み
with open('acl.txt', 'w') as f:
    for line in lines[54:98321]:
        f.write(line)
