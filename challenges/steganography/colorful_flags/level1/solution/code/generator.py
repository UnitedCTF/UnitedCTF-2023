import argparse
import qrcode
from PIL import Image


def handle_args():
    parser = argparse.ArgumentParser("Colorful codes")

    parser.add_argument('mode', choices=['RGB','RGBA','HSV'], help='QR color mode')
    parser.add_argument("data",  nargs='+', type=str, help="Data to be encoded in QR code")


    # rgb = parser.add_mutually_exclusive_group('RGB')
    # # rgb.add_argument("RGB", action='store_true', help="Data to be encoded in QR code")
    # rgb.add_argument("data", nargs=3, help="Data to be encoded in QR code")

    # rgba = parser.add_argument_group('RGB')
    # # rgba.add_argument("RGBA", action='store_true', help="Data to be encoded in QR code")
    # rgba.add_argument("data", nargs=4, help="Data to be encoded in QR code")

    # parser.add_argument("data1")
    # parser.add_argument("data2")
    # parser.add_argument("data3")``
    # parser.add_argument("data4")

    # parser.

    return parser.parse_args()


def generate_qr(data):
    return qrcode.make(data)


def create_rgb(red_data, green_data, blue_data):
    r_qr = generate_qr(red_data)
    g_qr = generate_qr(green_data)
    b_qr = generate_qr(blue_data)

    r, _, _ = r_qr.convert("RGB").split()
    _, g, _ = g_qr.convert("RGB").split()
    _, _, b = b_qr.convert("RGB").split()

    return Image.merge("RGB", bands=(r, g, b))


def create_rgba(red_data, green_data, blue_data, alpha_data):
    r_qr = generate_qr(red_data)
    g_qr = generate_qr(green_data)
    b_qr = generate_qr(blue_data)
    a_qr = generate_qr(alpha_data)

    r, _, _, _ = r_qr.convert("RGBA").split()
    _, g, _, _ = g_qr.convert("RGBA").split()
    _, _, b, _ = b_qr.convert("RGBA").split()
    _, _, a, _ = a_qr.convert("RGBA").split()

    return Image.merge("RGBA", bands=(r, g, b, a))


def create_hsv(h_data, s_data, v_data):
    h_qr = generate_qr(h_data)
    s_qr = generate_qr(s_data)
    v_qr = generate_qr(v_data)

    h, _, _ = h_qr.convert("HSV").split()
    _, s, _ = s_qr.convert("HSV").split()
    _, _, v = v_qr.convert("HSV").split()

    return Image.merge("HSV", bands=(h, s, v))


def main():
    args = handle_args()
    print(args)

    match args.mode:
        case 'RGB':
            assert (len(args.data) == 3) 
            qr = create_rgb(*args.data)
        case 'RGBA':
            assert (len(args.data) == 4) 
            qr = create_rgba(*args.data)
        case 'HSV':
            assert (len(args.data) == 3)
            qr = create_hsv(*args.data).convert('RGB')

    qr.save("qr.png")
    
    # qr1 = generate_qr(args.data1)
    # qr2 = generate_qr(args.data2)
    # qr3 = generate_qr(args.data3)
    # qr4 = generate_qr(args.data4)

    # r, _, _, _ = qr1.convert("RGBA").split()
    # _, g, _, _ = qr2.convert("RGBA").split()
    # _, _, b, _ = qr3.convert("RGBA").split()
    # _, _, a, _ = qr4.convert("RGBA").split()

    # color_qr = Image.merge("RGBA", bands=(r, g, b, a))

    # color_qr.save("colors2.png")


if __name__ == '__main__':
    main()