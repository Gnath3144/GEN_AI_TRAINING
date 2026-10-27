# Day 06 Exercises: Multimodal Vision Inspection

## Exercise 1: Image Base64 Pipeline (Warm-up)
1. Write a Python function `load_and_resize_image(path, max_dim=768)` using Pillow (`PIL`).
2. Downscale any image where width or height exceeds 768px while maintaining aspect ratio.
3. Convert the resized image to JPEG and output a Base64 data URL.

---

## Exercise 2: Hardware Defect & Equipment Auditor (Core Project)
### User Story
As a quality assurance engineer in a manufacturing facility, I need an automated multimodal assistant that inspects photos of hardware assemblies, identifies visible defects, assesses risk severity, and outputs a structured inspection record.

### Acceptance Criteria
1. The script must accept an image file path (or generate a synthetic test image if no path is provided).
2. Format the request for a multimodal model (or fallback mock inspection parser).
3. Extract:
   - Component name.
   - Identified anomaly or defect description.
   - Severity level (`Low`, `Medium`, `High`, `Critical`).
   - Recommended corrective action.
4. Output the structured report in clean JSON.

### Reference Solution
See `solutions/multimodal_analyzer.py`.
