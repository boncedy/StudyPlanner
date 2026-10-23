# ITCS258 Lab 11 — Required work and PDF submission
# งานที่ต้องทำและการส่งรายงาน PDF

Dr. Pisit Praiwattana, your mentor in 2026

Complete **ALL** of the website's numbered parts **01, 02, 03, 04 AND your own
project (05)**. Run the commands yourself and capture the actual output on your
own terminal or browser screen. Combine the evidence into **one PDF report**.

ทำส่วนที่มีหมายเลขบนเว็บไซต์ให้ **ครบทุกส่วน 01, 02, 03, 04 และโปรเจกต์ของคุณเอง
(05)** รันคำสั่งด้วยตนเองและจับภาพผลลัพธ์จริงจากหน้าจอเทอร์มินัลหรือเบราว์เซอร์ของคุณเอง
รวมหลักฐานเป็น **รายงาน PDF หนึ่งไฟล์**

## Required report sections / หัวข้อรายงานที่ต้องมี

| Part / ส่วน | Work and evidence / งานและหลักฐาน |
| --- | --- |
| 01 · Preflight / ตรวจความพร้อม | Capture Node and local Python versions, Docker Client/Server, `docker info` and successful `docker run --rm hello-world`. / แสดงเวอร์ชัน Node และ Python บนเครื่อง Docker Client/Server ข้อมูล Engine และผล hello-world ที่สำเร็จ |
| 02 · Express demo / ตัวอย่าง Express | Run locally and in Docker. Show `/` and `/health`, Dockerfile, .dockerignore, image build, running container, logs, `8080:3000`, host and inside-container requests, greeting/configuration change, source edit/rebuild and cleanup. / รันบนเครื่องและใน Docker แสดงผล API ไฟล์ Docker ผล build สถานะ log พอร์ต คำขอทั้งสองฝั่ง การเปลี่ยนค่าตั้งค่า การแก้ซอร์สแล้ว build ใหม่ และการล้างคอนเทนเนอร์ |
| 03 · FastAPI demo / ตัวอย่าง FastAPI | Show the local Python environment, local and container API responses, Dockerfile, .dockerignore, image build, running container, logs, `8081:8000`, host and inside-container requests, configuration change, source edit/rebuild and cleanup. / แสดงสภาพแวดล้อม Python ผล API บนเครื่องและในคอนเทนเนอร์ ไฟล์ Docker ผล build สถานะ log พอร์ต คำขอทั้งสองฝั่ง การทดลองเปลี่ยนค่าและซอร์ส และการล้างคอนเทนเนอร์ |
| 04 · NestJS bridge / ต่อยอดสู่ NestJS | Show the local TypeScript build, local requests, multi-stage Dockerfile, .dockerignore, image build, running container, logs, port mapping, host and inside-container requests, both experiments and cleanup. / แสดงการ build TypeScript ผลรันบนเครื่อง Dockerfile หลายสเตจ .dockerignore ผล build สถานะ log พอร์ต คำขอทั้งสองฝั่ง การทดลองทั้งสองแบบ และการล้างคอนเทนเนอร์ |
| 05 · Your own project / โปรเจกต์ของคุณเอง | Containerize your own backend. Show its real route, local baseline, adapted Dockerfile and .dockerignore, successful image build, running container, logs, actual port mapping, successful host and inside-container requests, one verified change, problem/fix or preventive check, and safe container shutdown. / นำแบ็กเอนด์ของคุณเองมารันในคอนเทนเนอร์ แสดงเส้นทางจริง ผลรันบนเครื่อง ไฟล์ที่ปรับใช้ ผล build สำเร็จ คอนเทนเนอร์ log พอร์ต คำขอที่สำเร็จทั้งสองฝั่ง การเปลี่ยนแปลงที่ตรวจผลแล้ว ปัญหาและวิธีแก้หรือการตรวจป้องกัน และการหยุดคอนเทนเนอร์ |

## Prepare the report / จัดทำรายงาน

1. Start with your name, student ID, operating system and own project name.
   เริ่มด้วยชื่อ รหัสนักศึกษา ระบบปฏิบัติการ และชื่อโปรเจกต์ของคุณเอง
2. Use five clearly labeled sections matching 01–05 above. Include the command
   and its actual output, with readable screenshots from your own screen and a
   caption explaining what each screenshot proves.
   แยกห้าหัวข้อตามข้อ 01–05 แสดงคำสั่งและผลจริงด้วยภาพที่อ่านชัดจากหน้าจอของคุณเอง
   พร้อมคำบรรยายว่าภาพแต่ละภาพพิสูจน์อะไร
3. Explain image vs container, the host/container port mapping, .dockerignore,
   and configuration changes vs source changes that require a rebuild.
   อธิบาย image กับ container การจับคู่พอร์ต .dockerignore และความต่างระหว่าง
   การเปลี่ยนค่าตั้งค่ากับการแก้ซอร์สที่ต้อง build ใหม่
4. Redact passwords, tokens and other real secrets before exporting. Include
   relevant Dockerfile/.dockerignore contents and safe configuration examples.
   ปิดบังรหัสผ่าน token และข้อมูลลับก่อนส่งออก ใส่เนื้อหา Dockerfile/.dockerignore
   ที่เกี่ยวข้องและตัวอย่างค่าตั้งค่าที่ปลอดภัย
5. Use [the report template](report-template.md) as a checklist; write in English
   or Thai. Screenshots must show your own execution and results.
   ใช้ [แม่แบบรายงาน](report-template.md) ช่วยตรวจรายการ เขียนภาษาอังกฤษหรือไทยได้
   ภาพหน้าจอต้องแสดงการรันและผลลัพธ์ของคุณเอง

## Export and upload / ส่งออกและอัปโหลด

1. Export one PDF named **student_ID_lab11.PDF**. Replace `student_ID` with
   your actual student ID. Example: **6688123_lab11.PDF**.
   ส่งออก PDF หนึ่งไฟล์ชื่อ **student_ID_lab11.PDF** แทน `student_ID`
   ด้วยรหัสนักศึกษาจริง เช่น **6688123_lab11.PDF**
2. Open the PDF and check that all five sections, commands and screenshots are readable.
   เปิด PDF ตรวจว่าครบทั้งห้าส่วน และอ่านคำสั่งกับภาพหน้าจอได้ชัดเจน
3. Upload the PDF to the **Lab 11 assignment on MyCourse**. Confirm that the
   uploaded file opens and has the correct filename.
   อัปโหลด PDF ใน **งาน Lab 11 บน MyCourse** แล้วตรวจว่าไฟล์ที่อัปโหลดเปิดได้
   และมีชื่อไฟล์ถูกต้อง
