from base_camera import BaseCamera


class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    #    imgs = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]

    imgs = [open('file1/vga_0' + f + '.jpg', 'rb').read() for f in ['1', '2', '3', '4', '5', '6', '7']]
    i = 0

    @staticmethod
    def frames():
        while True:
            # time.sleep(0.1)
            # yield Camera.imgs[int(time.time()) % 7]

            # time.sleep(1)
            Camera.i += 1
            # val = random.randint(0, 100) % 7
            yield Camera.imgs[Camera.i % 7]
