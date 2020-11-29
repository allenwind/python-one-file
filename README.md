# python-one-file

把Python项目代码转换为可执行文件。假设`program`为项目源码，原理如下：

```bash
#!/usr/bin/env bash
cd program;zip -r ../app.zip .;cd ..
echo '#!/usr/bin/env python3' | cat - app.zip > app
chmod a+x app
```
