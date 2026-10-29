// สมุดบันทึกการสอน: ส่งอีเมลแจ้งนักเรียนกลุ่มเสี่ยงด้วย Gmail ของคุณ
// วิธีใช้: เปิดเว็บ > แท็บ "ตั้งค่า" > "ตั้งค่าส่งอีเมลอัตโนมัติ" แล้วคัดลอกโค้ดจากหน้านั้น
// (โค้ดในหน้าเว็บมีรหัสลับ KEY ของเครื่องคุณใส่ไว้แล้ว) ไฟล์นี้เป็นตัวอย่างโครงสร้างเท่านั้น
const KEY = 'ใส่รหัสลับจากหน้าตั้งค่า';
function doPost(e) {
  const d = JSON.parse(e.postData.contents);
  if (d.key !== KEY) return ContentService.createTextOutput('denied');
  MailApp.sendEmail({ to: d.to, cc: d.cc || '', subject: d.subject, body: d.body, name: d.from || 'สมุดบันทึกการสอน' });
  return ContentService.createTextOutput('ok');
}
