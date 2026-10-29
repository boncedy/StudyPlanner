# ITCS258 Lab 11 — Docker report / รายงาน Docker

Student ID / รหัสนักศึกษา: 6788185
<br>
Name / ชื่อ: Daranpob Sianghen
<br>
Operating system / ระบบปฏิบัติการ: Windows
<br>
Docker context / Docker context ที่ใช้: Docker Desktop (Desktop-linux)
<br>
Own project name and repository URL / ชื่อโปรเจกต์ของตนเองและ URL repository:
https://github.com/boncedy/StudyPlanner
<br>
Complete **all five sections below**. Use screenshots of commands and actual output
from **your own screen**. Add readable captions explaining each result. You may
write explanations in English or Thai. Redact secrets before capturing or exporting.

ทำ **ทั้งห้าส่วนด้านล่างให้ครบ** ใช้ภาพคำสั่งและผลลัพธ์จริงจาก **หน้าจอของคุณเอง**
ใส่คำบรรยายที่อ่านได้ชัดเจน อธิบายเป็นภาษาอังกฤษหรือภาษาไทยได้
ปิดบังข้อมูลลับก่อนจับภาพหรือส่งออกไฟล์

Export this completed report as **student_ID_lab11.PDF**, replacing `student_ID`
with your student ID, e.g. **6688123_lab11.PDF**. Upload that PDF to the **Lab 11
assignment on MyCourse**, then open the uploaded file to verify it is readable.

ส่งออกรายงานที่ทำเสร็จเป็น **student_ID_lab11.PDF** แทน `student_ID` ด้วยรหัสนักศึกษา
เช่น **6688123_lab11.PDF** อัปโหลด PDF ใน **งาน Lab 11 บน MyCourse**
แล้วเปิดไฟล์ที่อัปโหลดเพื่อตรวจว่าอ่านได้ชัดเจน

## 01 · Preflight / ตรวจความพร้อม

- Show `node --version`, your local Python version, `docker version` and `docker info`.
  แสดงเวอร์ชัน Node, Python บนเครื่อง, Docker Client/Server และข้อมูล Engine
- Show the successful output of `docker run --rm hello-world`.
  แสดงผลสำเร็จของ hello-world จากหน้าจอของคุณเอง
- Explain which Docker context/engine you used and how you know it is running.
  อธิบาย context/engine ที่ใช้และหลักฐานว่าทำงานแล้ว

Screenshots, commands and explanation / ภาพหน้าจอ คำสั่ง และคำอธิบาย:

## 02 · Express demo / ตัวอย่าง Express

- Local baseline: startup command and successful `/` and `/health` requests on port 3000.
  รันบนเครื่องและแสดงผลคำขอ `/` กับ `/health` ผ่านพอร์ต 3000
- Show your `Dockerfile`, `.dockerignore` and successful `docker build` output with image tag.
  แสดงไฟล์ Dockerfile, .dockerignore และผล build สำเร็จพร้อมแท็กอิมเมจ
- Show `docker run`, `docker ps`, logs and the `8080:3000` port mapping.
  แสดงคำสั่งรัน สถานะคอนเทนเนอร์ log และการจับคู่พอร์ต
- Show successful requests from the host and from inside the Express container.
  แสดงคำขอที่สำเร็จทั้งจากโฮสต์และภายในคอนเทนเนอร์ Express
- Show the greeting change using a runtime variable, then the `lab: 111` result after
  editing source, rebuilding and recreating the container. Explain when a rebuild is needed.
  แสดงผลเปลี่ยนข้อความด้วยตัวแปรขณะรัน และผล `lab: 111` หลังแก้ซอร์ส build และสร้างคอนเทนเนอร์ใหม่
- Show the commands/output used to stop and remove your named lab container when finished.
  แสดงคำสั่งและผลการหยุดและลบคอนเทนเนอร์ของตัวอย่างเมื่อเสร็จแล้ว

Screenshots, commands and explanation / ภาพหน้าจอ คำสั่ง และคำอธิบาย:

## 03 · FastAPI demo / ตัวอย่าง FastAPI

- Local baseline: Python virtual environment/interpreter, startup command, and successful
  `/` and `/health` responses on port 8000.
  แสดงสภาพแวดล้อม Python คำสั่งเริ่มแอป และผล `/` กับ `/health` บนเครื่องผ่านพอร์ต 8000
- Show your `Dockerfile`, `.dockerignore` and successful image build with its tag.
  แสดง Dockerfile, .dockerignore และผล build อิมเมจสำเร็จพร้อมแท็ก
- Show the running container, logs and `8081:8000` mapping.
  แสดงคอนเทนเนอร์ที่ทำงาน log และพอร์ต 8081:8000
- Show successful host and inside-container requests; explain which Python runs each request.
  แสดงคำขอจากโฮสต์และภายในคอนเทนเนอร์ อธิบายว่าแต่ละคำขอใช้ Python ที่ใด
- Show the runtime greeting change and the source-change/rebuild result (`lab: 111`).
  แสดงผลเปลี่ยนข้อความขณะรันและผลหลังแก้ซอร์สแล้ว build ใหม่ (`lab: 111`)
