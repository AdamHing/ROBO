import os, time, shutil


#run this code to rmove all files in BotCountLog older than X days
print("BotCountLogCleaner\n")
days = input("All files in BotCountLog DIR older than X many days will be deleted: ")



x_days_ago = time.time() - (days * 86400)
root = (r"D:\coding\python\RobloxAFKBots\BotCountLog")

for i in os.listdir(root):
    path = os.path.join(root, i)

    if os.stat(path).st_mtime <= x_days_ago:
        if os.path.isfile(path):
            try:
                os.remove(path)

            except:
                print("Could not remove file:", i)

        else:
            try:
                shutil.rmtree(path)

            except:
                print("Could not remove directory:", i)