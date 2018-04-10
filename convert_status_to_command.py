from xml.etree.ElementTree import parse
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: python convert_status_to_command.py /PATH/TO/getplayerstatus.xml"
        sys.exit(1)
    path = sys.argv[1]
    tree = parse(path)
    root = tree.getroot()

    rtmp = root.find('rtmp')
    v_url = rtmp.find('url').text
    ticket = rtmp.find('ticket').text

    que = root.find('stream').find('quesheet').findall('que')[1].text
    v_id, que = que.split(' ')[1:]
    que_0, que_1 = que.split(',')

    offset = 0
    # url = './rtmpdump -vr "%s/%s" -N "%s" -C S:"%s" -p "http://live.nicovideo.jp/watch/%s" -o out.flv' % (v_url, v_id, que, ticket, v_id)
    command = 'rtmpdump -vr "%s/%s.f4v_%d" -C S:%s -E "nlPlayNotice,S:%s|S:mp4:%s|S:%s.f4v_%d|N:%d" -o output.flv' % (v_url, v_id, offset, ticket, que_0, que_1, v_id, offset, offset)
    print command
    # url_ffmpeg = 'ffmpeg -analyzeduration 30M -probesize 30M -f live_flv -i "%s/%s_%d live=1 nofcsub=1 conn=S:%s cmdinv=nlPlayNotice cmdinvamf=S:%s cmdinvamf=S:mp4:%s cmdinvamf=S:%s_%d cmdinvamf=N:%d" -sn -c copy output.flv' % (v_url, que_0, offset, ticket, que_0, que_1, que_1, offset, offset)
