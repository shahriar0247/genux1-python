if "open computer" in said or "open this pc" in said or "open my computer" in said:
    print("Open Computer command executed")
    os.system("explorer ::{20D04FE0-3AEA-1069-A2D8-08002B30309D}")
    

if "open documents" in said or "open document" in said or "open my document" in said or "open my documents" in said:
    print("Open Documents command executed")

    os.system("explorer shell:document")  

if "open download" in said or "open downloads" in said or "open my download" in said or "open my downloads" in said:
    print("Open Downloads command executed")
    os.system("explorer shell:downloads")

if "open desktop" in said:
    print("Open Desktop command executed")
    os.system("explorer shell:Desktop")

if "open music" in said or "open my music" in said:
    print("Open Music command executed")
    os.system("explorer shell:Music")

if "open video" in said or "open my video" in said or "open videos" in said or "open my videos" in said:
    print("Open Video command executed")
    os.system("explorer shell:Video")

if "open chrome" in said or "open google chrome" in said:
    print("Open Google Chrome command executed")
    os.system("start chrome")

if "open firefox" in said or "open mozilla firefox" in said:
    print("Open Mozilla Firefox command executed")
    os.system("start firefox")

if "open control panal" in said:
    print("Open Control Panal command executed")
    os.system("")