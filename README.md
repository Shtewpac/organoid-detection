

# Organoid Detection

This repository contains the code for detecting organoids in real-time using a Dino-Lite digital microscope. The code captures video from the microscope, processes the frames to detect organoids based on their color, and saves the annotated video. This implementation uses the OpenCV library for computer vision tasks.

## Features

- Real-time video capture from the Dino-Lite digital microscope
- Organoid detection using color-based segmentation
- Bounding box annotation for detected organoids
- Video recording and saving with annotations

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- OpenCV
- NumPy

You can install the required packages using pip:

```bash
pip install opencv-python numpy
```

### Running the Code

1. Clone the repository:

```bash
git clone https://github.com/Shtewpac/organoid-detection.git
cd organoid-detection
```

2. Run the organoid detection script:

```bash
python organoid_detection.py
```

### Code Overview

#### record_and_save_video(filename)

Captures video from the Dino-Lite microscope, processes each frame to detect organoids, and saves the annotated video.

#### detect_organoid(frame)

Processes a single frame to detect organoids based on their color in the HSV color space, draws bounding boxes around detected organoids, and highlights them.

#### get_last_video_number(directory)

Helper function to determine the number of the last saved video in the specified directory, ensuring that new videos are saved with a sequential filename.

### Example Usage

To start the video capture and organoid detection, run the following command:

```bash
python organoid_detection.py
```

Press `q` to stop the video capture and save the recorded video.

### Contributing

Contributions are welcome! Please fork this repository and submit pull requests with your improvements.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Contact

For any questions or inquiries, please contact the authors:

- William Kraft: [wkraft@umass.edu](mailto:wkraft@umass.edu)
- Isabella Lambros: [ilambros@umass.edu](mailto:ilambros@umass.edu)
- Beatriz Martinez-Martin: [bmartinezmar@umass.edu](mailto:bmartinezmar@umass.edu)
- Yubing Sun: [ybsun@umass.edu](mailto:ybsun@umass.edu)

### Acknowledgements

This project is developed at the Life Science Laboratories, Amherst MA.


