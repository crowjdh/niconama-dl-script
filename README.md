# Usage #
## Prerequisite ##
- Prepare rtmpdump for niconama. 
  - For MacOS: [here](https://crowjdh.blogspot.kr/2018/02/rtmpdump.html)
  - For Windows: [here](http://nico-lab.net/new_cumtom_rtmpdump_and_ffmpeg_without_n-option_for_nicolive/)
- Login and download player status xml: http://watch.live.nicovideo.jp/api/getplayerstatus?v=lv[ID]

## Video ##
- Generate rtmpdump command and run using:
```bash
# python convert_status_to_command.py /PATH/TO/getplayerstatus.xml
```

## Comment ##
See [here](https://crowjdh.blogspot.kr/2018/02/blog-post.html).
