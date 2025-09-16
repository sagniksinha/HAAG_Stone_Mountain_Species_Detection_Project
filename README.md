# 🦌 Stone Mountain Species Detection Project  

![Deer from Camera Trap](./images/Deer-ct.png)  
<sub><i>Example camera-trap image from Stone Mountain</i></sub>

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-blue.svg)](./CONTRIBUTING.md)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)

---

## 🌳 Overview  

This project applies **computer vision** to identify wildlife species from motion-activated camera-trap images across Stone Mountain.  
- **5 camera traps** placed in different ecosystems  
- Earlier approaches using public ML models were **less accurate & slower** than manual labeling  
- Our goal: build a **region-specific training dataset** and a more **effective pipeline** for species ID  

---

## 🛠️ Project Pipeline  

We’re currently running a **two-stage architecture**:

1️⃣ **Stage 1 – Animal Detection**  
> Classify frames as *animal* vs *empty*.  

2️⃣ **Stage 2 – Species Classification**  
> Identify which species appears in the frame.  

<details>
<summary>📊 Click to view pipeline diagram</summary>

*(insert your pipeline graphic here)*  

</details>

---

## 🚀 Recent Progress  

- ✅ Exploratory Data Analysis (EDA) on label distribution & imbalance  
- ✅ Benchmarked species detection using:  
  - [YOLO v8](https://github.com/ultralytics/ultralytics)  
  - GPT-4o  
  - [Segment Anything Model (SAM)](https://github.com/facebookresearch/segment-anything)  

---

## 🎯 Current Focus  

- 📝 Expanding labeled dataset to full **11 k images** using **semi-supervised pseudo-labeling**  
- 🌙 Night-vision augmentation & **domain randomization** to improve nocturnal performance  

---

## 🗓️ Next Steps  

- [ ] Demonstrate reliable **animal vs. empty** classification  
- [ ] Demo initial **species classification**  
- [ ] Build an **MVP** on a small hand-labeled Stone Mountain subset  

---

## 🤝 Contributing  

We welcome pull requests!  
- See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.  
- Check the [issues](./issues) page to pick up tasks.  

---

## 📄 License  

This project is licensed under the [MIT License](./LICENSE).

---

> 💡 **Tip for visitors:** You can open the [issues tab](./issues) to see what’s currently being worked on, or star the repo ⭐ to follow updates!
