#!/usr/bin/env python3
#
# used some <maze@pyth0n.org> wrote code. https://github.com/tehmaze/lolcat
#
# <efvhi> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return.



import re
import math
import random
import sys
import os
import time





STRIP_ANSI = re.compile(r'\x1b\[(\d+)(;\d+)?(;\d+)?[m|K]')
COLOR_ANSI = (
    (0x00, 0x00, 0x00), (0xcd, 0x00, 0x00),
    (0x00, 0xcd, 0x00), (0xcd, 0xcd, 0x00),
    (0x00, 0x00, 0xee), (0xcd, 0x00, 0xcd),
    (0x00, 0xcd, 0xcd), (0xe5, 0xe5, 0xe5),
    (0x7f, 0x7f, 0x7f), (0xff, 0x00, 0x00),
    (0x00, 0xff, 0x00), (0xff, 0xff, 0x00),
    (0x5c, 0x5c, 0xff), (0xff, 0x00, 0xff),
    (0x00, 0xff, 0xff), (0xff, 0xff, 0xff),
)

FREQ = 0.1


def wrap(*codes):
    return '\x1b[%sm' % (''.join(codes),)


def rainbow(freq, i):
    r = math.sin(freq * i) * 127 + 128
    g = math.sin(freq * i + 2 * math.pi / 3) * 127 + 128
    b = math.sin(freq * i + 4 * math.pi / 3) * 127 + 128
    return [r, g, b]


def _distance(rgb1, rgb2):
    return sum(map(lambda c: (c[0] - c[1]) ** 2,
        zip(rgb1, rgb2)))



def ansi( rgb):
    r, g, b = rgb

    if RGB_MODE in (8, 16):
        colors = COLOR_ANSI[:RGB_MODE]
        matches = [(_distance(c, map(int, rgb)), i) for i, c in enumerate(colors)]
        matches.sort()
        color = matches[0][1]

        return '3%d' % (color,)
    else:
        gray_possible = True
        sep = 2.5

        while gray_possible:
            if r < sep or g < sep or b < sep:
                gray = r < sep and g < sep and b < sep
                gray_possible = False

            sep += 42.5

        if gray:
            color = 232 + int(float(sum(rgb) / 33.0))
        else:
            color = sum([16]+[int(6 * float(val)/256) * mod
                for val, mod in zip(rgb, [36, 6, 1])])

        return '38;5;%d' % (color,)


def detect_mode(term_hint='xterm-256color'):
    '''
    Poor-mans color mode detection.
    '''
    if 'ANSICON' in os.environ:
        return 16
    elif os.environ.get('ConEmuANSI', 'OFF') == 'ON':
        return 256
    else:
        term = os.environ.get('TERM', term_hint)
        if term.endswith('-256color') or term in ('xterm', 'screen'):
            return 256
        elif term.endswith('-color') or term in ('rxvt',):
            return 16
        else:
            return 256 # optimistic default




def animate_imgs2ascii(options):
    import glob

    global OS_SEED

    imgs_num = len(glob.glob(pathname=options.dirname+'/*.jpg'))

    i = 0
    duration = 0.075

    while i < imgs_num:
        file_name = options.prefix + ("%04d" % i) + ".jpg"

        out = os.popen("jp2a " + options.dirname + '/' + file_name)


        if options.mode == 'rainbow':
            cxk = out.readlines()

            output = ''

            for line in cxk:
                OS_SEED += 1

                s = STRIP_ANSI.sub('', line)
                for j, c in enumerate(s):
                    rgb = rainbow(FREQ, (OS_SEED + j / 3.0))

                    output += ''.join([
                        wrap(ansi(rgb)),
                        c,
                    ])
        else:
            output = out.read()


        sys.stdout.write(output)
        sys.stdout.flush()

        time.sleep(duration)

        i += 1
        if i == imgs_num:
            i = 0




def run():
    """Main entry point."""
    import optparse

    parser = optparse.OptionParser(usage=r'%prog [<options>] [file ...]')
    parser.add_option('-d', '--dirname', default="imgs",
        help='指定图片文件夹名字')
    parser.add_option('-p', '--prefix',  default='img',
        help='指定图片的前缀名 比如图片是 xyz0001.jpg 那前缀就是 xyz')

    parser.add_option('-m', '--mode', default='rainbow', help='默认是rainbow 终端字体颜色设置为 normal')

    options, args = parser.parse_args()


    animate_imgs2ascii(options)




if __name__ == '__main__':
    OS_SEED = random.randint(0, 256)
    RGB_MODE = detect_mode()

    sys.exit(run())
