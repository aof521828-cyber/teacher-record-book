# แอป Android (Capacitor)

ห่อเว็บ `../index.html` เป็นแอป Android โดยใส่ไลบรารีไว้ในแอป (ไม่ต้องโหลดจาก CDN)

## Build เอง
```sh
cd app
npm ci
./make-www.sh ../index.html      # คัดลอกเว็บ + ไลบรารีไปที่ www/
python3 make-icons.py            # ไอคอน/หน้าเปิดจากตราวิทยาลัย
npx cap sync android
cd android && ./gradlew assembleRelease
```
ตั้งค่า `TB_KEYSTORE` (path ของไฟล์ .jks) และ `TB_KEYSTORE_PASSWORD` เพื่อเซ็นด้วยคีย์เดิม แอปเวอร์ชันใหม่จึงติดตั้งทับของเดิมได้
ห้ามใส่ไฟล์ .jks ไว้ใน repository
