import os, json
from transliterate import translit

def ktape_romanizer(file):
    #print("ktape_romanizer by adri")
    if not os.path.exists('out'): 
        os.makedirs('out')

    with open(file, 'rb') as f:
        raw = f.read().rstrip(b'\x00') #before reading, ignore the evil ubiart null byte of mistery 
    data = json.loads(raw)
    print(f"Converting cyrilic lyrics for {data['MapName']}")

    for clip in data['Clips']:
        if 'Lyrics' in clip:
            clip['Lyrics'] = translit(clip['Lyrics'], 'ru', reversed=True)

    with open(f'out/{os.path.basename(file)}', 'wb') as out:
        out.write(json.dumps(data, indent=4).encode() + b'\x00') #add back the evil null byte

    print("\nDone!")
    os.system('pause')
