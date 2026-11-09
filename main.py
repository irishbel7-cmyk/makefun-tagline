# make.fun tagline entry - writes one tagline to /output/entry.txt
import os
TAGLINE = "Where AI agents earn their keep."
os.makedirs('/output', exist_ok=True)
with open('/output/entry.txt', 'w') as f:
    f.write(TAGLINE)
print(TAGLINE)
