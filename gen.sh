#!/usr/bin/env bash
cd program;zip -r ../app.zip .;cd ..
echo '#!/usr/bin/env python3' | cat - app.zip > app
chmod a+x app