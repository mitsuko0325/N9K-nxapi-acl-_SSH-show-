




import os

# ファイルを開き、内容を1行ずつ読み込む
with open("acl.txt", "r") as f:
    lines = f.readlines()

# 現在処理中のファイル名
current_filename = ""

# 出力先のディレクトリを作成
output_dir = "./access-list"
os.makedirs(output_dir, exist_ok=True)

# 行を1行ずつ処理
for line in lines:
    # "ip access-list"が含まれる行を検出
    if "ip access-list" in line:
        # ファイル名を生成
        filename = line[15:].strip() + ".txt"  # 15文字目以降を取得し、空白文字を削除、拡張子を追加
        current_filename = os.path.join(output_dir, filename)  # 出力ファイルのパスを生成

        # 出力ファイルを新規作成し、現在処理中の文字列を書き込む
        with open(current_filename, "w") as out_file:
            out_file.write(line)
    
    # 現在処理中のファイルに文字列を追記
    elif current_filename:
        with open(current_filename, "a") as out_file:
            out_file.write(line)



# remarkで＄の後にSpaceを入力した後、文字を入力してEnterするとエラーになるのを回避するバージョンのScript
# remarkとか考えなくて良いなら不要


# import os

# # ファイルを開き、内容を1行ずつ読み込む
# with open("acl.txt", "r") as f:
#     lines = f.readlines()

# # 現在処理中のファイル名
# current_filename = ""

# # 出力先のディレクトリを作成
# output_dir = "./except-doller-in-remark-access-list"
# os.makedirs(output_dir, exist_ok=True)

# # 行を1行ずつ処理
# for line in lines:
#     # "ip access-list"が含まれる行を検出
#     if "ip access-list" in line:
#         # ファイル名を生成
#         filename = line[15:].strip() + ".txt"  # 15文字目以降を取得し、空白文字を削除、拡張子を追加
#         current_filename = os.path.join(output_dir, filename)  # 出力ファイルのパスを生成

#         # 出力ファイルを新規作成し、現在処理中の文字列を書き込む
#         with open(current_filename, "w") as out_file:
#             out_file.write(line)  # 改行コードを含めて書き込む
    
#     # "remark"が含まれる行の場合
#     elif "remark" in line:
#         # "$"を削除してからファイルに書き込む
#         if current_filename:
#             with open(current_filename, "a") as out_file:
#                 out_file.write(line.replace("$", ""))  # "$"を削除してから書き込む
    
#     # 現在処理中のファイルに文字列を追記
#     elif current_filename:
#         with open(current_filename, "a") as out_file:
#             out_file.write(line)  # 改行コードを含めて書き込む
