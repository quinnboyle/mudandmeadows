import re, os, base64

os.makedirs('../extracted/images', exist_ok=True)

files = ['mud-and-meadows.html', 'about.html', 'events.html', 'calendar.html']
image_map = {}  # hash -> filename, to deduplicate

for html_file in files:
    path = f'../extracted/{html_file}'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'data:image/(png|jpg|jpeg|gif|svg\+xml|webp);base64,([A-Za-z0-9+/=]+)'
    matches = list(re.finditer(pattern, content))
    print(f'{html_file}: {len(matches)} images found')

    for i, m in enumerate(matches):
        ext = m.group(1).replace('svg+xml', 'svg')
        b64data = m.group(2)
        full_data_uri = m.group(0)

        # Use a hash to deduplicate across files
        import hashlib
        h = hashlib.md5(b64data.encode()).hexdigest()[:8]

        if h not in image_map:
            fname = f'img_{h}.{ext}'
            image_map[h] = fname
            img_path = f'../extracted/images/{fname}'
            with open(img_path, 'wb') as f:
                f.write(base64.b64decode(b64data))
            size_kb = os.path.getsize(img_path) / 1024
            print(f'  Saved {fname} ({size_kb:.1f} KB)')
        else:
            fname = image_map[h]
            print(f'  Reusing {fname} (duplicate)')

        content = content.replace(full_data_uri, f'images/{fname}', 1)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  Updated {html_file}')

print('Done.')
