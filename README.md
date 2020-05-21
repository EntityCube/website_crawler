# website_tree_crawler
view a website tree structure


Example:
python website_crawler.py www.duckduckgo.com -a -l -m -s

Found 16 links on https://www.duckduckgo.com
```
^
└── https:
    ├── www.duckduckgo.com
    │   ├── assets
    │   │   └── icons
    │   │       └── meta
    │   │           ├── DDG-iOS-icon_60x60.png
    │   │           ├── DDG-iOS-icon_76x76.png
    │   │           ├── DDG-iOS-icon_120x120.png
    │   │           ├── DDG-iOS-icon_152x152.png
    │   │           └── DDG-icon_256x256.png
    │   ├── locale
    │   │   └── en_US
    │   │       └── duckduckgo14.js
    │   ├── lib
    │   │   └── l114.js
    │   ├── util
    │   │   └── u446.js
    │   ├── about
    │   ├── d2794.js
    │   ├── s1898.css
    │   ├── o1898.css
    │   ├── favicon.ico
    │   └── manifest.json
    └── duckduckgo.com
```

Syntax:
website_crawler.py <url> <args>

Arguments:
-a   find links
-s   find scripts
-m   find medias
-l   find stylesheets
-o   output image
