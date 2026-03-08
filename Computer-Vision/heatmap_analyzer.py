import cv2
import numpy as np

def analyze_heatmap(image_path):
    # 1. Φόρτωση της εικόνας
    image = cv2.imread(image_path)
    if image is None:
        print(f"❌ Σφάλμα: Η εικόνα '{image_path}' δεν βρέθηκε!")
        return

    # 2. Μετατροπή από BGR σε HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 3. Ορισμός ορίων για το "Κόκκινο" χρώμα (Hotspots)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    
    # 4. Δημιουργία Μάσκας (Masking)
    mask = cv2.inRange(hsv_image, lower_red, upper_red)

    # 5. Στατιστική Ανάλυση
    hot_pixels = cv2.countNonZero(mask)
    total_pixels = image.shape[0] * image.shape[1]
    heat_index = (hot_pixels / total_pixels) * 100

    # 6. Εκτύπωση Αποτελεσμάτων
    print("\n" + "="*40)
    print(f"📊 ΑΝΑΛΥΣΗ HEATMAP: {image_path}")
    print(f"📈 Heatmap Index: {heat_index:.2f}%")
    print("="*40)

if __name__ == "__main__":
    print("🚀 Ο αλγόριθμος Computer Vision είναι έτοιμος.")
