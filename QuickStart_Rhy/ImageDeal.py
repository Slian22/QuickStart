import sys
import os


def set_img_background():
    from QuickStart_Rhy.ImageTools.ColorTools import transport_back, get_color_from_str

    try:
        img = sys.argv[2]
        if img == '-help':
            raise IndexError
        if not os.path.exists(img):
            exit('[ERROR] No Such File: %s' % img)
        to = sys.argv[3]
        try:
            frm = sys.argv[4]
        except IndexError:
            frm = '0,0,0,0'
    except IndexError:
        print('Usage: qs -stbg picture to_color [from_color: default transparency]')
        exit(0)
    else:
        to = get_color_from_str(to)
        frm = get_color_from_str(frm)
        img = transport_back(img, to, frm)
        iname = sys.argv[2].split('.')
        iname = iname[0] + '_stbg.' + ''.join(iname[1:])
        img.save(iname)


def v2gif():
    from QuickStart_Rhy.ImageTools.VideoTools import video_2_gif

    try:
        video = sys.argv[2]
        sz, fps = None, None
        if len(sys.argv) > 3:
            for i in sys.argv[3:]:
                try:
                    if ',' in i:
                        sz = tuple([int(j) for j in i.split(',')])
                    else:
                        fps = int(i)
                except:
                    raise IndexError
        sz = tuple([int(i) for i in sys.argv[3].split(',')]) if len(sys.argv) > 3 and ',' in sys.argv[3] else None
    except IndexError:
        print('Usage: qs -v2gif *.mp4 width,height fps')
        exit(0)
    else:
        video_2_gif(video, sz, fps) if sz and fps else video_2_gif(video, sz) \
            if sz else video_2_gif(video, fps) if fps else video_2_gif(video)


def rmaudio():
    from QuickStart_Rhy.ImageTools.VideoTools import rm_audio
    try:
        video = sys.argv[2]
    except IndexError:
        exit('Usage: qs -rmaudio *.mp4')
    else:
        rm_audio(video)


def v2mp4():
    from QuickStart_Rhy.ImageTools.VideoTools import tomp4
    try:
        video = sys.argv[2]
    except IndexError:
        exit('Usage: qs -v2mp4 <video>')
    else:
        tomp4(video)
