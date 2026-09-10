import os, json

def ktape_sort(file):
    #print("ktape_sort by adri")
    if not os.path.exists('out'): 
        os.makedirs('out')

    with open(file, 'rb') as f:
        raw = f.read().rstrip(b'\x00') #before reading, ignore the evil ubiart null byte of mistery 
    data = json.loads(raw)
    print(f"Sorting lyrics for {data["MapName"]}")

    data["Clips"] = sorted(data["Clips"], key=lambda c: c["StartTime"])

    with open(f'out/{os.path.basename(file)}', 'wb') as out:
        out.write(json.dumps(data, indent=4, ensure_ascii=False).encode('utf-8') + b'\x00') #add back the evil null byte. ensure non ascii character dont get fucked

    print("\nDone!")
    os.system('pause')
