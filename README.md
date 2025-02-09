# Transport Demand Assessment Program Using Matrix Models 🚏

## Table of contents

- [Application Description 🚍](#application-description-)
- [**Software Registration No. 2025610798**](#software-registration-no-2025610798)
- [Stack (Main Libraries) 📚](#stack-main-libraries-)
- [How to Download and Run the Program 🚀](#how-to-download-and-run-the-program-)
- [Screenshots](#screenshots)

## Application Description 🚍

The program is designed to assess passenger transport demand using an inter-stop matrix, a crucial step in planning the operation of urban public transport. The matrix displays the number of trips between stops or zones, allowing the determination of inter-zonal passenger flows. The program also offers graphical representation of passenger flows between specific stopping points.

The main input parameters of the application include the number of passengers boarding and alighting. Upon completion of the calculations, the program generates an inter-stop matrix. This functional solution can be utilized by carriers, municipal authorities, and design organizations to optimize the urban transport system's operation. 🌆

## **Software Registration No. 2025610798**  
**Link:** [STATE REGISTRATION OF THE SOFTWARE PROGRAM](https://new.fips.ru/registers-doc-view/fips_servlet?DB=EVM&DocNumber=2025610798&TypeFile=html "«Transport Demand Assessment Using Matrix Models»")

## Stack (Main Libraries) 📚

- **Programming Language:** Python 🐍
- **Main Libraries:**
  - <span style="color:#4285B4; font-weight: bold;">tkinter, pandas, numpy, scipy</span> — for matrix model calculations and data processing.
  - <span style="color:#4285B4; font-weight: bold;">matplotlib</span> — for plotting error reduction and passenger flow graphs. 📊
  - <span style="color:#4285B4; font-weight: bold;">xlsx-writer</span> — for creating and populating xls files with calculated data. 📄
  - <span style="color:#4285B4; font-weight: bold;">Nuitka</span> — for compiling the project (reduces size and increases application speed). ⚙️

**Program Size:** 277 KB 

- **Computer Type:** IBM PC-compatible 💻
- **Operating Systems:** Windows 10, Linux 🐧
- 
## How to Download and Run the Program 🚀

1. **Download the Program:**
   - Download zip or clone this repository. 📥
   - ```bash
     git clone https://github.com/yermaka-a/Transport-Demand-Assessment
     ```
2. **Set Up Python Environment:**
   - Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).

3. **Create a Virtual Environment:**
   - Open your terminal or command prompt and navigate to the directory where the program files are located.
   - Run the following command to create a virtual environment:
          `python -m venv venv`
     
   - Activate the virtual environment:
     - On Windows:
              `.\venv\Scripts\activate`
       
     - On macOS and Linux:
              `source venv/bin/activate`
       

4. **Install Required Libraries:**
   - Once the virtual environment is active, install the necessary libraries by running:
          `pip install -r requirements.txt`
     

5. **Run the Program:** or compile it with Nuitka:
   - Execute the program by running:
          `python main.py`
   - Compile with nuitka in standalone file:
     ```bash
     python -m nuitka --onefile --standalone --follow-imports --output-dir=dist transport_demand_assessment.py
     ```
     
6. **Using the Program:**
   - Follow the on-screen instructions to input passenger data and generate the inter-stop matrix.
   - Use the graphical interface to visualize passenger flows between stops.

  ## Screenshots

  <details>
    <summary>🔍 Click here to open</summary>
    <img alt="first" src="https://github.com/user-attachments/assets/d99f4359-12bf-4f69-8af0-eb92a3a83c1a">
    <img alt="first" src="https://github.com/user-attachments/assets/d4f1b8a3-7067-4e8c-8b5d-b462af48d12b">
    <img alt="first" src="https://github.com/user-attachments/assets/ba053db1-dbfc-4a54-a6b2-c7d6f849cb77">
  </details>
