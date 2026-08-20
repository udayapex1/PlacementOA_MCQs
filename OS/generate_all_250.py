import json

questions = []

def add_q(topic, difficulty, companies, question, options, answer_idx, explanation):
    global questions
    q_id = len(questions) + 1
    questions.append({
        "id": q_id,
        "difficulty": difficulty,
        "topic": topic,
        "companyPattern": companies,
        "question": question,
        "options": options,
        "answer": answer_idx,
        "explanation": explanation
    })

# UNIT 1: Introduction to OS (18 Qs)
# UNIT 2: Process Management (20 Qs)
# UNIT 3: CPU Scheduling (25 Qs)
# UNIT 4: Threads (15 Qs)
# UNIT 5: Process Synchronization (25 Qs)
# UNIT 6: Deadlocks (25 Qs)
# UNIT 7: Memory Management (25 Qs)
# UNIT 8: Virtual Memory (25 Qs)
# UNIT 9: File Systems (18 Qs)
# UNIT 10: Disk Scheduling (18 Qs)
# UNIT 11: Security & Protection (15 Qs)
# UNIT 12: Linux Concepts & System Calls (18 Qs)
# UNIT 13: Advanced OS Concepts (13 Qs)
# TOTAL = 250 Questions

# --- UNIT 1 ---
add_q("Introduction to OS", "Easy", ["TCS", "Infosys", "Wipro"], "Which of the following is the primary purpose of an Operating System?", ["To provide a user interface for web browsing", "To manage hardware resources and provide an environment for running applications", "To execute database queries efficiently", "To compile high-level programming code into machine instructions"], 1, "The primary goal of an Operating System is to manage computer hardware resources (CPU, memory, disk, I/O) efficiently and provide an abstraction layer for application programs to execute smoothly.")
add_q("Introduction to OS", "Easy", ["Accenture", "Capgemini", "Deloitte"], "In which type of operating system are jobs submitted in batches and processed without user interaction?", ["Time-Sharing Operating System", "Real-Time Operating System", "Batch Operating System", "Distributed Operating System"], 2, "Batch Operating Systems collect jobs of similar requirements into batches and execute them sequentially without direct user interaction during execution. Time-Sharing systems allow multi-user interactive access via time slicing.")
add_q("Introduction to OS", "Medium", ["Amazon", "Microsoft", "Oracle"], "What is the main difference between User Mode and Kernel Mode in modern CPUs?", ["User Mode allows direct hardware execution, while Kernel Mode uses software emulation.", "Kernel Mode has execution access to all CPU instructions and memory, whereas User Mode is restricted.", "User Mode runs faster because it bypasses security checks.", "Kernel Mode can only execute single-threaded tasks."], 1, "Kernel Mode operates at Dual-Mode CPU ring 0 with full access to hardware privileges, sensitive control registers, and memory space. User Mode (ring 3) prevents user applications from executing privileged instructions directly.")
add_q("Introduction to OS", "Easy", ["TCS", "HCL", "Tech Mahindra"], "What component of an operating system directly interacts with the computer hardware?", ["Shell", "Kernel", "Command Prompt", "Compiler"], 1, "The Kernel is the core component of an OS that sits between software applications and physical hardware, directly handling memory, process, device, and file management.")
add_q("Introduction to OS", "Medium", ["Qualcomm", "Intel", "Samsung"], "During the system booting process, which of the following is executed first by the CPU?", ["Operating System Kernel", "Init / Systemd Process", "BIOS / UEFI Firmware", "Bootloader (GRUB)"], 2, "When power is applied, the CPU starts executing non-volatile code stored in ROM/flash memory, which is the BIOS or UEFI firmware. BIOS performs POST and loads the Bootloader, which then loads the OS Kernel into main memory.")
add_q("Introduction to OS", "Easy", ["IBM", "LTIMindtree", "Infosys"], "Which OS architecture bundles all operating system services (scheduling, memory management, file systems) into a single monolithic binary running in kernel space?", ["Microkernel Architecture", "Monolithic Kernel Architecture", "Exokernel Architecture", "Hybrid Architecture"], 1, "A Monolithic Kernel executes all core OS subsystems in a unified privileged kernel address space. Microkernels keep only minimal core services in kernel space.")
add_q("Introduction to OS", "Medium", ["Google", "Meta", "Amazon"], "What happens when a user program attempts to execute a privileged instruction while running in User Mode?", ["The instruction is executed normally with elevated rights.", "The CPU generates a hardware trap/exception, switching execution to Kernel Mode.", "The CPU halts the entire computer system immediately.", "The instruction is ignored and skipped without any error."], 1, "Executing a privileged instruction while in User Mode triggers a hardware protection trap. The CPU transitions control to the OS kernel trap handler, which typically terminates the offending process with a signal.")
add_q("Introduction to OS", "Hard", ["Nvidia", "Qualcomm", "Cisco"], "Which requirement is MOST critical for a Hard Real-Time Operating System (RTOS)?", ["Maximizing overall system throughput and average response time", "Guaranteeing that tasks complete strictly before their specified deadlines", "Providing an aesthetic graphical user interface", "Supporting maximum concurrent virtual memory capacity"], 1, "In a Hard Real-Time OS (e.g. flight control, medical devices), missing a deadline constitutes a total system failure. Deterministic hard deadline enforcement is paramount.")
add_q("Introduction to OS", "Easy", ["TCS", "Wipro", "Cognizant"], "Which of the following is an example of a Command Line Interface (CLI) Shell in Unix/Linux?", ["GNOME", "Bash", "KDE Plasma", "X11"], 1, "Bash (Bourne Again Shell) is a widely used Unix shell and command interpreter. GNOME and KDE Plasma are Graphical User Interfaces (GUIs).")
add_q("Introduction to OS", "Medium", ["Deloitte", "Capgemini", "Accenture"], "Spooling (Simultaneous Peripheral Operations On-Line) was primarily introduced to solve which operational problem?", ["Slow speed differences between CPU and slow I/O devices like printers", "Memory fragmentation in virtual memory systems", "Deadlock occurrence in concurrent processes", "CPU register overflow during context switching"], 0, "Spooling uses disk storage as a buffer queue for data destined for slow peripheral devices (like printers), preventing the fast CPU from waiting synchronously for slow physical devices.")
add_q("Introduction to OS", "Medium", ["Goldman Sachs", "JPMorgan"], "Which system interrupt is routinely generated by a hardware timer to enable time-sharing process context switches?", ["I/O Completion Interrupt", "Page Fault Interrupt", "Timer Interrupt", "Software Trap"], 2, "A hardware timer periodically fires a Timer Interrupt to preempt the currently running process and pass control to the OS short-term scheduler, ensuring fair allocation of CPU time slices.")
add_q("Introduction to OS", "Easy", ["Infosys", "TCS", "Zoho"], "Which OS concept allows multiple program instances to reside in main memory simultaneously, keeping the CPU active by switching to another job when one is waiting for I/O?", ["Multiprogramming", "Single-user mode", "Serial processing", "Batch queuing"], 0, "Multiprogramming increases CPU utilization by holding multiple jobs in memory. When the currently running job blocks on I/O, the OS switches the CPU to another memory-resident job.")
add_q("Introduction to OS", "Hard", ["Microsoft", "Adobe", "Google"], "Consider an OS microkernel design. What is the primary performance trade-off compared to a monolithic kernel?", ["Microkernels consume significantly more disk space.", "Frequent Inter-Process Communication (IPC) and context switching between user-space services reduce performance speed.", "Microkernels cannot support multi-core CPU architectures.", "Microkernels lack support for file systems entirely."], 1, "Microkernels enhance modularity by running file systems, drivers, and networking as user-space daemons. However, requests require user-to-kernel context switches and IPC messages, introducing performance IPC overhead.")
add_q("Introduction to OS", "Medium", ["VMware", "Oracle"], "What is the role of the Dual-Mode operation bit in modern processor registers?", ["To switch between 32-bit and 64-bit address space", "To differentiate between User Mode (mode bit = 1) and Kernel Mode (mode bit = 0)", "To enable or disable floating-point calculations", "To switch between Wi-Fi and Ethernet communication modes"], 1, "The CPU mode bit indicates execution privilege. Mode bit 0 designates Kernel Mode (privileged), while mode bit 1 designates User Mode (unprivileged).")
add_q("Introduction to OS", "Easy", ["HCL", "Wipro", "Tech Mahindra"], "Which of the following is NOT a core responsibility of an Operating System?", ["Process Scheduling", "Memory Allocation", "Source Code Compilation", "File System Management"], 2, "Source code compilation is performed by language compilers (like gcc, javac), which are application software. Process scheduling, memory allocation, and file systems are core OS kernel responsibilities.")
add_q("Introduction to OS", "Medium", ["ServiceNow", "SAP"], "Which component loads the operating system kernel into RAM from persistent storage during system startup?", ["Compiler", "Bootloader", "Device Manager", "Assembler"], 1, "The Bootloader (e.g. GRUB, LILO, Windows Boot Manager) is initialized by firmware to locate, load, and transfer control to the OS kernel into system RAM.")
add_q("Introduction to OS", "Hard", ["Amazon", "Qualcomm"], "Assertion (A): Microkernels are safer and more stable than Monolithic kernels.\nReason (R): In a Microkernel architecture, driver crashes run in user space and do not crash the entire operating system.", ["Both A and R are true, and R is the correct explanation of A.", "Both A and R are true, but R is NOT the correct explanation of A.", "A is true, but R is false.", "A is false, but R is true."], 0, "Because microkernel system services and device drivers execute in isolated user spaces, a failure in a device driver causes only that service daemon to crash and restart, without crashing the privileged kernel core.")
add_q("Introduction to OS", "Easy", ["TCS", "Cognizant"], "Embedded Operating Systems are typically found in which of the following devices?", ["Mainframe Supercomputers", "Washing machines, Smartwatches, and Automotive ECUs", "Cloud Data Center Server Clusters", "Desktop Gaming Rigs"], 1, "Embedded OSs (e.g. FreeRTOS, VxWorks, Embedded Linux) are tailored for low-power, specialized hardware systems like home appliances, automotive units, and IoT wearables.")

print("Unit 1 complete. Current count:", len(questions))