- Show cleanup of your named FastAPI lab container.
  แสดงการหยุดและล้างคอนเทนเนอร์ FastAPI ของตัวอย่าง

Screenshots, commands and explanation / ภาพหน้าจอ คำสั่ง และคำอธิบาย:

## 04 · NestJS bridge / ต่อยอดสู่ NestJS

- Local baseline: `npm run build`, startup and successful local API requests.
  แสดงการ build TypeScript การเริ่มแอป และคำขอ API ที่สำเร็จบนเครื่อง
- Show the multi-stage `Dockerfile`, `.dockerignore`, image tag and successful build.
  แสดง Dockerfile แบบหลายสเตจ .dockerignore แท็กอิมเมจ และผล build สำเร็จ
- Show `docker run`, `docker ps`, logs and the actual host/container port mapping.
  แสดงคำสั่งรัน สถานะคอนเทนเนอร์ log และการจับคู่พอร์ตที่ใช้จริง
- Show successful host and inside-container `/health` requests.
  แสดงผล `/health` ที่สำเร็จทั้งจากโฮสต์และภายในคอนเทนเนอร์
- Show both experiments: greeting/environment change and source edit followed by rebuild
  and container recreation. Explain the build stage and real compiled entrypoint.
  แสดงการทดลองเปลี่ยนข้อความด้วยตัวแปร และแก้ซอร์สแล้ว build/สร้างคอนเทนเนอร์ใหม่
  อธิบายสเตจ build และไฟล์เริ่มทำงานที่คอมไพล์แล้ว
- Show cleanup of your named NestJS lab container.
  แสดงการหยุดและล้างคอนเทนเนอร์ NestJS ของตัวอย่าง

Screenshots, commands and explanation / ภาพหน้าจอ คำสั่ง และคำอธิบาย:

## 05 · My own project / โปรเจกต์ของฉันเอง

Project name / ชื่อโปรเจกต์:
Existing route tested / เส้นทางจริงที่ทดสอบ:
Host port → container port / พอร์ตโฮสต์ → พอร์ตคอนเทนเนอร์:
Image tag and container name / แท็กอิมเมจและชื่อคอนเทนเนอร์:

- Show the local startup and a successful request to your own API.
  แสดงการเริ่มโปรเจกต์บนเครื่องและคำขอ API ของคุณเองที่สำเร็จ
- Include your adapted `Dockerfile`, `.dockerignore`, dependency files and sanitized
  configuration example. Explain the runtime, build steps and entrypoint you chose.
  แสดง Dockerfile และ .dockerignore ที่ปรับใช้ ไฟล์ dependency และตัวอย่างค่าตั้งค่าที่ไม่มีข้อมูลลับ
  อธิบาย runtime ขั้นตอน build และ entrypoint ที่เลือก
- Show a successful image build, `docker run`, `docker ps`, logs and actual port mapping.
  แสดงผล build สำเร็จ คำสั่งรัน สถานะคอนเทนเนอร์ log และพอร์ตจริง
- Show successful requests to your own API from the host **and inside its container**.
  แสดงคำขอที่สำเร็จไปยัง API ของคุณเองจากโฮสต์ **และภายในคอนเทนเนอร์**
- Change one runtime setting or source behavior. Show the commands and verified result;
  state whether you rebuilt the image and recreated the container, and why.
  เปลี่ยนค่าตั้งค่าหรือพฤติกรรมของซอร์สหนึ่งรายการ แสดงคำสั่งและผลตรวจสอบ
  ระบุว่า build อิมเมจและสร้างคอนเทนเนอร์ใหม่หรือไม่ พร้อมเหตุผล
- Document one problem, diagnosis and fix with evidence. If none occurred, explain one
  check you used to prevent a problem. Show how you stopped your project container safely.
  บันทึกปัญหา การวิเคราะห์ และวิธีแก้พร้อมหลักฐาน หากไม่พบปัญหาให้อธิบายการตรวจป้องกันหนึ่งเรื่อง
  แสดงวิธีหยุดคอนเทนเนอร์โปรเจกต์ของคุณอย่างเหมาะสม
- Explain image vs container, why `EXPOSE` alone does not publish a port, why
  `.dockerignore` matters, and why editing host source does not change a packaged image.
  อธิบาย image กับ container เหตุใด EXPOSE ไม่ได้เปิดพอร์ตบนโฮสต์ด้วยตัวเอง
  ความสำคัญของ .dockerignore และเหตุใดแก้ซอร์สบนโฮสต์แล้วอิมเมจไม่เปลี่ยนตาม

Screenshots, commands and explanation / ภาพหน้าจอ คำสั่ง และคำอธิบาย:

Final check: all five sections are complete, screenshots are readable, secrets are
redacted, and the uploaded file is named **your actual student ID followed by _lab11.PDF**.

ตรวจสุดท้าย: ครบทั้งห้าส่วน ภาพอ่านได้ชัดเจน ปิดบังข้อมูลลับ และไฟล์ที่อัปโหลดใช้ชื่อ
**รหัสนักศึกษาจริงของคุณตามด้วย _lab11.PDF**
