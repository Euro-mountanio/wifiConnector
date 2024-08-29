import cv2
import  pyzbar.pyzbar
import QRcodeReader


def parse_wifi_data(data_string):
    wifi_list = str(data_string)
    wifi_list.split(";")
    print(wifi_list)
    #pairs = data_string.split(";")[1:-1]
    #return [pair.split(":") for pair in pairs]

def connector(infor):
    data = parse_wifi_data(infor)
    print(data)

    try:

        QRcodeReader.createNewConnection(infor('name'), infor('name'), infor('password'))
        text = "new connection made"
    except:
        text = "failed to create a new connect"

    try:
        QRcodeReader.connect(infor('name'), infor('name'))
        text = " connected"
    except:
        text = " failed to connect"


def decoder(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.pyzbar.decode(gray_img)
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        barcode_info = barcode.data.decode('utf-8')
        cv2.putText(img, barcode_info, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)

        print(barcode_info)
        return barcode_info
# Capture video from camera
def capture():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        infor = decode(frame)
        connector(infor)
        print(infor)

        cv2.imshow("Barcode Reader", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

