import os
import numpy as np
from PIL import Image, ImageEnhance
import cv2
import streamlit as st  # For creating the webapp


def main():
    st.title("Image Editing App")
    st.text("Edit your Images in a fast and simple way")

    activities = ["Detection", "About"]
    choice = st.sidebar.selectbox("Select Activity", activities)

    if choice == "Detection":
        st.subheader("Face Detection")
        img_file = st.file_uploader(
            "Upload Image", type=["jpg", "png", "jpeg"])

        if img_file is not None:
            img = Image.open(img_file)
            st.text("Original Image")
            st.image(img)  # Displaying the image

            enhance_type = st.sidebar.radio("Enhance type", ["Original", "Grey-scale",
                                                             "Contrast", "Brightness",
                                                             "Blur", "Sharpness",
                                                             "Saturation", "Sepia Tone",
                                                             "Edge Enhancement"])

            if enhance_type == "Grey-scale":
                img_arr = np.array(img.convert('RGB'))
                gray = cv2.cvtColor(img_arr, cv2.COLOR_BGR2GRAY)
                st.image(gray)

            elif enhance_type == "Contrast":
                rate = st.sidebar.slider("Contrast Level", 0.1, 5.0)
                enhancer = ImageEnhance.Contrast(img)
                enhanced_img = enhancer.enhance(rate)
                st.image(enhanced_img)

            elif enhance_type == "Brightness":
                rate = st.sidebar.slider("Brightness", 0.0, 10.0)
                brightness = ImageEnhance.Brightness(img)
                brighter_img = brightness.enhance(rate)
                st.image(brighter_img)

            elif enhance_type == "Blur":
                rate = st.sidebar.slider("Blurriness", 0.0, 10.0)
                blur_img = cv2.GaussianBlur(np.array(img), (15, 15), rate)
                st.image(blur_img)

            elif enhance_type == "Sharpness":
                rate = st.sidebar.slider("Sharpness Level", 0.0, 10.0)
                sharp = ImageEnhance.Sharpness(img)
                sharp_img = sharp.enhance(rate)
                st.image(sharp_img)

            elif enhance_type == "Saturation":
                saturation_rate = st.sidebar.slider(
                    "Saturation Level", 0.0, 5.0)
                saturation = ImageEnhance.Color(img)
                saturated_img = saturation.enhance(saturation_rate)
                st.image(saturated_img)

            elif enhance_type == "Sepia Tone":
                img_arr = np.array(img.convert('RGB'))

                # Define Sepia Tone matrix
                sepia_matrix = np.array([[0.393, 0.769, 0.189],
                                        [0.349, 0.686, 0.168],
                                        [0.272, 0.534, 0.131]])

                # Add a slider for Sepia Tone intensity
                sepia_intensity = st.sidebar.slider(
                    "Sepia Intensity", 0.0, 1.0, 0.5)

                sepia_img = np.dot(img_arr, sepia_matrix.T)
                sepia_img = np.clip(sepia_img * sepia_intensity,
                                    0, 255).astype(np.uint8)

                st.image(sepia_img)

            elif enhance_type == "Edge Enhancement":
                img_arr = np.array(img.convert('RGB'))
                gray = cv2.cvtColor(img_arr, cv2.COLOR_BGR2GRAY)

                # Add a slider for Sobel filter kernel size
                sobel_kernel_size = st.sidebar.slider(
                    "Sobel Kernel Size", 3, 15, 5)

                edges = cv2.Sobel(gray, cv2.CV_64F, 1, 1,
                                  ksize=sobel_kernel_size)
                enhanced_img = cv2.convertScaleAbs(edges)
                st.image(enhanced_img, channels="GRAY")

            elif enhance_type == "Original":
                st.image(img, width=300)

            else:
                st.image(img, width=300)

    elif choice == "About":
        st.subheader("About the Developer")
        st.markdown(
            "Built with ❤️ by [Shubham Kumar](https://www.linkedin.com/in/shubham-911/)")
        st.text(
            "My name is Shubham Kumar I am a Computer Science Student at NMIMS Navi Mumbai")


main()
