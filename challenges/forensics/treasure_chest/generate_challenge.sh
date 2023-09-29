#!/bin/bash
FLAG=flag-YouDidntEvenNeedTheKey

# Remove the old treasure chest
if [ -f "treasure_chest.zip" ]; then
  rm treasure_chest.zip
fi

# Create the flag
convert \
  -background black \
  -fill white \
  -pointsize 32 "label:$FLAG" \
  flag.png

# Add the flag without compression
zip -0eP "$FLAG" treasure_chest.zip flag.png
rm flag.png

# And add some value to the treasure chest
for file in $(find ./loot -type f -exec basename "{}" \;); do
  zip -0eP "$FLAG" treasure_chest.zip "loot/$file"
  # Move the files to the root of the archive
  echo -e "@ loot/$file\n@=$file" | zipnote -w treasure_chest.zip
done
