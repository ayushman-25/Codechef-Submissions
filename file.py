orig_stdout = sys.stdout
f = open("D:\\n1\\New folder\\cp\\out2.txt", 'w')
sys.stdout = f
sys.stdout = orig_stdout
f.close()
