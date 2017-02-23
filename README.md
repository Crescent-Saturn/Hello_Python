# Hello_Python
Learning Python from Rice University through Coursera


### Sublime Text3 设置Python3为默认编译系统
`Tools -> Build System -> New Build System`

    {
     "cmd": ["usr/bin/python3", "$file"], 
     "selector": "source.python", 
      "file_regex": "file \"(...*?)\", line ([0-9]+)"
    }
    
Saved As Python3.sublime-build.
