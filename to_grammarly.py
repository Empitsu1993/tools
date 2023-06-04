path = "original.txt"
path_out = "to_grammarly.txt"

with open(path, encoding="utf-8") as f_in:
    for line in f_in:
        if line[0] != "%" and line[1:11] != "usepackage":
            with open(path_out,"a",encoding="utf-8") as f_out:
                f_out.write(line)
                f_out.close()